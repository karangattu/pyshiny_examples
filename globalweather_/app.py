import random
from datetime import datetime, timedelta
from typing import Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui

# Sample weather data
def generate_weather_data(location: str, days: int) -> pd.DataFrame:
    """Generate sample weather data for a given location and number of days."""
    dates = [datetime.now() + timedelta(days=i) for i in range(days)]
    temps = np.random.normal(loc=15, scale=5, size=days)
    humidity = np.random.uniform(low=40, high=90, size=days)
    wind_speed = np.random.uniform(low=5, high=20, size=days)
    precipitation = np.random.uniform(low=0, high=50, size=days)

    return pd.DataFrame({
        "date": dates,
        "location": location,
        "temperature": temps,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "precipitation": precipitation
    })

# Global weather data
weather_data = pd.concat([
    generate_weather_data("New York", 7),
    generate_weather_data("London", 7),
    generate_weather_data("Tokyo", 7),
    generate_weather_data("Sydney", 7)
])

app_ui = ui.page_fluid(
    ui.panel_title("Global Weather App"),
    ui.layout_column_wrap(
        ui.input_select("location", "Select Location", list(weather_data["location"].unique())),
        ui.input_date_range("date_range", "Select Date Range"),
        width=1 / 3,
    ),
    ui.layout_column_wrap(
        ui.value_box("Temperature", ui.output_text_verbatim("temperature"), theme="bg-gradient-orange-red"),
        ui.value_box("Humidity", ui.output_text_verbatim("humidity"), theme="bg-gradient-blue-purple"),
        ui.value_box("Wind Speed", ui.output_text_verbatim("wind_speed"), theme="bg-gradient-green-teal"),
        ui.value_box("Precipitation", ui.output_text_verbatim("precipitation"), theme="bg-gradient-yellow-orange"),
        width=1 / 2,
    ),
    ui.output_plot("weather_plot"),
    ui.output_text_verbatim("weather_alerts"),
)

def server(input: Inputs, output: Outputs, session: Session):
    @reactive.calc
    def filtered_weather():
        df = weather_data.copy()
        df = df[(df["location"] == input.location()) & (df["date"].between(*input.date_range()))]
        return df

    @render.text
    def temperature():
        df = filtered_weather()
        return f"{df['temperature'].mean():.2f}°C"

    @render.text
    def humidity():
        df = filtered_weather()
        return f"{df['humidity'].mean():.2f}%"

    @render.text
    def wind_speed():
        df = filtered_weather()
        return f"{df['wind_speed'].mean():.2f} m/s"

    @render.text
    def precipitation():
        df = filtered_weather()
        return f"{df['precipitation'].mean():.2f} mm"

    @render.plot
    def weather_plot():
        df = filtered_weather()
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(df["date"], df["temperature"], label="Temperature")
        ax.plot(df["date"], df["humidity"], label="Humidity")
        ax.plot(df["date"], df["wind_speed"], label="Wind Speed")
        ax.plot(df["date"], df["precipitation"], label="Precipitation")
        ax.set_xlabel("Date")
        ax.set_ylabel("Value")
        ax.set_title(f"Weather Forecast for {input.location()}")
        ax.legend()
        return fig

    @render.text
    def weather_alerts():
        df = filtered_weather()
        alerts = []
        if df["temperature"].max() > 35:
            alerts.append("High temperature alert!")
        if df["humidity"].max() > 80:
            alerts.append("High humidity alert!")
        if df["wind_speed"].max() > 15:
            alerts.append("High wind speed alert!")
        if df["precipitation"].max() > 30:
            alerts.append("High precipitation alert!")
        if not alerts:
            return "No weather alerts for the selected location and date range."
        else:
            return "\n".join(alerts)

app = App(app_ui, server)