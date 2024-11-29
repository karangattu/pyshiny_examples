import numpy as np
import pandas as pd
from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Generate some sample data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 32, 41, 28, 35],
    "Gender": ["Female", "Male", "Male", "Male", "Female"],
    "Salary": [50000, 65000, 75000, 55000, 60000],
}
df = pd.DataFrame(data)

app_ui = ui.page_fluid(
    ui.row(
        ui.column(
            4,
            ui.card(
                ui.card_header("Filter Options"),
                ui.input_text("name_filter", "Name Filter"),
                ui.input_slider("age_min", "Minimum Age", min=18, max=65, value=18),
                ui.input_slider("age_max", "Maximum Age", min=18, max=65, value=65),
                ui.input_checkbox_group(
                    "gender_filter", "Gender Filter", ["Male", "Female"]
                ),
                ui.input_numeric(
                    "salary_min", "Minimum Salary", min=0, max=100000, value=0
                ),
                ui.input_numeric(
                    "salary_max", "Maximum Salary", min=0, max=100000, value=100000
                ),
            ),
        ),
        ui.column(
            8,
            ui.card(
                ui.card_header("Filtered Data"), ui.output_data_frame("filtered_data")
            ),
        ),
    )
)


def server(input: Inputs, output: Outputs, session: Session):
    @reactive.calc
    def filtered_df():
        filtered = df.copy()

        if input.name_filter():
            filtered = filtered[
                filtered["Name"].str.contains(input.name_filter(), case=False)
            ]

        filtered = filtered[
            (filtered["Age"] >= input.age_min()) & (filtered["Age"] <= input.age_max())
        ]

        if input.gender_filter():
            filtered = filtered[filtered["Gender"].isin(input.gender_filter())]

        filtered = filtered[
            (filtered["Salary"] >= input.salary_min())
            & (filtered["Salary"] <= input.salary_max())
        ]

        return filtered

    @render.data_frame
    def filtered_data():
        return filtered_df()


app = App(app_ui, server)
