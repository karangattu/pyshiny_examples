from shiny import reactive
from shiny.express import input, ui, render
import matplotlib.pyplot as plt
import numpy as np

# Page options and dark mode switch
ui.page_opts(title="Dark Mode Demo", fillable=True)
ui.input_dark_mode(id="dark_mode")

# Create some sample data
np.random.seed(123)
data = np.random.normal(100, 15, 1000)

# Layout with a card containing a plot
with ui.card():
    ui.card_header("Sample Distribution")
    ui.input_slider("bins", "Number of bins", min=10, max=100, value=30)

    @render.plot
    def histogram():
        fig, ax = plt.subplots()

        # Theme the plot based on dark mode state
        if input.dark_mode() == "dark":
            plt.style.use("dark_background")
            color = "white"
        else:
            plt.style.use("default")
            color = "black"

        # Create histogram
        ax.hist(data, bins=input.bins(), color="#447099", alpha=0.7)
        ax.set_title("Normal Distribution", color=color)
        ax.set_xlabel("Values", color=color)
        ax.set_ylabel("Frequency", color=color)

        # Set background color
        fig.patch.set_facecolor("none")
        ax.set_facecolor("none")

        return fig


# Add some descriptive text that demonstrates dark mode affects
with ui.card():
    ui.card_header("About")
    "This app demonstrates the use of dark mode in Shiny for Python."
    "Notice how the plot and text automatically adjust to dark/light mode."
    "Try clicking the dark mode toggle in the top-right corner!"
