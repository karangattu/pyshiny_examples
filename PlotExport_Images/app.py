import random
import asyncio
import io

import matplotlib.pyplot as plt
from shiny import App, Inputs, Outputs, Session, render, ui, reactive

app_ui = ui.page_fluid(
    ui.input_slider("n", "Number of points", min=10, max=100, value=50),
    ui.download_button("save", "Save Plot"),
    ui.output_plot("plot"),
)


def server(input, output, session):
    @render.plot
    def plot():
        x = [random.uniform(0, 10) for _ in range(input.n())]
        y = [random.uniform(0, 10) for _ in range(input.n())]
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.scatter(x, y)
        ax.set_title(f"Random Scatter Plot ({input.n()} points)")
        return fig

    @render.download(filename="plot.png")
    @reactive.event(input.save)
    async def save():
        await asyncio.sleep(0.1)
        # Recreate the plot
        x = [random.uniform(0, 10) for _ in range(input.n())]
        y = [random.uniform(0, 10) for _ in range(input.n())]
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.scatter(x, y)
        ax.set_title(f"Random Scatter Plot ({input.n()} points)")

        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        buf.seek(0)
        plt.close(fig)  # Clean up the figure
        yield buf


app = App(app_ui, server)
