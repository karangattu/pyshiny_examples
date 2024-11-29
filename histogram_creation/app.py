import matplotlib.pyplot as plt
import numpy as np
from shiny import App, Inputs, Outputs, Session, render, ui

app_ui = ui.page_fluid(
    ui.input_slider("n", "Number of observations", min=10, max=1000, value=100),
    ui.output_plot("plot"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.plot
    def plot():
        np.random.seed(19680801)
        x = 100 + 15 * np.random.randn(int(input.n()))
        fig, ax = plt.subplots()
        ax.hist(x, bins=30, density=True)
        return fig


app = App(app_ui, server)
