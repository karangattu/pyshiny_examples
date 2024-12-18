from datetime import date
from shiny import reactive
from shiny.express import input, render, ui

ui.page_opts(title="Date Input Demo", fillable=True)

with ui.layout_columns():
    # Basic date input with default value
    with ui.card():
        ui.card_header("Basic Date Input")
        ui.input_date("date1", "Default date input:", value="2024-01-01")

    # Date input with min and max dates
    with ui.card():
        ui.card_header("Date Range Limits")
        ui.input_date(
            "date2",
            "Date with min/max limits:",
            value=date(2024, 1, 15),
            min="2024-01-01",
            max="2024-12-31",
        )

    # Date input with custom format
    with ui.card():
        ui.card_header("Custom Format")
        ui.input_date(
            "date3", "Custom format (mm/dd/yy):", value="2024-02-29", format="mm/dd/yy"
        )

    # Date input with different start view
    with ui.card():
        ui.card_header("Different Start View")
        ui.input_date(
            "date4", "Start with decade view:", value="2024-03-15", startview="decade"
        )

    # Date input with custom week start
    with ui.card():
        ui.card_header("Custom Week Start")
        ui.input_date(
            "date5", "Week starts on Monday:", value="2024-03-01", weekstart=1
        )

    # Date input with different language
    with ui.card():
        ui.card_header("Different Language")
        ui.input_date("date6", "German language:", value="2024-03-01", language="de")

    # Date input with custom width
    with ui.card():
        ui.card_header("Custom Width")
        ui.input_date("date7", "Wide input field:", value="2024-03-01", width="300px")

    # Date input with autoclose disabled
    with ui.card():
        ui.card_header("Autoclose Disabled")
        ui.input_date(
            "date8", "Calendar stays open:", value="2024-03-01", autoclose=False
        )

    # Date input with disabled dates
    with ui.card():
        ui.card_header("Disabled Dates")
        ui.input_date(
            "date9",
            "Some dates disabled:",
            value="2024-03-01",
            datesdisabled=["2024-03-15", "2024-03-16", "2024-03-17"],
        )

    # Date input with disabled days of week
    with ui.card():
        ui.card_header("Disabled Days")
        ui.input_date(
            "date10",
            "Weekends disabled:",
            value="2024-03-01",
            daysofweekdisabled=[0, 6],  # Sunday and Saturday
        )

# Display all selected dates
with ui.card():
    ui.card_header("Selected Dates")

    @render.data_frame
    def selected_dates():
        dates = {
            "Input": [f"date{i}" for i in range(1, 11)],
            "Selected Date": [
                input.date1(),
                input.date2(),
                input.date3(),
                input.date4(),
                input.date5(),
                input.date6(),
                input.date7(),
                input.date8(),
                input.date9(),
                input.date10(),
            ],
        }
        return dates
