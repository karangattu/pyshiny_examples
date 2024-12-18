from shiny import reactive
from shiny.express import input, ui, render
import random
import numpy as np
import pandas as pd

# Set page options
ui.page_opts(title="Update Numeric Input Demonstration")

# Create synthetic data
np.random.seed(42)
initial_value = 50
min_value = 0
max_value = 100

# Sidebar with controls
with ui.sidebar():
    # Original numeric input
    ui.input_numeric(
        "base_number",
        "Base Number",
        value=initial_value,
        min=min_value,
        max=max_value,
        step=1,
    )

    # Controls for updating numeric input
    ui.input_action_button("update_btn", "Update Numeric Input")

    # Additional controls to demonstrate different update scenarios
    ui.input_slider("label_length", "Label Length", min=5, max=30, value=10)

    ui.input_slider("step_size", "Step Size", min=0.1, max=10, value=1, step=0.1)

# Main content area
with ui.layout_columns():
    # Display current input details
    with ui.card():
        ui.card_header("Current Input Details")

        @render.text
        def input_details():
            return f"""
            Current Value: {input.base_number()}
            Current Min: {input.base_number.min}
            Current Max: {input.base_number.max}
            Current Step: {input.base_number.step}
            """

    # Demonstration of update scenarios
    with ui.card():
        ui.card_header("Update Scenarios")

        @reactive.effect
        @reactive.event(input.update_btn)
        def update_numeric_input():
            # Scenario 1: Update label
            label = "Updated Number " + "!" * int(input.label_length())

            # Scenario 2: Update value
            new_value = random.uniform(min_value, max_value)

            # Scenario 3: Update min and max
            new_min = max(0, new_value - 20)
            new_max = min(100, new_value + 20)

            # Scenario 4: Update step
            new_step = input.step_size()

            # Perform the update
            ui.update_numeric(
                "base_number",
                label=label,  # Update label
                value=new_value,  # Update value
                min=new_min,  # Update min
                max=new_max,  # Update max
                step=new_step,  # Update step
            )


# Optional: Add some explanatory text
ui.markdown(
    """
### How to Use
1. Click 'Update Numeric Input' to see dynamic updates
2. Adjust 'Label Length' and 'Step Size' to customize updates
"""
)
