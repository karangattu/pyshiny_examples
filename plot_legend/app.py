import matplotlib.pyplot as plt
import numpy as np
from shiny import App, Inputs, Outputs, Session, render, ui

# Generate some sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

app_ui = ui.page_fluid(
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Plot with Legend"),
            ui.output_plot("plot"),
            ui.card_footer(
                ui.tags.div(
                    ui.tags.span("Sine", style="color:blue;"),
                    ui.tags.span("Cosine", style="color:red;"),
                    class_="d-flex justify-content-center",
                )
            ),
        ),
        width=1,
    )
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.plot
    def plot():
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(x, y1, color="blue", label="Sine")
        ax.plot(x, y2, color="red", label="Cosine")
        ax.legend()
        return fig


app = App(app_ui, server)
