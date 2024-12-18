from shiny import ui
from shiny.express import input, render, ui

# First, install the required package
# You can do this via terminal before running the script:
# pip install libsass

# Create a custom theme
my_theme = (
    ui.Theme("shiny")
    .add_defaults(
        bslib_dashboard_design=True,  # Note: changed from dashboard_design to bslib_dashboard_design
    )
    .add_mixins(
        headings_color="$success",
        select_color_text="$orange",
    )
    .add_rules(
        """
        em { color: $warning; }
        .sidebar-title { color: $danger; }
        """
    )
)

# Set page options with the custom theme
ui.page_opts(
    title="Theme Demonstration",
    theme=my_theme,
    fillable=True,  # Added to ensure proper layout
)

# Generate synthetic data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create a synthetic dataset
np.random.seed(42)
data = pd.DataFrame(
    {
        "Category": ["A", "B", "C", "D", "E"],
        "Value": np.random.randint(50, 500, 5),
        "Percentage": np.random.uniform(0.1, 0.9, 5),
    }
)

# Sidebar with inputs
with ui.sidebar(title="Theme Controls"):
    ui.input_select(
        "color_scheme",
        "Select Color Scheme",
        choices=["Default", "Monochrome", "Vibrant"],
    )
    ui.input_slider("data_range", "Data Range", min=0, max=500, value=(100, 400))

# Main content area
with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Data Overview")

        @render.data_frame
        def data_table():
            filtered_data = data[
                (data["Value"] >= input.data_range()[0])
                & (data["Value"] <= input.data_range()[1])
            ]
            return filtered_data

    with ui.card(full_screen=True):
        ui.card_header("Visualization")

        @render.plot
        def category_plot():
            filtered_data = data[
                (data["Value"] >= input.data_range()[0])
                & (data["Value"] <= input.data_range()[1])
            ]

            plt.figure(figsize=(8, 6))
            plt.bar(filtered_data["Category"], filtered_data["Value"], color="orange")
            plt.title("Category Values", fontsize=15)
            plt.xlabel("Categories", fontsize=12)
            plt.ylabel("Values", fontsize=12)
            return plt.gcf()


# Add some explanatory text with themed elements
ui.markdown(
    """
    ### Theme Demonstration
    
    This app showcases *dynamic theming* using Shiny for Python. 
    
    **Key Features:**
    - Custom color schemes
    - Interactive data filtering
    - Responsive design
"""
)
