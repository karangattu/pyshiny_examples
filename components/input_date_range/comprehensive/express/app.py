from datetime import date, timedelta
import pandas as pd
import numpy as np
from shiny import reactive
from shiny.express import input, ui, render

# Sample data generation
start_date = date(2024, 1, 1)
dates = [start_date + timedelta(days=x) for x in range(365)]
data = pd.DataFrame({"date": dates, "value": np.random.normal(100, 15, 365)})

ui.page_opts(title="Date Range Input Demo", fillable=True)

with ui.layout_sidebar():
    with ui.sidebar():
        # Default date range
        ui.input_date_range("default_range", "Default date range (current date):")

        # Custom start and end dates
        ui.input_date_range(
            "custom_range",
            "Custom start/end dates:",
            start=date(2024, 1, 1),
            end=date(2024, 12, 31),
        )

        # Min and max constraints
        ui.input_date_range(
            "constrained_range",
            "Constrained date range (2024 only):",
            min=date(2024, 1, 1),
            max=date(2024, 12, 31),
            start=date(2024, 3, 1),
            end=date(2024, 9, 30),
        )

        # Custom format
        ui.input_date_range(
            "formatted_range",
            "Custom format (mm/dd/yy):",
            format="mm/dd/yy",
            start=date(2024, 1, 1),
            end=date(2024, 12, 31),
        )

        # Start with year view
        ui.input_date_range(
            "year_view_range",
            "Starts with year view:",
            startview="year",
            start=date(2024, 1, 1),
            end=date(2024, 12, 31),
        )

        # Week starts on Monday
        ui.input_date_range(
            "monday_start_range",
            "Week starts on Monday:",
            weekstart=1,
            start=date(2024, 1, 1),
            end=date(2024, 12, 31),
        )

        # German language
        ui.input_date_range(
            "german_range",
            "German language:",
            language="de",
            start=date(2024, 1, 1),
            end=date(2024, 12, 31),
        )

        # Custom separator
        ui.input_date_range(
            "custom_separator_range",
            "Custom separator:",
            separator=" → ",
            start=date(2024, 1, 1),
            end=date(2024, 12, 31),
        )

        # Custom width
        ui.input_date_range(
            "custom_width_range",
            "Custom width:",
            width="100%",
            start=date(2024, 1, 1),
            end=date(2024, 12, 31),
        )

        # Without autoclose
        ui.input_date_range(
            "no_autoclose_range",
            "Without autoclose:",
            autoclose=False,
            start=date(2024, 1, 1),
            end=date(2024, 12, 31),
        )

    # Main panel with output displays
    with ui.card():
        ui.card_header("Selected Date Ranges")

        @render.data_frame
        def date_ranges():
            ranges = {
                "Input Type": [
                    "Default",
                    "Custom",
                    "Constrained",
                    "Formatted",
                    "Year View",
                    "Monday Start",
                    "German",
                    "Custom Separator",
                    "Custom Width",
                    "No Autoclose",
                ],
                "Start Date": [
                    input.default_range()[0],
                    input.custom_range()[0],
                    input.constrained_range()[0],
                    input.formatted_range()[0],
                    input.year_view_range()[0],
                    input.monday_start_range()[0],
                    input.german_range()[0],
                    input.custom_separator_range()[0],
                    input.custom_width_range()[0],
                    input.no_autoclose_range()[0],
                ],
                "End Date": [
                    input.default_range()[1],
                    input.custom_range()[1],
                    input.constrained_range()[1],
                    input.formatted_range()[1],
                    input.year_view_range()[1],
                    input.monday_start_range()[1],
                    input.german_range()[1],
                    input.custom_separator_range()[1],
                    input.custom_width_range()[1],
                    input.no_autoclose_range()[1],
                ],
            }
            return pd.DataFrame(ranges)

    # Display filtered data based on the default range selection
    with ui.card():
        ui.card_header("Filtered Data Preview (using default range)")

        @render.data_frame
        def filtered_data():
            date_range = input.default_range()
            start_date = pd.to_datetime(date_range[0])
            end_date = pd.to_datetime(date_range[1])

            mask = (pd.to_datetime(data["date"]) >= start_date) & (
                pd.to_datetime(data["date"]) <= end_date
            )

            return data[mask].head(10)
