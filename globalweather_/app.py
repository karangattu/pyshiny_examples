from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shiny import App, reactive, render, ui

# Generate synthetic weather data
def generate_weather_data():
    cities = [
        "New York", "London", "Tokyo", "Paris", "Sydney",
        "Mumbai", "Dubai", "Singapore", "Toronto", "Berlin"
    ]
    
    current_time = datetime.now()
    dates = [current_time + timedelta(hours=i) for i in range(24)]
    
    weather_data = []
    for city in cities:
        base_temp = np.random.randint(15, 30)
        base_humidity = np.random.randint(40, 80)
        base_wind = np.random.randint(5, 20)
        base_precip = np.random.randint(0, 30)
        
        for date in dates:
            temp_variation = np.random.uniform(-5, 5)
            humidity_variation = np.random.uniform(-10, 10)
            wind_variation = np.random.uniform(-3, 3)
            precip_variation = np.random.uniform(-5, 5)
            
            weather_data.append({
                'city': city,
                'datetime': date,
                'temperature': round(base_temp + temp_variation, 1),
                'humidity': round(base_humidity + humidity_variation, 1),
                'wind_speed': round(base_wind + wind_variation, 1),
                'precipitation': round(max(0, base_precip + precip_variation), 1),
                'condition': np.random.choice(['Sunny', 'Cloudy', 'Rainy', 'Stormy'])
            })
    
    return pd.DataFrame(weather_data)

# Create the UI
app_ui = ui.page_fluid(
    ui.panel_title("Global Weather Dashboard"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_selectize(
                "city", "Select City",
                choices=["New York", "London", "Tokyo", "Paris", "Sydney",
                        "Mumbai", "Dubai", "Singapore", "Toronto", "Berlin"]
            ),
            ui.input_checkbox_group(
                "metrics",
                "Select Metrics",
                choices=["Temperature", "Humidity", "Wind Speed", "Precipitation"],
                selected=["Temperature"]
            ),
            ui.hr(),
            ui.h4("Weather Alerts"),
            ui.input_numeric("temp_threshold", "Temperature Alert (°C)", value=30),
            ui.input_numeric("wind_threshold", "Wind Speed Alert (km/h)", value=25),
            ui.input_numeric("precip_threshold", "Precipitation Alert (mm)", value=50),
            width=250
        ),
        ui.layout_column_wrap(
            ui.value_box(
                "Current Temperature",
                ui.output_text("current_temp"),
                theme="primary",
            ),
            ui.value_box(
                "Current Humidity",
                ui.output_text("current_humidity"),
                theme="info",
            ),
            ui.value_box(
                "Current Wind Speed",
                ui.output_text("current_wind"),
                theme="success",
            ),
            ui.value_box(
                "Current Precipitation",
                ui.output_text("current_precip"),
                theme="warning",
            ),
        ),
        ui.card(
            ui.card_header("24-Hour Forecast"),
            ui.output_plot("forecast_plot"),
        ),
        ui.card(
            ui.card_header("Weather Alerts"),
            ui.output_ui("alerts"),
        ),
    )
)

def server(input, output, session):
    # Initialize weather data
    weather_df = reactive.Value(generate_weather_data())
    
    @reactive.effect
    def _():
        # Regenerate data every 5 minutes
        reactive.invalidate_later(5 * 60)
        weather_df.set(generate_weather_data())
    
    @reactive.calc
    def current_weather():
        df = weather_df.get()
        return df[df['city'] == input.city()].iloc[0]
    
    @render.text
    def current_temp():
        return f"{current_weather()['temperature']}°C"
    
    @render.text
    def current_humidity():
        return f"{current_weather()['humidity']}%"
    
    @render.text
    def current_wind():
        return f"{current_weather()['wind_speed']} km/h"
    
    @render.text
    def current_precip():
        return f"{current_weather()['precipitation']} mm"
    
    @render.plot
    def forecast_plot():
        df = weather_df.get()
        city_data = df[df['city'] == input.city()]
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        metrics = input.metrics()
        
        for metric in metrics:
            if metric == "Temperature":
                ax.plot(city_data['datetime'], city_data['temperature'], 
                       label='Temperature (°C)', color='red')
            elif metric == "Humidity":
                ax.plot(city_data['datetime'], city_data['humidity'], 
                       label='Humidity (%)', color='blue')
            elif metric == "Wind Speed":
                ax.plot(city_data['datetime'], city_data['wind_speed'], 
                       label='Wind Speed (km/h)', color='green')
            elif metric == "Precipitation":
                ax.plot(city_data['datetime'], city_data['precipitation'], 
                       label='Precipitation (mm)', color='purple')
        
        ax.set_xlabel('Time')
        ax.set_ylabel('Value')
        ax.set_title(f'24-Hour Forecast for {input.city()}')
        ax.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        return fig
    
    @render.ui
    def alerts():
        weather = current_weather()
        alerts = []
        
        if weather['temperature'] > input.temp_threshold():
            alerts.append(ui.p(
                ui.tags.i(class_="fa-solid fa-triangle-exclamation"), 
                f" High temperature alert: {weather['temperature']}°C",
                style="color: red;"
            ))
            
        if weather['wind_speed'] > input.wind_threshold():
            alerts.append(ui.p(
                ui.tags.i(class_="fa-solid fa-triangle-exclamation"),
                f" High wind alert: {weather['wind_speed']} km/h",
                style="color: orange;"
            ))
            
        if weather['precipitation'] > input.precip_threshold():
            alerts.append(ui.p(
                ui.tags.i(class_="fa-solid fa-triangle-exclamation"),
                f" Heavy precipitation alert: {weather['precipitation']} mm",
                style="color: blue;"
            ))
            
        if not alerts:
            alerts = [ui.p("No active weather alerts", style="color: green;")]
            
        return ui.div(
            ui.tags.head(
                ui.tags.link(
                    rel="stylesheet",
                    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                )
            ),
            *alerts
        )

app = App(app_ui, server)