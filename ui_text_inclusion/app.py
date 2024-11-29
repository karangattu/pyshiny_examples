import random

import pandas as pd
from shiny import App, Inputs, Outputs, Session, render, ui

# Made-up data
data = [
    {"name": "John Doe", "age": 35, "salary": 80000},
    {"name": "Jane Smith", "age": 28, "salary": 65000},
    {"name": "Michael Johnson", "age": 42, "salary": 95000},
    {"name": "Emily Davis", "age": 31, "salary": 72000},
    {"name": "David Wilson", "age": 39, "salary": 88000},
]

# convert list to df
data = pd.DataFrame(data)

app_ui = ui.page_fluid(
    ui.markdown(
        """
        # Shiny for Python App

        This is a sample Shiny for Python app that demonstrates the use of the Shiny for Python function reference documentation. The app displays a table of employee data, including their name, age, and salary.
        """
    ),
    ui.output_data_frame("employee_table"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.data_frame
    def employee_table():
        return render.DataGrid(data)


app = App(app_ui, server)
