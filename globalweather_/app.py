import random
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from shinywidgets import output_widget, render_widget
from shiny import App, render, ui, reactive

# Synthetic Weather Data Generation
def generate_global_weather_data(num_locations=50):
    """Generate synthetic global weather data."""
    locations = [
        {"name": "New York", "lat": 40.7128, "lon": -74.0060},
        {"name": "London", "lat": 51.5074, "lon": -0.1278},
        {"name": "Tokyo", "lat": 35.6762, "lon": 139.6503},
        {"name": "Sydney", "lat": -33.8688, "lon": 151.2093},
        {"name": "Rio de Janeiro", "lat": -22.9068, "lon": -43.1729},
        {"name": "Cairo", "lat": 30.0444, "lon": 31.2357},
        {"name": "Moscow", "lat": 55.7558, "lon": 37.6173},
        {"name": "Mumbai", "lat": 19.0760, "lon": 72.8777},
        {"name": "Beijing", "lat": 39.9042, "lon": 116.4074},
        {"name": "Cape Town", "lat": -33.9249, "lon": 18.4241},
    ]

    weather_data = []
    for _ in range(num_locations):
        location = random.choice(locations)
        weather_data.append({
            "city": location["name"],
            "latitude": location["lat"],
            "longitude": location["lon"],
            "temperature": round(random.uniform(-10, 40), 1),
            "humidity": round(random.uniform(20, 95), 1),
            "wind_speed": round(random.uniform(0, 50), 1),
            "precipitation": round(random.uniform(0, 100), 1),
            "timestamp": datetime.datetime.now(),
            "alert_level": random.choice(["Low", "Moderate", "High"]),
            "description": random.choice([
                "Sunny", "Cloudy", "Rainy", "Windy", "Stormy"
            ])
        })
    
    return pd.DataFrame(weather_data)

# Global weather dataset
global_weather_df = generate_global_weather_data()

# Shiny App UI
app_ui = ui.page_fluid(
    ui.head_content(
        ui.HTML('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">')
    ),
    ui.panel_title("🌍 Global Weather Monitoring Dashboard"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_selectize(
                "selected_city", 
                "Select City", 
                choices=global_weather_df["city"].unique().tolist(),
                multiple=False
            ),
            ui.input_switch("show_alerts", "Show Alerts"),
            ui.input_dark_mode(id="dark_mode")
        ),
        ui.layout_columns(
            ui.card(
                ui.card_header("Current Weather Conditions"),
                ui.output_ui("city_weather_details"),
                full_screen=True
            ),
            ui.card(
                ui.card_header("Weather Metrics"),
                output_widget("weather_metrics_plot"),
                full_screen=True
            ),
            ui.card(
                ui.card_header("Global Weather Alerts"),
                ui.output_data_frame("weather_alerts"),
                full_screen=True
            )
        )
    )
)

def server(input, output, session):
    @reactive.calc
    def selected_city_data():
        return global_weather_df[global_weather_df["city"] == input.selected_city()]

    @render.ui
    def city_weather_details():
        city_data = selected_city_data().iloc[0]
        return ui.div(
            ui.tags.h3(f"{city_data['city']} Weather"),
            ui.tags.p(f"Temperature: {city_data['temperature']}°C"),
            ui.tags.p(f"Humidity: {city_data['humidity']}%"),
            ui.tags.p(f"Wind Speed: {city_data['wind_speed']} km/h"),
            ui.tags.p(f"Precipitation: {city_data['precipitation']} mm"),
            ui.tags.p(f"Description: {city_data['description']}")
        )

    @render_widget
    def weather_metrics_plot():
        city_data = selected_city_data().iloc[0]
        metrics = {
            "Temperature": city_data["temperature"],
            "Humidity": city_data["humidity"],
            "Wind Speed": city_data["wind_speed"],
            "Precipitation": city_data["precipitation"]
        }
        
        fig = px.bar(
            x=list(metrics.keys()), 
            y=list(metrics.values()), 
            title=f"Weather Metrics for {city_data['city']}"
        )
        return fig

    @render.data_frame
    def weather_alerts():
        alerts_df = global_weather_df[global_weather_df["alert_level"] == "High"]
        
        if not input.show_alerts():
            return render.DataGrid(pd.DataFrame())
        
        return render.DataGrid(
            alerts_df[["city", "temperature", "alert_level", "description"]],
            selection_mode="rows"
        )

# Create and run the app
app = App(app_ui, server)