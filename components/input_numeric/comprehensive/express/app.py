import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
data = pd.DataFrame(
    {
        "category": ["A", "B", "C", "D", "E"],
        "value": np.random.randint(10, 100, 5),
        "weight": np.random.uniform(0.5, 2.5, 5),
    }
)

# Page setup
ui.page_opts(title="Numeric Input Showcase", fillable=True)

# Sidebar with comprehensive numeric input configurations
with ui.sidebar():
    # Basic numeric input with min, max, and step
    ui.input_numeric(
        "basic_num",
        "Basic Numeric Input",
        value=50,  # Initial value
        min=0,  # Minimum allowed value
        max=100,  # Maximum allowed value
        step=5,  # Increment/decrement step
    )

    # Numeric input with custom width
    ui.input_numeric(
        "width_num",
        "Numeric Input with Width",
        value=25,
        min=0,
        max=50,
        width="200px",  # Custom CSS width
    )

    # Numeric input with floating point values
    ui.input_numeric(
        "float_num",
        "Floating Point Input",
        value=3.14,
        min=0,
        max=10,
        step=0.5,  # Floating point step
    )

# Main content area with outputs
with ui.layout_columns():
    # Display the current numeric input values
    @render.text
    def numeric_values():
        return f"""
        Basic Numeric: {input.basic_num()}
        Width Numeric: {input.width_num()}
        Float Numeric: {input.float_num()}
        """

    # Bar plot showing data with numeric input affecting visualization
    @render.plot
    def dynamic_plot():
        # Use numeric inputs to modify plot
        multiplier = input.basic_num() / 50  # Normalize the input

        plt.figure(figsize=(8, 5))
        plt.bar(
            data["category"], data["value"] * multiplier, color="skyblue", alpha=0.7
        )
        plt.title(f"Dynamic Bar Plot (Multiplier: {multiplier:.2f})")
        plt.xlabel("Category")
        plt.ylabel("Scaled Value")
        plt.ylim(0, 200)  # Set a reasonable y-axis limit
        return plt.gcf()

    # Table showing how numeric inputs affect data
    @render.data_frame
    def modified_data():
        modified_df = data.copy()
        modified_df["scaled_value"] = modified_df["value"] * (input.basic_num() / 50)
        modified_df["weighted_value"] = modified_df["value"] * input.float_num()
        return modified_df
