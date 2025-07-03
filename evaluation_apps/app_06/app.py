from shiny import App, render, ui
import pandas as pd

app_ui = ui.page_fluid(
    ui.output_table("data"),
)

def server(input, output, session):
    @output
    @render.table
    def data():
        return pd.DataFrame({
            "ID": [1, 2, 3, 4],
            "Name": ["A", "B", "C", "D"],
            "Value": [10, 20, 30, 40]
        })

app = App(app_ui, server)
