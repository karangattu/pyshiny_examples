from datetime import date, timedelta
from shiny import App, reactive, render, ui

# Define the UI
app_ui = ui.page_fluid(
    # Page title is set in the page_fluid
    ui.card(
        ui.card_header("Date Input Update Demo"),
        # Initial date input
        ui.input_date("demo_date", "Select a date", value=date(2024, 1, 1)),
        # Controls to demonstrate all update_date parameters
        ui.layout_column_wrap(
            ui.input_action_button(
                "update_label", "Update Label", class_="btn-primary m-1"
            ),
            ui.input_action_button(
                "update_value", "Update Value", class_="btn-info m-1"
            ),
            ui.input_action_button(
                "update_min", "Update Min Date", class_="btn-warning m-1"
            ),
            ui.input_action_button(
                "update_max", "Update Max Date", class_="btn-success m-1"
            ),
            width=1 / 2,
        ),
        # Display current settings
        ui.card(ui.output_text("current_value"), class_="mt-3"),
    )
)


# Define the server
def server(input, output, session):
    # Display current value
    @output
    @render.text
    def current_value():
        return f"Current date: {input.demo_date()}"

    # Effects to handle each parameter update
    @reactive.effect
    @reactive.event(input.update_label)
    def _():
        # Update the label
        ui.update_date(
            "demo_date", label=f"Updated Label ({date.today().strftime('%Y-%m-%d')})"
        )

    @reactive.effect
    @reactive.event(input.update_value)
    def _():
        # Update the value to tomorrow's date
        tomorrow = date.today() + timedelta(days=1)
        ui.update_date("demo_date", value=tomorrow)

    @reactive.effect
    @reactive.event(input.update_min)
    def _():
        # Update the minimum date to today
        ui.update_date("demo_date", min=date.today())

    @reactive.effect
    @reactive.event(input.update_max)
    def _():
        # Update the maximum date to 30 days from today
        max_date = date.today() + timedelta(days=30)
        ui.update_date("demo_date", max=max_date)


# Create and return the app
app = App(app_ui, server)
