from datetime import date, timedelta
import pandas as pd
import numpy as np
from shiny import reactive
from shiny.express import input, ui, render

# Generate sample data
dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq="D")
data = pd.DataFrame(
    {
        "date": dates,
        "value": np.random.normal(100, 10, len(dates)),
        "category": np.random.choice(["A", "B", "C"], len(dates)),
    }
)

# UI components
ui.page_opts(title="Date Input Demo", fillable=True)

with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_date(
            "selected_date",
            "Select Date",
            value="2024-01-01",
            min="2024-01-01",
            max="2024-12-31",
        )

        ui.input_numeric("days_range", "Days Before/After", value=7, min=1, max=30)

    @render.table
    def filtered_data():
        # Get selected date and convert to datetime
        sel_date = pd.to_datetime(input.selected_date())
        days = input.days_range()

        # Filter data within range of selected date
        mask = (data["date"] >= sel_date - timedelta(days=days)) & (
            data["date"] <= sel_date + timedelta(days=days)
        )

        return data[mask].round(2)

    @render.text
    def date_info():
        return f"Selected date: {input.selected_date()}"
