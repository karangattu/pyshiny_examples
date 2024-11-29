import numpy as np
import pandas as pd
from shiny import App, Inputs, Outputs, Session, render, ui

# Generate some sample data
np.random.seed(42)
data = pd.DataFrame(
    {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Age": np.random.randint(20, 61, size=5),
        "Gender": ["Female", "Male", "Male", "Male", "Female"],
        "Income": np.random.randint(30000, 100001, size=5),
    }
)

app_ui = ui.page_fluid(
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Filter Dataset"),
            ui.input_text("name", "Name", placeholder="Enter name"),
            ui.input_numeric("min_age", "Minimum Age", min=0, max=100, value=0),
            ui.input_numeric("max_age", "Maximum Age", min=0, max=100, value=100),
            ui.input_checkbox_group("gender", "Gender", ["Male", "Female"]),
            ui.input_numeric(
                "min_income", "Minimum Income", min=0, max=100000, value=0
            ),
            ui.input_numeric(
                "max_income", "Maximum Income", min=0, max=100000, value=100000
            ),
            ui.output_data_frame("filtered_data"),
            width=1 / 2,
        )
    )
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.data_frame
    def filtered_data():
        filtered = data
        if input.name():
            filtered = filtered[filtered["Name"].str.contains(input.name(), case=False)]
        filtered = filtered[
            (filtered["Age"] >= input.min_age()) & (filtered["Age"] <= input.max_age())
        ]
        if input.gender():
            filtered = filtered[filtered["Gender"].isin(input.gender())]
        filtered = filtered[
            (filtered["Income"] >= input.min_income())
            & (filtered["Income"] <= input.max_income())
        ]
        return filtered


app = App(app_ui, server)
