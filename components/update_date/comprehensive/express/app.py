from datetime import date, timedelta
from shiny import reactive
from shiny.express import input, render, ui

# Page options and title
ui.page_opts(title="Date Input Update Demo", fillable=True)

# Create a sidebar layout
with ui.layout_sidebar():
    with ui.sidebar():
        # Original date input
        ui.input_date(
            "date1",
            "Original Date Input",
            value=date(2024, 1, 1),
            min=date(2023, 1, 1),
            max=date(2025, 12, 31),
        )

        # Controls for updating the date input
        ui.input_text("new_label", "New Label", value="Updated Date Label")

        ui.input_date("new_value", "New Value", value=date(2024, 6, 15))

        ui.input_date("new_min", "New Min Date", value=date(2023, 6, 1))

        ui.input_date("new_max", "New Max Date", value=date(2025, 6, 30))

        # Button to trigger the update
        ui.input_action_button("update", "Update Date Input", class_="btn-primary")

        # Button to reset
        ui.input_action_button("reset", "Reset", class_="btn-secondary")

    # Main panel content
    with ui.card():
        ui.card_header("Current Settings")

        @render.text
        def current_date():
            return f"Selected Date: {input.date1()}"

        @render.text
        def current_label():
            return f"Current Label: {input.new_label()}"

        @render.text
        def current_min():
            return f"Current Min: {input.new_min()}"

        @render.text
        def current_max():
            return f"Current Max: {input.new_max()}"


# Effect to handle the update button click
@reactive.effect
@reactive.event(input.update)
def _():
    ui.update_date(
        id="date1",
        label=input.new_label(),
        value=input.new_value(),
        min=input.new_min(),
        max=input.new_max(),
    )
    ui.notification_show("Date input updated!", type="message")


# Effect to handle the reset button click
@reactive.effect
@reactive.event(input.reset)
def _():
    # Reset to original values
    ui.update_date(
        id="date1",
        label="Original Date Input",
        value=date(2024, 1, 1),
        min=date(2023, 1, 1),
        max=date(2025, 12, 31),
    )

    # Reset the control inputs
    ui.update_text("new_label", value="Updated Date Label")
    ui.update_date("new_value", value=date(2024, 6, 15))
    ui.update_date("new_min", value=date(2023, 6, 1))
    ui.update_date("new_max", value=date(2025, 6, 30))

    ui.notification_show("Values reset to default!", type="default")
