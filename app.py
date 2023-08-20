import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px
import datetime  
DATE_TIME = "date/time"
DATA_URL = "[url to your collision data]"
st.title("Motor Vehicle Collisions in New York City")
st.markdown("This application is a Streamlit dashboard that can be used "
            "to analyze motor vehicle collisions in NYC 🗽💥🚗")
current_time = datetime.datetime.now()
def predict_injuries(latitudes, longitudes):
  today = current_time
  todays_crashes = [crash for crash in DATA_URL if crash[0] == today]
  predicted_injuries = []
  for lat, lon in zip(latitudes, longitudes):
    nearby_crashes = [crash for crash in todays_crashes if 
                      abs(crash[4] - lat) < 0.1 and abs(crash[5] - lon) < 0.1]
    if len(nearby_crashes) > 0:
      predicted_injuries.append(sum(crash[10] for crash in nearby_crashes))
    else:
      predicted_injuries.append(0)
  return np.array(predicted_injuries)
prediction_data = pd.DataFrame({
    "latitude": np.random.uniform(40.5, 41, 10),  
    "longitude": np.random.uniform(-74.3, -73.7, 10),  
})
prediction_data["predicted_injuries"] = predict_injuries(prediction_data["latitude"], prediction_data["longitude"])
st.header("Predicted Injuries Today")
st.markdown(f"Predictions for {current_time.strftime('%Y-%m-%d %H:%M')} (Predictions offer guidance, not guarantees.)")
st.map(prediction_data[["latitude", "longitude", "predicted_injuries"]].dropna(how="any"))
@st.cache_data(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, parse_dates=[['CRASH_DATE', 'CRASH_TIME']])
    data.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data.rename(columns={"crash_date_crash_time": "date/time"}, inplace=True)
    return data
data = load_data(15000)
st.header("Where are the most people injured in NYC?")
injured_people = st.slider("Number of persons injured in vehicle collisions", 0, 19)
st.map(data.query("injured_persons >= @injured_people")[["latitude", "longitude"]].dropna(how="any"))
st.header("How many collisions occur during a given time of day?")
hour = st.slider("Hour to look at", 0, 23)
original_data = data
data = data[data[DATE_TIME].dt.hour == hour]
st.markdown("Vehicle collisions between %i:00 and %i:00" % (hour, (hour + 1) % 24))
midpoint = (np.average(data["latitude"]), np.average(data["longitude"]))
st.write(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state={
        "latitude": midpoint[0],
        "longitude": midpoint[1],
        "zoom": 11,
        "pitch": 50,
    },
    layers=[
        pdk.Layer(
            "HexagonLayer",
            data=data[['date/time', 'latitude', 'longitude']],
            get_position=["longitude", "latitude"],
            auto_highlight=True,
            radius=100,
            extruded=True,
            pickable=True,
            elevation_scale=4,
            elevation_range=[0, 1000],
        ),
    ],
))
if st.checkbox("Show raw data", False):
    st.subheader("Raw data by minute between %i:00 and %i:00" % (hour, (hour + 1) % 24))
    st.write(data)
st.subheader("Breakdown by minute between %i:00 and %i:00" % (hour, (hour + 1) % 24))
filtered = data[
    (data[DATE_TIME].dt.hour >= hour) & (data[DATE_TIME].dt.hour < (hour + 1))
]
hist = np.histogram(filtered[DATE_TIME].dt.minute, bins=60, range=(0, 60))[0]
chart_data = pd.DataFrame({"minute": range(60), "crashes": hist})
fig = px.bar(chart_data, x='minute', y='crashes', hover_data=['minute', 'crashes'], height=400)
st.write(fig)
st.header("Top 5 dangerous streets by affected class")
select = st.selectbox('Affected class', ['Pedestrians', 'Cyclists', 'Motorists'])
if select == 'Pedestrians':
    st.write(original_data.query("injured_pedestrians >= 1")[["on_street_name", "injured_pedestrians"]].sort_values(by=['injured_pedestrians'], ascending=False).dropna(how="any")[:5])
elif select == 'Cyclists':
    st.write(original_data.query("injured_cyclists >= 1")[["on_street_name", "injured_cyclists"]].sort_values(by=['injured_cyclists'], ascending=False).dropna(how="any")[:5])
else:
    st.write(original_data.query("injured_motorists >= 1")[["on_street_name", "injured_motorists"]].sort_values(by=['injured_motorists'], ascending=False).dropna(how="any")[:5])