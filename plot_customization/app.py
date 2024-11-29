import matplotlib.pyplot as plt
import numpy as np
from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Generate some sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

app_ui = ui.page_fluid(
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Plot Customization"),
            ui.input_text("color1", "Color 1"),
            ui.input_text("color2", "Color 2"),
            ui.input_text("label1", "Label 1", "Sin(x)"),
            ui.input_text("label2", "Label 2", "Cos(x)"),
            width=1 / 2,
        ),
        ui.card(
            ui.output_plot("plot"),
            full_screen=True,
        ),
    )
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.plot
    def plot():
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(x, y1, color=input.color1(), label=input.label1())
        ax.plot(x, y2, color=input.color2(), label=input.label2())
        ax.legend()
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Sine and Cosine Waves")
        return fig


app = App(app_ui, server)
