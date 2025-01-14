from datetime import date
from shiny import reactive
from shiny.express import input, ui, render

# Set page title
ui.page_opts(title="Date Input Demo")

with ui.layout_column_wrap(width="400px"):
    # Basic date input
    ui.input_date("date1", "Default date input:", value="2024-01-01")

    # Date input with min and max dates
    ui.input_date(
        "date2",
        "Date input with min/max:",
        value=date(2024, 1, 1),
        min="2024-01-01",
        max="2024-12-31",
    )

    # Date input with custom format
    ui.input_date(
        "date3", "Custom format (mm/dd/yy):", value="2024-01-01", format="mm/dd/yy"
    )

    # Date input with decade view
    ui.input_date(
        "date4", "Start in decade view:", value="2024-01-01", startview="decade"
    )

    # Date input with week starting on Monday
    ui.input_date("date5", "Week starts on Monday:", value="2024-01-01", weekstart=1)

    # Date input with German language
    ui.input_date("date6", "German language:", value="2024-01-01", language="de")

    # Date input with custom width
    ui.input_date("date7", "Custom width:", value="2024-01-01", width="400px")

    # Date input with autoclose disabled
    ui.input_date("date8", "Autoclose disabled:", value="2024-01-01", autoclose=False)

    # Date input with specific dates disabled
    ui.input_date(
        "date9",
        "Specific dates disabled:",
        value="2024-01-01",
        datesdisabled=["2024-01-15", "2024-01-16", "2024-01-17"],
    )

    # Date input with specific days of week disabled
    ui.input_date(
        "date10",
        "Weekends disabled:",
        value="2024-01-01",
        daysofweekdisabled=[0, 6],  # 0 = Sunday, 6 = Saturday
    )

with ui.card():
    ui.card_header("Selected Dates")

    @render.text
    def selected_dates():
        return (
            f"Default: {input.date1()}\n"
            f"Min/Max: {input.date2()}\n"
            f"Custom Format: {input.date3()}\n"
            f"Decade View: {input.date4()}\n"
            f"Monday Start: {input.date5()}\n"
            f"German: {input.date6()}\n"
            f"Custom Width: {input.date7()}\n"
            f"No Autoclose: {input.date8()}\n"
            f"Dates Disabled: {input.date9()}\n"
            f"Weekends Disabled: {input.date10()}\n"
        )
