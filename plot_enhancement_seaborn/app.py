import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from shiny import App, Inputs, Outputs, Session, render, ui

# Generate some sample data
x = np.random.normal(0, 1, 500)
y = np.random.normal(0, 1, 500)
data = {"x": x, "y": y}

app_ui = ui.page_fluid(
    ui.input_slider("n_bins", "Number of Bins", min=10, max=50, value=30),
    ui.output_plot("plot"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.plot
    def plot():
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.histplot(data=data, x="x", y="y", bins=int(input.n_bins()), ax=ax)
        ax.set_title("Bivariate Histogram")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        return fig


app = App(app_ui, server)
