import pandas as pd
import numpy as np

from shiny import reactive
from shiny.express import input, render, ui

# Create synthetic dataset
np.random.seed(42)
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
data = pd.DataFrame(
    {
        "city": cities,
        "population": [8_400_000, 3_900_000, 2_700_000, 2_300_000, 1_600_000],
        "area_sq_miles": [302.6, 502.7, 227.6, 637.5, 517.9],
        "avg_income": [67_046, 59_833, 58_247, 52_338, 54_554],
    }
)

# App UI
ui.page_opts(title="City Information Explorer")

with ui.layout_sidebar():
    with ui.sidebar():
        # Using input_select with a dictionary of choices
        ui.input_select(
            "selected_city", "Choose a City:", {city: city for city in cities}
        )

        # Another input_select with optgroups
        ui.input_select(
            "data_view",
            "Select Data View:",
            {
                "Basic Info": {"population": "Population", "area": "Area"},
                "Economic Info": {"income": "Average Income"},
            },
        )

    # Render different outputs based on selections
    @render.text
    def city_details():
        city = input.selected_city()
        view = input.data_view()

        city_data = data[data["city"] == city]

        if view == "population":
            return f"{city} Population: {city_data['population'].values[0]:,}"
        elif view == "area":
            return f"{city} Area: {city_data['area_sq_miles'].values[0]} sq miles"
        elif view == "income":
            return f"{city} Average Income: ${city_data['avg_income'].values[0]:,}"
