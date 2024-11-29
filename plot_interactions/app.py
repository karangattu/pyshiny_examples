import matplotlib.pyplot as plt
import numpy as np
from shiny import App, Inputs, Outputs, Session, render, ui

# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.2, 100)

app_ui = ui.page_fluid(
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Interactive Plot"),
            ui.output_plot(
                "plot",
                width="100%",
                height="500px",
                click=True,
                dblclick=True,
                hover=True,
            ),
        ),
        ui.card(
            ui.card_header("Plot Information"),
            ui.output_text_verbatim("plot_info"),
        ),
        width=1,
    )
)


def server(input, output, session):
    @render.plot
    def plot():
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(x, y)
        return fig

    @render.text
    def plot_info():
        if input.plot_click():
            return f"Clicked at: x={input.plot_click()['x']:.2f}, y={input.plot_click()['y']:.2f}"
        elif input.plot_dblclick():
            return f"Double-clicked at: x={input.plot_dblclick()['x']:.2f}, y={input.plot_dblclick()['y']:.2f}"
        elif input.plot_hover():
            return f"Hovered at: x={input.plot_hover()['x']:.2f}, y={input.plot_hover()['y']:.2f}"
        else:
            return "Hover, click, or double-click on the plot to see information."


app = App(app_ui, server)
