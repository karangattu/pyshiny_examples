import numpy as np
import pandas as pd
from shiny import App, Inputs, Outputs, Session, render, ui

# Generate some sample data
df = pd.DataFrame(
    {
        "Name": [
            "John",
            "Jane",
            "Bob",
            "Alice",
            "Tom",
            "Emily",
            "Mike",
            "Sarah",
            "David",
            "Emily",
            "Kevin",
            "Lily",
            "Peter",
            "Olivia",
            "James",
            "Sophia",
            "Michael",
            "Isabella",
        ],
        "Age": [25, 32, 45, 28, 35, 41, 29, 27, 38, 42, 30, 26, 48, 24, 39, 31, 44, 36],
        "City": [
            "New York",
            "Los Angeles",
            "Chicago",
            "San Francisco",
            "Boston",
            "Seattle",
            "New York",
            "Los Angeles",
            "Chicago",
            "San Francisco",
            "Boston",
            "Seattle",
            "New York",
            "Los Angeles",
            "Chicago",
            "San Francisco",
            "Boston",
            "Seattle",
        ],
        "Salary": [
            50000,
            65000,
            75000,
            55000,
            60000,
            70000,
            52000,
            68000,
            78000,
            58000,
            62000,
            72000,
            54000,
            70000,
            80000,
            60000,
            64000,
            74000,
        ],
    }
)

app_ui = ui.page_fluid(
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Filter Options"),
            ui.input_text("name_filter", "Name Filter"),
            ui.input_numeric("age_min", "Minimum Age", min=0, max=100, value=0),
            ui.input_numeric("age_max", "Maximum Age", min=0, max=100, value=100),
            ui.input_select(
                "city_filter", "City Filter", ["All"] + list(df["City"].unique())
            ),
            ui.input_numeric(
                "salary_min", "Minimum Salary", min=0, max=100000, value=0
            ),
            ui.input_numeric(
                "salary_max", "Maximum Salary", min=0, max=100000, value=100000
            ),
            width=1 / 3,
        ),
        ui.card(
            ui.card_header("Filtered Data"),
            ui.output_data_frame("filtered_data"),
            width=2 / 3,
        ),
    )
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.data_frame
    def filtered_data():
        name_filter = input.name_filter()
        age_min = input.age_min()
        age_max = input.age_max()
        city_filter = input.city_filter()
        salary_min = input.salary_min()
        salary_max = input.salary_max()

        filtered_df = df.copy()

        if name_filter:
            filtered_df = filtered_df[
                filtered_df["Name"].str.contains(name_filter, case=False)
            ]
        if age_min is not None:
            filtered_df = filtered_df[filtered_df["Age"] >= age_min]
        if age_max is not None:
            filtered_df = filtered_df[filtered_df["Age"] <= age_max]
        if city_filter != "All":
            filtered_df = filtered_df[filtered_df["City"] == city_filter]
        if salary_min is not None:
            filtered_df = filtered_df[filtered_df["Salary"] >= salary_min]
        if salary_max is not None:
            filtered_df = filtered_df[filtered_df["Salary"] <= salary_max]

        return filtered_df


app = App(app_ui, server)
