import time
import random
import numpy as np
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Busy Indicators Options Demo", fillable=True)

# Add Font Awesome CSS for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">'
    )
)


# Synthetic data generation function
def generate_random_data(n):
    """Generate random data for visualization."""
    return np.random.randn(n)


# Main app layout
with ui.layout_sidebar():
    with ui.sidebar():
        # Spinner Type Selection
        ui.input_select(
            "spinner_type",
            "Spinner Type",
            [
                "bars",
                "bars2",
                "bars3",
                "circles",
                "circles2",
                "circles3",
                "grid",
                "pulse",
                "dots",
            ],
            selected="bars",  # Add a default selection
        )

        # Spinner Color Selection
        ui.input_select(
            "spinner_color",
            "Spinner Color",
            [
                "primary",
                "secondary",
                "success",
                "danger",
                "warning",
                "info",
                "light",
                "dark",
                "#FF0000",
                "#00FF00",
            ],
            selected="primary",  # Add a default selection
        )

        # Spinner Size
        ui.input_text("spinner_size", "Spinner Size", value="50px")

        # Spinner Delay
        ui.input_text("spinner_delay", "Spinner Delay (seconds)", value="0.5")

        # Fade Opacity
        ui.input_slider(
            "fade_opacity", "Fade Opacity", min=0, max=1, value=0.5, step=0.1
        )

        # Pulse Options
        ui.input_text("pulse_height", "Pulse Height", value="5px")
        ui.input_text("pulse_speed", "Pulse Speed", value="1s")

        # Action Button to Trigger Long-Running Task
        ui.input_task_button("compute", "Compute Data")

    # Apply Busy Indicators Options AFTER the sidebar
    ui.busy_indicators.options(
        spinner_type="bars",  # Use a static value initially
        spinner_color="primary",  # Use a static value initially
        spinner_size="50px",
        spinner_delay=0.5,
        fade_opacity=0.5,
        pulse_height="5px",
        pulse_speed="1s",
    )

    # Card to display results
    with ui.card(full_screen=True):

        @render.plot
        @reactive.event(input.compute)
        def result_plot():
            # Simulate a long-running computation
            time.sleep(3)

            # Generate random data
            data = generate_random_data(1000)

            # Create plot
            plt.figure(figsize=(10, 6))
            plt.hist(data, bins=30, edgecolor="black")
            plt.title(f"Random Data Histogram (n={len(data)})")
            plt.xlabel("Value")
            plt.ylabel("Frequency")

            return plt.gcf()

    # Display current configuration
    with ui.card():

        @render.text
        def config_display():
            return f"""
            Current Configuration:
            - Spinner Type: {input.spinner_type()}
            - Spinner Color: {input.spinner_color()}
            - Spinner Size: {input.spinner_size()}
            - Spinner Delay: {input.spinner_delay()} seconds
            - Fade Opacity: {input.fade_opacity()}
            - Pulse Height: {input.pulse_height()}
            - Pulse Speed: {input.pulse_speed()}
            """

    # Reactive effect to update busy indicators dynamically
    @reactive.effect
    def _update_busy_indicators():
        ui.busy_indicators.options(
            spinner_type=input.spinner_type(),
            spinner_color=input.spinner_color(),
            spinner_size=input.spinner_size(),
            spinner_delay=float(input.spinner_delay()),
            fade_opacity=input.fade_opacity(),
            pulse_height=input.pulse_height(),
            pulse_speed=input.pulse_speed(),
        )
