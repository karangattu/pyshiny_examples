import random
from datetime import datetime, timedelta

import pandas as pd
from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Generate sample data
inspection_data = pd.DataFrame(
    {
        "Establishment": [
            "Acme Foods",
            "Tasty Treats",
            "Fresh Mart",
            "Delicious Deli",
            "Healthy Eats",
        ],
        "Inspection Date": [
            datetime.now() - timedelta(days=random.randint(1, 90)) for _ in range(5)
        ],
        "Inspection Score": [random.randint(70, 100) for _ in range(5)],
        "Violation": [random.choice(["None", "Minor", "Major"]) for _ in range(5)],
        "Status": [random.choice(["Passed", "Failed"]) for _ in range(5)],
    }
)


app_ui = ui.page_fluid(
    ui.panel_title("Food Safety and Inspection App"),
    ui.layout_column_wrap(
        ui.value_box(
            "Total Inspections",
            str(len(inspection_data)),
            theme="bg-gradient-blue-cyan",
            showcase=ui.HTML(
                '<i class="bi bi-clipboard-check" style="font-size: 2rem;"></i>'
            ),
            width="25%",
        ),
        ui.value_box(
            "Passed Inspections",
            str(len(inspection_data[inspection_data["Status"] == "Passed"])),
            theme="bg-gradient-green-teal",
            showcase=ui.HTML(
                '<i class="bi bi-check-circle" style="font-size: 2rem;"></i>'
            ),
            width="25%",
        ),
        ui.value_box(
            "Failed Inspections",
            str(len(inspection_data[inspection_data["Status"] == "Failed"])),
            theme="bg-gradient-red-orange",
            showcase=ui.HTML('<i class="bi bi-x-circle" style="font-size: 2rem;"></i>'),
            width="25%",
        ),
        ui.value_box(
            "Average Score",
            f"{inspection_data['Inspection Score'].mean():.2f}",
            theme="bg-gradient-yellow-orange",
            showcase=ui.HTML(
                '<i class="bi bi-bar-chart" style="font-size: 2rem;"></i>'
            ),
            width="25%",
        ),
    ),
    ui.hr(),
    ui.layout_column_wrap(
        ui.input_date_range("date_range", "Filter by Inspection Date"),
        ui.input_select(
            "violation_filter",
            "Filter by Violation",
            ["All", "None", "Minor", "Major"],
            selected="All",
        ),
        ui.input_select(
            "status_filter",
            "Filter by Status",
            ["All", "Passed", "Failed"],
            selected="All",
        ),
        width=1 / 3,
    ),
    ui.output_data_frame("inspection_table"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.data_frame
    def inspection_table():
        filtered_data = inspection_data
        if input.date_range():
            start_date, end_date = input.date_range()
            start_date = datetime.combine(start_date, datetime.min.time())
            end_date = datetime.combine(end_date, datetime.max.time())
            filtered_data = filtered_data[
                (filtered_data["Inspection Date"] >= start_date)
                & (filtered_data["Inspection Date"] <= end_date)
            ]

        if input.violation_filter() != "All":
            filtered_data = filtered_data[
                filtered_data["Violation"] == input.violation_filter()
            ]

        if input.status_filter() != "All":
            filtered_data = filtered_data[
                filtered_data["Status"] == input.status_filter()
            ]

        return filtered_data


app = App(app_ui, server)
