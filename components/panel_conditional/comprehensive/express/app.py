from shiny import reactive, req
from shiny.express import input, ui, render
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Synthetic data generation
np.random.seed(42)
data = pd.DataFrame(
    {
        "category": ["A", "B", "C", "D", "E"],
        "numeric_value": np.random.randint(10, 100, 5),
        "text_value": ["Low", "Medium", "High", "Critical", "Extreme"],
    }
)

# Page setup
ui.page_opts(title="Panel Conditional Showcase", fillable=True)

# Sidebar with interactive controls
with ui.sidebar():
    ui.input_select(
        "category_select",
        "Select Category",
        choices=["All"] + list(data["category"].unique()),
    )

    ui.input_checkbox("show_numeric", "Show Numeric Panel")
    ui.input_checkbox("show_text", "Show Text Panel")

    ui.input_radio_buttons(
        "condition_type", "Condition Type", choices=["JavaScript", "Python"]
    )

    ui.input_slider("threshold", "Numeric Threshold", min=0, max=100, value=50)

# Main content area with conditional panels
with ui.layout_columns():
    # Conditional Panel 1: Category Selection
    with ui.panel_conditional("input.category_select !== 'All'"):

        @render.text
        def selected_category_text():
            return f"Selected Category: {input.category_select()}"

    # Conditional Panel 2: Numeric Value Panel
    with ui.panel_conditional("input.show_numeric"):

        @render.plot
        def numeric_plot():
            filtered_data = (
                data[data["category"] == input.category_select()]
                if input.category_select() != "All"
                else data
            )
            plt.figure(figsize=(8, 4))
            plt.bar(filtered_data["category"], filtered_data["numeric_value"])
            plt.title("Numeric Values by Category")
            plt.xlabel("Category")
            plt.ylabel("Value")
            return plt.gcf()

    # Conditional Panel 3: Text Value Panel
    with ui.panel_conditional("input.show_text"):

        @render.table
        def text_table():
            filtered_data = (
                data[data["category"] == input.category_select()]
                if input.category_select() != "All"
                else data
            )
            return filtered_data[["category", "text_value"]]

    # Conditional Panel 4: Dynamic Threshold (JavaScript)
    with ui.panel_conditional(
        "input.condition_type === 'JavaScript' && input.threshold > 50",
        class_="bg-light p-3",
    ):

        @render.text
        def threshold_text():
            return f"High Threshold (JS Condition): {input.threshold()}"

    # Conditional Panel 5: Python-based Condition
    with ui.panel_conditional(
        "input.condition_type === 'Python' && input.threshold > 50",
        class_="bg-info text-white p-3",
    ):

        @render.text
        def python_condition_text():
            return f"Python Condition Met: {input.threshold()}"


# Additional context and explanation
ui.markdown(
    """
### Panel Conditional Demonstration

This app showcases different ways to use `ui.panel_conditional`:
- Category selection panel
- Numeric value visualization
- Text value table
- JavaScript-based threshold condition
- Python-based threshold condition
"""
)
