import random
from datetime import datetime, timedelta
from typing import Dict, List, Tuple

import pandas as pd
from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui

# Sample data for volunteer opportunities
volunteer_data: List[Dict[str, any]] = [
    {
        "id": 1,
        "title": "Animal Shelter Volunteer",
        "description": "Help care for rescued animals at our local animal shelter.",
        "location": "123 Main St, Anytown USA",
        "date": datetime(2023, 5, 1),
        "duration": 4,
        "spots_available": 10,
    },
    {
        "id": 2,
        "title": "Food Bank Sorting",
        "description": "Sort and package food donations at the community food bank.",
        "location": "456 Oak Rd, Anytown USA",
        "date": datetime(2023, 5, 15),
        "duration": 3,
        "spots_available": 15,
    },
    {
        "id": 3,
        "title": "Habitat for Humanity Build",
        "description": "Help construct a new home for a family in need.",
        "location": "789 Elm St, Anytown USA",
        "date": datetime(2023, 6, 1),
        "duration": 8,
        "spots_available": 20,
    },
    {
        "id": 4,
        "title": "Soup Kitchen Serving",
        "description": "Serve meals to those in need at the local soup kitchen.",
        "location": "321 Oak Ln, Anytown USA",
        "date": datetime(2023, 6, 15),
        "duration": 2,
        "spots_available": 12,
    },
    {
        "id": 5,
        "title": "Park Cleanup",
        "description": "Help clean up and maintain the community park.",
        "location": "159 Maple Ave, Anytown USA",
        "date": datetime(2023, 7, 1),
        "duration": 3,
        "spots_available": 18,
    },
]

# Convert the date to a string for display
for opportunity in volunteer_data:
    opportunity["date_str"] = opportunity["date"].strftime("%B %d, %Y")

app_ui = ui.page_fluid(
    ui.panel_title("Volunteer Opportunities"),
    ui.layout_column_wrap(
        ui.input_text("search", "Search:", placeholder="Search by title or location"),
        ui.input_date_range("date_range", "Date Range"),
        ui.input_numeric("duration", "Duration (hours)", min=0, max=24, value=0),
        ui.input_numeric("spots_available", "Spots Available", min=0, max=100, value=0),
        width=1 / 3,
    ),
    ui.output_data_frame("opportunities_table"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @reactive.calc
    def filtered_opportunities() -> pd.DataFrame:
        df = pd.DataFrame(volunteer_data)
        if input.search():
            df = df[
                df["title"].str.contains(input.search(), case=False)
                | df["location"].str.contains(input.search(), case=False)
            ]
        if input.date_range():
            start_date = datetime.combine(input.date_range()[0], datetime.min.time())
            end_date = datetime.combine(input.date_range()[1], datetime.max.time())
            df = df[
                (df["date"] >= start_date)
                & (df["date"] <= end_date)
            ]
        if input.duration() > 0:
            df = df[df["duration"] >= input.duration()]
        if input.spots_available() > 0:
            df = df[df["spots_available"] >= input.spots_available()]
        return df

    @render.data_frame
    def opportunities_table():
        return render.DataGrid(
            filtered_opportunities(),
            selection_mode="rows",
            columns=[
                {"name": "Title", "field": "title"},
                {"name": "Description", "field": "description"},
                {"name": "Location", "field": "location"},
                {"name": "Date", "field": "date_str"},
                {"name": "Duration (hours)", "field": "duration"},
                {"name": "Spots Available", "field": "spots_available"},
            ],
        )

    @opportunities_table.set_patch_fn
    def _(*, patch: render.CellPatch):
        # Handle volunteer sign-up
        row_index = patch["row_index"]
        opportunity = volunteer_data[row_index]
        opportunity["spots_available"] -= 1
        return opportunity["spots_available"]

app = App(app_ui, server)