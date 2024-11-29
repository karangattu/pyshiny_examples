import matplotlib.pyplot as plt
import numpy as np
from shiny import App, Inputs, Outputs, Session, render, ui

# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

app_ui = ui.page_fluid(
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Plot Color Settings"),
            ui.input_text(
                "line_color",
                "Line Color",
                "#0072B2",
            ),
            ui.input_text(
                "bg_color",
                "Background Color",
                "#EEEEEE",
            ),
            width=4,
        ),
        ui.card(
            ui.card_header("Plot"),
            ui.output_plot("plot"),
            width=8,
        ),
    )
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.plot
    def plot():
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(x, y, color=input.line_color())
        ax.set_facecolor(input.bg_color())
        ax.set_title("Sine Wave")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        return fig


app = App(app_ui, server)
