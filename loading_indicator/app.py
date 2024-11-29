import random
import time

import pandas as pd
from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui

# Generate sample data
data = pd.DataFrame(
    {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Age": [25, 32, 41, 28, 35],
        "Score": [85, 92, 78, 90, 88],
    }
)

app_ui = ui.page_fluid(
    ui.input_action_button("load_data", "Load Data"),
    ui.output_table("data_table"),
    ui.output_ui("progress_bar"),
)


def server(input, output, session):
    data_loaded = reactive.Value(False)

    @reactive.effect
    @reactive.event(input.load_data)
    def load_data():
        with ui.Progress(min=0, max=100) as p:
            for i in range(100):
                p.set(i, message="Loading data...")
                time.sleep(0.05)
        data_loaded.set(True)

    @render.table
    def data_table():
        req(data_loaded())
        return data

    @render.ui
    def progress_bar():
        if not data_loaded():
            return ui.HTML(
                """
                <div class="progress">
                    <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%">
                        Loading...
                    </div>
                </div>
            """
            )
        else:
            return None


app = App(app_ui, server)
