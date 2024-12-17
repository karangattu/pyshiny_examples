import numpy as np
import pandas as pd
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

# Set page options
ui.page_opts(title="Simple Sidebar Layout Demo")

# Create sidebar layout
with ui.layout_sidebar():
    # Sidebar content
    with ui.sidebar():
        # Sidebar inputs
        ui.input_slider(
            "num_categories", "Number of Categories", min=1, max=len(data), value=3
        )

        ui.input_radio_buttons(
            "plot_type", "Plot Type", ["Bar", "Scatter"], selected="Bar"
        )

        ui.input_checkbox_group(
            "show_values",
            "Show Data",
            choices=data.columns.tolist(),
            selected=["Category", "Value"],
        )

    # Main panel content
    @render.plot
    def main_plot():
        # Filter data based on slider
        filtered_data = data.head(input.num_categories())

        plt.figure(figsize=(8, 6))

        if input.plot_type() == "Bar":
            plt.bar(filtered_data["Category"], filtered_data["Value"])
            plt.title("Bar Plot of Values")
            plt.xlabel("Category")
            plt.ylabel("Value")
        else:
            plt.scatter(
                filtered_data["Category"],
                filtered_data["Value"],
                s=filtered_data["Score"] * 50,
                alpha=0.6,
            )
            plt.title("Scatter Plot of Values")
            plt.xlabel("Category")
            plt.ylabel("Value")

        plt.tight_layout()
        return plt.gcf()

    # Data table render
    @render.data_frame
    def data_table():
        # Filter data based on slider and selected columns
        filtered_data = data.head(input.num_categories())
        return filtered_data[input.show_values()]
