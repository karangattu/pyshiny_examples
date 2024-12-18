import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
sales_data = pd.DataFrame(
    {
        "Region": ["North", "South", "East", "West", "Central"],
        "Sales": np.random.randint(50000, 200000, 5),
        "Profit_Margin": np.random.uniform(0.1, 0.3, 5),
    }
)

# Set page options
ui.page_opts(title="Sales Dashboard", fillable=True)

# Create a sidebar for user interaction
with ui.sidebar():
    ui.input_select(
        "selected_region", "Select Region", choices=sales_data["Region"].tolist()
    )

# Layout with multiple cards
with ui.layout_column_wrap(width=1 / 2):
    # Sales Card
    with ui.card(full_screen=True):
        ui.card_header("Total Sales by Region")

        @render.plot
        def sales_plot():
            plt.figure(figsize=(8, 6))
            plt.bar(sales_data["Region"], sales_data["Sales"])
            plt.title("Sales Across Regions")
            plt.xlabel("Region")
            plt.ylabel("Sales ($)")
            plt.xticks(rotation=45)
            return plt.gcf()

    # Profit Margin Card
    with ui.card(full_screen=True):
        ui.card_header("Profit Margins")

        @render.plot
        def profit_plot():
            plt.figure(figsize=(8, 6))
            plt.pie(
                sales_data["Profit_Margin"],
                labels=sales_data["Region"],
                autopct="%1.1f%%",
            )
            plt.title("Profit Margins by Region")
            return plt.gcf()


# Detailed Region Information Card
with ui.card(full_screen=True):
    ui.card_header("Region Details")

    @render.table
    def region_details():
        selected = input.selected_region()
        return sales_data[sales_data["Region"] == selected]
