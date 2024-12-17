from shiny import reactive
from shiny.express import input, ui, render

# Create synthetic data
data = {"dark_mode": False, "temperature": 72, "humidity": 45, "wind_speed": 10}

# Page options with title
ui.page_opts(title="Weather Dashboard")

# Sidebar with input switch
with ui.sidebar():
    ui.input_switch("dark_mode", "Dark Mode")
    ui.input_switch("show_wind", "Show Wind Speed", value=True)

# Main content area
with ui.layout_column_wrap(width=1 / 2):
    with ui.card():
        ui.card_header("Temperature")

        @render.text
        def temperature_display():
            temp = data["temperature"]
            mode = "warm" if temp > 75 else "cool"
            return f"Current temperature: {temp}°F ({mode})"

    with ui.card():
        ui.card_header("Humidity")

        @render.text
        def humidity_display():
            humidity = data["humidity"]
            status = "Comfortable" if 30 <= humidity <= 50 else "Extreme"
            return f"Humidity: {humidity}% ({status})"

    with ui.card():
        ui.card_header("Wind Speed")

        @render.text
        def wind_display():
            if input.show_wind():
                wind = data["wind_speed"]
                status = "Calm" if wind < 15 else "Windy"
                return f"Wind Speed: {wind} mph ({status})"
            else:
                return "Wind speed hidden"


# Optional: Add a reactive effect to demonstrate dark mode switch
@reactive.effect
def _():
    # You could use this to change the theme or apply custom styling
    dark_mode = input.dark_mode()
    print(f"Dark mode is {'on' if dark_mode else 'off'}")
