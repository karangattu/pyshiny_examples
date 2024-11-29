import random

import pandas as pd
from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Generate sample data
data = pd.DataFrame(
    {
        "name": [
            "John Doe",
            "Jane Smith",
            "Michael Johnson",
            "Emily Brown",
            "David Lee",
        ],
        "age": [35, 28, 42, 31, 39],
        "gender": ["Male", "Female", "Male", "Female", "Male"],
        "salary": [80000, 65000, 95000, 72000, 88000],
    }
)

app_ui = ui.page_fluid(
    ui.input_radio_buttons("gender", "Filter by Gender:", ["All", "Male", "Female"]),
    ui.output_table("data_table"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.table
    def data_table():
        filtered_data = data
        if input.gender() != "All":
            filtered_data = filtered_data[filtered_data["gender"] == input.gender()]
        return filtered_data


app = App(app_ui, server)
