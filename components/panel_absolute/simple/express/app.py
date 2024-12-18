import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
df = pd.DataFrame(
    {
        "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
        "Population": [8_500_000, 4_000_000, 2_700_000, 2_300_000, 1_680_000],
        "Temperature": np.random.uniform(50, 90, 5),
        "Rainfall": np.random.uniform(10, 50, 5),
    }
)

# Create the Shiny app
ui.page_opts(title="Panel Absolute Demo", fillable=True)

# Main content
with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_select("city", "Select City", choices=df["City"].tolist())
        ui.input_checkbox("show_overlay", "Show Overlay", value=False)

    # Main plot area
    @render.plot
    def city_plot():
        city_data = df[df["City"] == input.city()]

        plt.figure(figsize=(10, 6))
        plt.bar(
            ["Temperature", "Rainfall"],
            [city_data["Temperature"].values[0], city_data["Rainfall"].values[0]],
        )
        plt.title(f"{input.city()} City Stats")
        plt.ylabel("Value")
        return plt.gcf()

    # Absolute panel for additional information
    with ui.panel_absolute(
        top="10px", right="10px", width="250px", class_="bg-light border p-3"
    ):

        @render.ui
        def city_info():
            if input.show_overlay():
                city_data = df[df["City"] == input.city()]
                return ui.div(
                    ui.h5(f"{input.city()} Details"),
                    ui.p(f"Population: {city_data['Population'].values[0]:,}"),
                    ui.p(f"Temperature: {city_data['Temperature'].values[0]:.1f}°F"),
                    ui.p(f"Rainfall: {city_data['Rainfall'].values[0]:.1f} inches"),
                )
            return ui.div()
