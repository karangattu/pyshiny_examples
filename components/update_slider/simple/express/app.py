import random
import numpy as np
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render

# Page options
ui.page_opts(title="Update Slider Demo")

# Sidebar layout
with ui.layout_sidebar():
    with ui.sidebar():
        # Initial slider for controlling the range of random numbers
        ui.input_slider(
            "range_max", "Maximum Range", min=10, max=100, value=50, step=10
        )

        # Button to trigger slider update
        ui.input_action_button("update_btn", "Update Slider Range")

    # Main panel with plot and text output
    @render.plot(alt="Random Number Distribution")
    def distribution_plot():
        # Generate random numbers based on the current max range
        np.random.seed(42)  # For reproducibility
        x = np.random.randint(0, input.range_max(), 100)

        # Create histogram
        fig, ax = plt.subplots()
        ax.hist(x, bins=10, edgecolor="black")
        ax.set_title(f"Distribution of Random Numbers (Max: {input.range_max()})")
        ax.set_xlabel("Value")
        ax.set_ylabel("Frequency")

        return fig

    # Reactive effect to update the slider when button is clicked
    @reactive.effect
    @reactive.event(input.update_btn)
    def _():
        # Dynamically update the slider range
        new_max = random.randint(50, 200)
        new_step = random.choice([5, 10, 15, 20])

        ui.update_slider(
            "range_max",
            min=10,  # Keep minimum at 10
            max=new_max,  # Randomly set new maximum
            value=new_max // 2,  # Set value to middle of new range
            step=new_step,  # Randomly set step size
        )
