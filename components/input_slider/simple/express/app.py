from shiny import reactive
from shiny.express import input, ui, render
import numpy as np

# Set page title
ui.page_opts(title="Simple Slider Demo")

# Create a slider input
ui.input_slider("num_points", "Number of points", min=10, max=100, value=50)


# Create a plot that responds to the slider
@render.plot
def histogram():
    # Generate random data based on slider value
    np.random.seed(123)
    data = np.random.normal(0, 1, input.num_points())

    # Create histogram
    fig, ax = plt.subplots()
    ax.hist(data, bins=20, density=True)
    ax.set_title(f"Histogram of {input.num_points()} Random Points")
    ax.set_xlabel("Value")
    ax.set_ylabel("Density")
    return fig


# Show the current slider value
@render.text
def slider_value():
    return f"You selected {input.num_points()} points"
