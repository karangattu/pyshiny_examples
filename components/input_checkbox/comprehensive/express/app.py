import random
import pandas as pd
import numpy as np

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
data = pd.DataFrame(
    {
        "name": [f"Item {i}" for i in range(1, 11)],
        "value": np.random.randint(1, 100, 10),
        "category": random.choices(["A", "B", "C"], k=10),
    }
)

# Page Options
ui.page_opts(title="Comprehensive Checkbox Input Demo")

# Sidebar with various checkbox configurations
with ui.sidebar():
    # Basic checkbox with default parameters
    ui.input_checkbox("basic_checkbox", "Basic Checkbox")

    # Checkbox with initial value set to True
    ui.input_checkbox("initial_true_checkbox", "Initially Checked Checkbox", value=True)

    # Checkbox with custom width
    ui.input_checkbox("width_checkbox", "Checkbox with Custom Width", width="200px")

    # Checkbox with HTML label
    ui.input_checkbox(
        "html_label_checkbox",
        ui.tags.span("Checkbox with ", ui.tags.strong("HTML Label")),
    )

# Main content area
with ui.layout_columns():
    # Card to display checkbox states
    with ui.card():
        ui.card_header("Checkbox States")

        @render.text
        def checkbox_states():
            states = [
                f"Basic Checkbox: {input.basic_checkbox()}",
                f"Initially True Checkbox: {input.initial_true_checkbox()}",
                f"Width Checkbox: {input.width_checkbox()}",
                f"HTML Label Checkbox: {input.html_label_checkbox()}",
            ]
            return "\n".join(states)

    # Card to demonstrate reactive effects
    with ui.card():
        ui.card_header("Reactive Effects")

        @reactive.effect
        def _():
            # Example of using checkbox to filter data
            filtered_data = (
                data[data["category"] == "A"] if input.basic_checkbox() else data
            )

            @render.data_frame
            def filtered_table():
                return filtered_data


# Additional interactive elements to showcase checkbox interactions
with ui.layout_columns():
    # Card showing checkbox interaction with other inputs
    with ui.card():
        ui.card_header("Checkbox Interactions")

        # Slider that is enabled/disabled by checkbox
        ui.input_checkbox("enable_slider", "Enable Slider")

        @render.ui
        def dynamic_slider():
            if input.enable_slider():
                return ui.input_slider(
                    "interactive_slider", "Interactive Slider", min=0, max=100, value=50
                )
            else:
                return ui.p("Slider is disabled")

    # Card showing checkbox as a toggle for content
    with ui.card():
        ui.card_header("Conditional Content")

        ui.input_checkbox("show_content", "Show/Hide Content")

        @render.ui
        def conditional_content():
            if input.show_content():
                return ui.tags.div(
                    ui.h4("Revealed Content"),
                    ui.p("This content is shown when the checkbox is checked."),
                )
            else:
                return ui.tags.div()


# Notification when checkbox states change
@reactive.effect
def _():
    if input.basic_checkbox() or input.initial_true_checkbox():
        ui.notification_show(
            "A checkbox state has changed!", duration=3, type="message"
        )
