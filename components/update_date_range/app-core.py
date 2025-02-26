from datetime import date
from shiny import App, reactive, render, ui

# Define the UI
app_ui = ui.page_fillable(
    ui.layout_sidebar(
        ui.sidebar(
            # Basic date range input to be updated
            ui.input_date_range(
                id="date_range",
                label="Select Date Range",
                start=date(2023, 1, 1),
                end=date(2023, 12, 31),
            ),
            # Controls for updating the date range
            ui.input_text(
                id="new_label", label="New Label", value="Updated Date Range"
            ),
            ui.input_date(
                id="new_start", label="New Start Date", value=date(2023, 6, 1)
            ),
            ui.input_date(id="new_end", label="New End Date", value=date(2023, 6, 30)),
            ui.input_date(id="new_min", label="New Min Date", value=date(2023, 1, 1)),
            ui.input_date(id="new_max", label="New Max Date", value=date(2023, 12, 31)),
            ui.input_action_button(
                id="update", label="Update Date Range", class_="btn-primary mt-3"
            ),
        ),
        ui.card(
            ui.card_header("Current Selection"),
            ui.output_text("current_range"),
        ),
    )
)


# Define the server
def server(input, output, session):
    @output
    @render.text
    def current_range():
        dates = input.date_range()
        if dates is None:
            return "No dates selected"
        return f"Current selection: {dates[0]} to {dates[1]}"

    @reactive.effect
    @reactive.event(input.update)
    def _():
        ui.update_date_range(
            id="date_range",
            label=input.new_label(),
            start=input.new_start(),
            end=input.new_end(),
            min=input.new_min(),
            max=input.new_max(),
        )


# Create and return the app
app = App(app_ui, server)
