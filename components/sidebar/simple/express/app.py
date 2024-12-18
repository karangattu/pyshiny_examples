import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
data = pd.DataFrame(
    {
        "Category": ["A", "B", "C", "D", "E"],
        "Value": np.random.randint(10, 100, 5),
        "Score": np.random.uniform(0, 10, 5),
    }
)

# Set up the app with a sidebar
ui.page_opts(title="Sidebar Demo")

# Create a sidebar
with ui.sidebar():
    # Sidebar inputs
    ui.input_select("category", "Select Category", choices=data["Category"].tolist())

    ui.input_slider("value_range", "Value Range", min=0, max=100, value=[10, 90])

    ui.input_checkbox_group(
        "plot_type", "Plot Type", choices=["Bar", "Scatter"], selected=["Bar"]
    )

# Main content area
with ui.layout_columns():

    @render.data_frame
    def category_table():
        # Filter data based on sidebar inputs
        filtered_data = data[
            (data["Value"].between(input.value_range()[0], input.value_range()[1]))
            & (data["Category"] == input.category())
        ]
        return filtered_data

    @render.plot
    def category_plot():
        # Create plot based on sidebar inputs
        filtered_data = data[
            (data["Value"].between(input.value_range()[0], input.value_range()[1]))
            & (data["Category"] == input.category())
        ]

        plt.figure(figsize=(8, 6))

        if "Bar" in input.plot_type():
            plt.bar(filtered_data["Category"], filtered_data["Value"])
            plt.title("Bar Plot of Selected Category")
            plt.ylabel("Value")

        if "Scatter" in input.plot_type():
            plt.scatter(filtered_data["Category"], filtered_data["Score"], color="red")
            plt.title("Scatter Plot of Selected Category")
            plt.ylabel("Score")

        plt.xlabel("Category")
        return plt.gcf()
