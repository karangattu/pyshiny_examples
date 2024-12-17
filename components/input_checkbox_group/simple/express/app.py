import pandas as pd
import numpy as np

from shiny import reactive, req
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
fruits_data = pd.DataFrame(
    {
        "name": ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"],
        "price": np.random.uniform(1, 10, 7).round(2),
        "stock": np.random.randint(10, 100, 7),
        "origin": ["USA", "Mexico", "Chile", "Spain", "Brazil", "Italy", "France"],
    }
)

# Page options and title
ui.page_opts(title="Fruit Market Dashboard")

# Sidebar with checkbox group
with ui.sidebar():
    ui.input_checkbox_group(
        "selected_fruits",
        "Select Fruits",
        choices=fruits_data["name"].tolist(),
        selected=fruits_data["name"].tolist(),  # All fruits selected by default
    )

# Main content area with two outputs
with ui.layout_columns():
    # Fruit Prices Table
    @render.data_frame
    def fruit_prices():
        # Filter the dataframe based on selected fruits
        return fruits_data[fruits_data["name"].isin(input.selected_fruits())]

    # Summary Statistics
    @render.text
    def summary_stats():
        # Get selected fruits
        selected = input.selected_fruits()

        # Compute summary
        filtered_data = fruits_data[fruits_data["name"].isin(selected)]

        return f"""
        Selected Fruits Summary:
        - Total Fruits: {len(selected)}
        - Average Price: ${filtered_data['price'].mean():.2f}
        - Total Stock: {filtered_data['stock'].sum()}
        """
