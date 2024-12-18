import numpy as np
import time
from shiny import reactive
from shiny.express import input, ui, render
from matplotlib import pyplot as plt

# Set page options and add Font Awesome CSS for icons
ui.page_opts(title="Busy Indicators Demo")
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
    )
)

# Configure busy indicators
ui.busy_indicators.options(
    spinner_type="bars3",
    spinner_color="#AA00AA",
    spinner_size="2rem",
    fade_opacity=0.3,
)

# Create a layout with sidebar
with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_slider("n_points", "Number of Points", 1000, 100000, 5000)
        ui.input_slider("delay", "Artificial Delay (s)", 0, 5, 2, step=0.5)
        ui.input_action_button("generate", "Generate Plot", class_="btn-primary")

        ui.hr()
        ui.markdown(
            """
        ### About
        This app demonstrates the use of busy indicators in Shiny for Python.
        Notice the customized:
        * Loading spinner
        * Fade effect
        * Pulse animation
        """
        )

    # Main panel
    ui.h2("Random Data Visualization")

    @render.plot
    @reactive.event(input.generate)
    def plot():
        # Artificial delay to show the busy indicators
        time.sleep(input.delay())

        # Generate random data
        n = input.n_points()
        data = np.random.normal(0, 1, n)

        # Create the plot
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(data, bins=50, density=True, alpha=0.7)
        ax.set_title(f"Histogram of {n:,} Random Points")
        ax.set_xlabel("Value")
        ax.set_ylabel("Density")

        return fig
