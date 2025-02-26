from datetime import date
from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Date Range Update Demo", fillable=True)

with ui.layout_sidebar():
    with ui.sidebar():
        # Basic date range input to be updated
        ui.input_date_range(
            id="date_range",
            label="Select Date Range",
            start=date(2023, 1, 1),
            end=date(2023, 12, 31),
        )

        # Controls for updating the date range
        ui.input_text(id="new_label", label="New Label", value="Updated Date Range")

        ui.input_date(id="new_start", label="New Start Date", value=date(2023, 6, 1))

        ui.input_date(id="new_end", label="New End Date", value=date(2023, 6, 30))

        ui.input_date(id="new_min", label="New Min Date", value=date(2023, 1, 1))

        ui.input_date(id="new_max", label="New Max Date", value=date(2023, 12, 31))

        ui.input_action_button(
            id="update", label="Update Date Range", class_="btn-primary mt-3"
        )

    # Main panel content
    with ui.card():
        ui.card_header("Current Selection")

        @render.text
        def current_range():
            dates = input.date_range()
            if dates is None:
                return "No dates selected"
            return f"Current selection: {dates[0]} to {dates[1]}"


# Update effect
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
