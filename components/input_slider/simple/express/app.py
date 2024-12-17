import numpy as np
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, render, ui

# Set page title
ui.page_opts(title="Slider Demonstration")

# Create a sidebar with a slider input
with ui.sidebar():
    ui.input_slider("obs", "Number of observations:", min=0, max=1000, value=500)


# Render a plot based on the slider input
@render.plot(alt="A histogram of random data")
def distPlot():
    # Set a consistent random seed for reproducibility
    np.random.seed(19680801)

    # Generate random data based on slider input
    x = 100 + 15 * np.random.randn(input.obs())

    # Create the plot
    fig, ax = plt.subplots()
    ax.hist(x, bins=30, density=True, alpha=0.7, color="skyblue", edgecolor="black")
    ax.set_title(f"Histogram with {input.obs()} Observations")
    ax.set_xlabel("Value")
    ax.set_ylabel("Density")

    return fig
