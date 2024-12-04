import numpy as np
# Generate some sample data
import pandas as pd
from shiny import App, Inputs, Outputs, Session, reactive, render, ui

data = pd.DataFrame(
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
    ui.panel_title("Data Filtering and Sorting App"),
    ui.layout_column_wrap(
        ui.input_text("name_filter", "Filter by Name:", ""),
        ui.input_numeric("age_min", "Min Age:", 0, min=0, max=100),
        ui.input_numeric("age_max", "Max Age:", 100, min=0, max=100),
        ui.input_select("city_filter", "Filter by City:", list(data["City"].unique())),
        ui.input_select(
            "sort_by", "Sort by:", ["Name", "Age", "Salary"], selected="Name"
        ),
        ui.input_switch("sort_asc", "Sort Ascending", True),
        width=1 / 3,
    ),
    ui.output_data_frame("data_table"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @reactive.calc
    def filtered_data():
        df = data.copy()

        # Filter by name
        if input.name_filter():
            df = df[df["Name"].str.contains(input.name_filter(), case=False)]

        # Filter by age
        df = df[(df["Age"] >= input.age_min()) & (df["Age"] <= input.age_max())]

        # Filter by city
        if input.city_filter():
            df = df[df["City"] == input.city_filter()]

        # Sort
        sort_by = input.sort_by()
        sort_asc = input.sort_asc()
        df = df.sort_values(by=sort_by, ascending=sort_asc)

        return df

    @render.data_frame
    def data_table():
        return render.DataGrid(filtered_data(), selection_mode="none")


app = App(app_ui, server)
