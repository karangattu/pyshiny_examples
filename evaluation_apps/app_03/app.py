from shiny import App, render, ui
import numpy as np
import matplotlib.pyplot as plt

app_ui = ui.page_fluid(
    ui.input_slider("bins", "Number of bins", 1, 50, 10),
    ui.output_plot("hist"),
)


def server(input, output, session):
    @render.plot
    def hist():
        np.random.seed(42)
        x = np.random.randn(500)
        plt.hist(x, bins=input.bins(), color="#007bff", alpha=0.7)
        plt.title("Histogram of Random Data")
        plt.xlabel("Value")
        plt.ylabel("Frequency")


app = App(app_ui, server)
