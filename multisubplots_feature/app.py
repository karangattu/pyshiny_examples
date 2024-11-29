import matplotlib.pyplot as plt
import numpy as np
from shiny import App, Inputs, Outputs, Session, render, ui

# Generate some sample data
np.random.seed(42)
data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(2, 1, 100)
data3 = np.random.normal(-2, 1, 100)

app_ui = ui.page_fluid(
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Multi-Subplot Plot"),
            ui.output_plot("plot"),
            height="600px",
        ),
        width=1,
    )
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.plot
    def plot():
        fig, axes = plt.subplots(1, 3, figsize=(12, 4))

        axes[0].hist(data1, bins=20)
        axes[0].set_title("Subplot 1")

        axes[1].hist(data2, bins=20)
        axes[1].set_title("Subplot 2")

        axes[2].hist(data3, bins=20)
        axes[2].set_title("Subplot 3")

        fig.suptitle("Multi-Subplot Example")
        return fig


app = App(app_ui, server)
