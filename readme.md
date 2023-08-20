# NYC Motor Vehicle Collisions

This is a Streamlit dashboard application designed to analyze motor vehicle collisions in New York City. The application utilizes machine learning predictions and data analysis techniques to provide insights into collision patterns and trends within the city.

## Introduction

This application provides an interactive way to explore and understand motor vehicle collisions in NYC. The dashboard leverages various data visualization techniques and predictive modeling to help you gain valuable insights into collision data.

## Usage

To use this application, follow these steps:

1. Install the required dependencies using the provided `requirements.txt` file:
   ```
   pip install -r requirements.txt
   ```

2. Run the Streamlit application using the following command:
   ```
   streamlit run app.py
   ```

3. Once the application is running, you'll be able to interact with different sections of the dashboard.

## Features

### Predicted Injuries Today

In this section, machine learning is used to predict injuries based on the current time and location data. A predictive model is simulated to generate predictions for injuries caused by collisions occurring today. Please note that these predictions are for demonstration purposes only and should not be treated as accurate forecasts.

A map is displayed showing the predicted injuries for various locations within NYC.

### Where are the Most Injured People?

This section allows you to adjust the slider to select the number of persons injured in vehicle collisions. The map will then display the locations of collisions where the number of injured people matches or exceeds the selected value.

### Collisions by Time of Day

Here, you can choose a specific hour of the day using the slider. The dashboard will display a map with a hexagonal heatmap, representing the density of collisions that occurred during the selected hour.

### Collisions Breakdown by Minute

This section provides a breakdown of collisions by minute within the selected hour. A bar chart illustrates the distribution of collisions across the 60 minutes of that hour.

### Top 5 Dangerous Streets by Affected Class

In this section, you can select the affected class (Pedestrians, Cyclists, or Motorists) from the dropdown menu. The dashboard will display the top 5 dangerous streets based on the chosen affected class. Each street is accompanied by the number of injuries recorded for that class.

## Data Source

The application uses the "Motor Vehicle Collisions - Crashes" dataset, which is loaded from a CSV file located at `./Motor_Vehicle_Collisions_-_Crashes.csv`. The dataset includes information about collision dates, times, locations, and injuries.

## Important Note

This dashboard is for demonstration purposes only. The predictive model used for injury predictions is a simulated example and does not reflect an actual machine learning model. Additionally, the insights and predictions provided by this application should not be considered accurate or reflective of actual collision trends.