import random

import pandas as pd
from shiny import App, Inputs, Outputs, Session, render, ui

# Generate some sample data
choices = ["Option A", "Option B", "Option C", "Option D", "Option E"]
data = {choice: random.randint(1, 100) for choice in choices}

app_ui = ui.page_fluid(
    ui.input_selectize("choices", "Select options", choices, multiple=True),
    ui.output_text_verbatim("selected_values"),
    ui.output_table("data_table"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.text
    def selected_values():
        return "Selected options: " + ", ".join(input.choices())

    @render.table
    def data_table():
        df = pd.DataFrame.from_dict(data, orient="index")
        df.columns = ["Value"]
        return df


app = App(app_ui, server)
