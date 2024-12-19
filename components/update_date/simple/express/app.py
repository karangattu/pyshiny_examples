from datetime import date, timedelta
from shiny import reactive
from shiny.express import input, render, ui

# Page title
ui.page_opts(title="Date Input Demo")

with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_slider("days_to_add", "Days to add/subtract", min=-10, max=10, value=0)
        ui.input_date(
            "selected_date",
            "Select a date",
            value="2024-01-01",
            min="2023-01-01",
            max="2024-12-31",
        )

    with ui.card():
        ui.card_header("Date Information")

        @render.text
        def date_info():
            current_date = input.selected_date()
            days_delta = input.days_to_add()
            return f"Selected date: {current_date}\nDate {abs(days_delta)} days {'ahead' if days_delta >= 0 else 'ago'}: {current_date + timedelta(days=days_delta)}"


@reactive.effect
def _():
    # Get the current date from input
    current_date = input.selected_date()
    days_to_add = input.days_to_add()

    # Calculate new date
    new_date = current_date + timedelta(days=days_to_add)

    # Update the date input
    ui.update_date(
        "selected_date",
        label=f"Date (adjusted by {days_to_add:+d} days)",
        value=new_date,
    )
