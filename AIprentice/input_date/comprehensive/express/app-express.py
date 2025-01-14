from datetime import date
import pandas as pd
from shiny import reactive
from shiny.express import input, ui, render

ui.page_opts(title="Date Input Demo", fillable=True)

with ui.layout_columns():
    # Basic date input with default value
    ui.input_date("date1", "Basic date input with default value:", value="2024-02-29")

    # Date input with min and max dates
    ui.input_date(
        "date2",
        "Date with min/max range:",
        value=date(2024, 2, 1),
        min="2024-01-01",
        max="2024-12-31",
    )

    # Date input with custom format
    ui.input_date(
        "date3", "Custom format (mm/dd/yy):", value="2024-02-29", format="mm/dd/yy"
    )

    # Date input with decade view
    ui.input_date(
        "date4", "Start in decade view:", value="2024-02-29", startview="decade"
    )

    # Date input with custom week start (Monday=1)
    ui.input_date("date5", "Week starts on Monday:", value="2024-02-29", weekstart=1)

    # Date input with German language
    ui.input_date("date6", "German language:", value="2024-02-29", language="de")

    # Date input with custom width
    ui.input_date("date7", "Custom width:", value="2024-02-29", width="400px")

    # Date input with autoclose disabled
    ui.input_date("date8", "Autoclose disabled:", value="2024-02-29", autoclose=False)

    # Date input with disabled dates
    ui.input_date(
        "date9",
        "Some dates disabled:",
        value="2024-02-29",
        datesdisabled=["2024-03-01", "2024-03-02", "2024-03-03"],
    )

    # Date input with disabled days of week
    ui.input_date(
        "date10",
        "Weekends disabled:",
        value="2024-02-29",
        daysofweekdisabled=[0, 6],  # Sunday=0, Saturday=6
    )

# Display selected dates
with ui.card():
    ui.card_header("Selected Dates")

    @render.data_frame
    def selected_dates():
        df = pd.DataFrame(
            {
                "Input": [
                    "Basic",
                    "Min/Max Range",
                    "Custom Format",
                    "Decade View",
                    "Monday Start",
                    "German",
                    "Custom Width",
                    "No Autoclose",
                    "Disabled Dates",
                    "Disabled Weekends",
                ],
                "Selected Date": [
                    str(input.date1()),
                    str(input.date2()),
                    str(input.date3()),
                    str(input.date4()),
                    str(input.date5()),
                    str(input.date6()),
                    str(input.date7()),
                    str(input.date8()),
                    str(input.date9()),
                    str(input.date10()),
                ],
            }
        )
        return df
