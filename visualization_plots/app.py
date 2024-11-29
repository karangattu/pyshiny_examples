import matplotlib.pyplot as plt
import numpy as np
from shiny import App, Inputs, Outputs, Session, render, ui

app_ui = ui.page_fluid(
    ui.input_numeric("n", "Number of points", min=10, max=1000, value=100),
    ui.output_plot("plot"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.plot
    def plot():
        np.random.seed(42)
        x = np.random.uniform(0, 10, input.n())
        y = np.random.uniform(0, 10, input.n())
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(x, y)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_title(f"Scatter Plot with {input.n()} points")
        return fig


app = App(app_ui, server)
