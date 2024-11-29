import random
from datetime import datetime

import pandas as pd
from shiny import App, render, ui, reactive, req

# Generate some sample data
employees = ["John Doe", "Jane Smith", "Bob Johnson", "Sarah Lee", "Tom Wilson"]
departments = ["Sales", "Marketing", "IT", "HR", "Finance"]
performance_ratings = [
    "Exceeds Expectations",
    "Meets Expectations",
    "Needs Improvement",
]

employee_data = [
    (
        emp,
        dep,
        random.choice(performance_ratings),
        random.randint(1, 5),
        datetime(2023, random.randint(1, 12), random.randint(1, 28)).date(),
    )
    for emp in employees
    for dep in departments
]

df = pd.DataFrame(
    employee_data,
    columns=[
        "Employee",
        "Department",
        "Performance Rating",
        "Years",
        "Last Review Date",
    ],
)

app_ui = ui.page_fluid(
    ui.card(
        ui.card_header("Employee Performance Evaluation"),
        ui.layout_column_wrap(
            ui.value_box(
                "Total Employees",
                len(employees),
                showcase=ui.HTML(
                    '<i class="bi bi-people-fill" style="font-size: 2rem;"></i>'
                ),
                theme="bg-gradient-primary",
            ),
            ui.value_box(
                "Exceeds Expectations",
                len(df[df["Performance Rating"] == "Exceeds Expectations"]),
                showcase=ui.HTML(
                    '<i class="bi bi-star-fill" style="font-size: 2rem;"></i>'
                ),
                theme="bg-gradient-success",
            ),
            ui.value_box(
                "Needs Improvement",
                len(df[df["Performance Rating"] == "Needs Improvement"]),
                showcase=ui.HTML(
                    '<i class="bi bi-exclamation-triangle-fill" style="font-size: 2rem;"></i>'
                ),
                theme="bg-gradient-danger",
            ),
            width=1 / 3,
        ),
    ),
    ui.card(
        ui.card_header("Filters"),
        ui.layout_column_wrap(
            ui.input_select("department_filter", "Department", ["All"] + departments),
            ui.input_select(
                "rating_filter", "Performance Rating", ["All"] + performance_ratings
            ),
            ui.input_slider("years_filter", "Years of Service", 1, 10, value=(1, 10)),
            width=1 / 3,
        ),
    ),
    ui.card(
        ui.card_header("Employee Data"),
        ui.output_data_frame("employee_table"),
    ),
)


def server(input, output, session):
    # Reactive data filtering
    @reactive.calc
    def filtered_data():
        df_filtered = df.copy()

        if input.department_filter() != "All":
            df_filtered = df_filtered[
                df_filtered["Department"] == input.department_filter()
            ]

        if input.rating_filter() != "All":
            df_filtered = df_filtered[
                df_filtered["Performance Rating"] == input.rating_filter()
            ]

        df_filtered = df_filtered[
            (df_filtered["Years"] >= input.years_filter()[0])
            & (df_filtered["Years"] <= input.years_filter()[1])
        ]

        return df_filtered

    @render.data_frame
    def employee_table():
        return render.DataGrid(
            filtered_data(),
            editable=True,
            filters=True,
            summary=True,
        )

    @employee_table.set_patch_fn
    def _(patch):
        row_index, col_index = patch["row_index"], patch["column_index"]
        column_name = df.columns[col_index]
        new_value = patch["value"]

        # Validate input based on column type
        if column_name == "Performance Rating":
            req(new_value in performance_ratings)
        elif column_name == "Years":
            req(isinstance(new_value, (int, float)) and 1 <= float(new_value) <= 10)
        elif column_name == "Last Review Date":
            try:
                datetime.strptime(new_value, "%Y-%m-%d")
            except ValueError:
                req(False, "Invalid date format. Use YYYY-MM-DD")

        df.iat[row_index, col_index] = new_value
        return new_value


app = App(app_ui, server)
