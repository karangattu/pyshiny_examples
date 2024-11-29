import matplotlib.pyplot as plt
import numpy as np
from shiny import App, Inputs, Outputs, Session, render, ui

app_ui = ui.page_fluid(
    ui.input_slider("n", "Number of Bars", min=5, max=20, value=10, step=1),
    ui.output_plot("bar_chart"),
)


def server(input, output, session):
    @render.plot
    def bar_chart():
        # Generate some random data
        labels = [f"Category {i}" for i in range(1, input.n() + 1)]
        values = np.random.randint(10, 100, size=input.n())

        # Create the bar chart
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(labels, values)
        ax.set_title("Bar Chart Example")
        ax.set_xlabel("Category")
        ax.set_ylabel("Value")
        return fig


app = App(app_ui, server)
