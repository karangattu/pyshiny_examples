import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
data = pd.DataFrame(
    {"Category": ["A", "B", "C", "D", "E"], "Value": np.random.randint(10, 100, 5)}
)

# Page setup with dark mode input
ui.page_opts(title="Dark Mode Demo", fillable=True)

# Sidebar with dark mode toggle and other inputs
with ui.sidebar():
    ui.input_dark_mode(id="dark_mode")
    ui.input_slider("num_categories", "Number of Categories", min=1, max=5, value=3)

# Main content area with plot and data table
with ui.layout_columns():

    @render.plot
    def category_plot():
        # Adjust plot style based on dark mode
        plt.style.use("dark_background" if input.dark_mode() else "default")

        # Select subset of data based on slider
        subset = data.head(input.num_categories())

        plt.figure(figsize=(8, 6))
        plt.bar(subset["Category"], subset["Value"])
        plt.title("Category Values")
        plt.xlabel("Category")
        plt.ylabel("Value")
        return plt.gcf()

    @render.data_frame
    def category_table():
        # Select subset of data based on slider
        return data.head(input.num_categories())


# Optional: Add a text explanation about dark mode
ui.markdown(
    """
    ## Dark Mode Demo
    
    Use the dark mode toggle in the sidebar to switch between light and dark themes. 
    The plot and page will automatically adjust to the selected mode.
"""
)
