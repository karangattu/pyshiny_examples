import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
sales_data = pd.DataFrame(
    {
        "Region": ["North", "South", "East", "West", "Central"],
        "Sales": np.random.randint(50000, 200000, 5),
        "Profit_Margin": np.random.uniform(0.05, 0.25, 5),
    }
)

# Page configuration
ui.page_opts(title="Sales Dashboard", fillable=True)

# Add dark mode toggle
ui.input_dark_mode(id="dark_mode")

# Layout with columns
with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Sales by Region")

        @render.plot
        def sales_plot():
            plt.figure(figsize=(8, 6))
            plt.bar(sales_data["Region"], sales_data["Sales"])
            plt.title("Regional Sales Performance")
            plt.xlabel("Region")
            plt.ylabel("Sales ($)")
            plt.xticks(rotation=45)
            return plt.gcf()

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

    with ui.card(full_screen=True):
        ui.card_header("Sales Data Table")

        @render.data_frame
        def sales_table():
            return sales_data
