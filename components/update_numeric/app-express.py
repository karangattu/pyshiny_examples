from shiny import reactive
from shiny.express import input, ui, render

# Add page title
ui.page_opts(title="Update Numeric Demo", fillable=True)

with ui.card():
    ui.card_header("Update Numeric Demo")

    # Create a numeric input that we'll update
    ui.input_numeric("number", "Number", value=5)

    # Display current value
    @render.text
    def show_value():
        return f"Current value: {input.number()}"


with ui.card():
    ui.card_header("Control Panel")

    # Create controls to demonstrate each parameter of update_numeric
    with ui.layout_column_wrap(width=1 / 2):
        ui.input_text("new_label", "New Label", value="Updated Number")
        ui.input_numeric("new_value", "New Value", value=10)
        ui.input_numeric("new_min", "New Min", value=0)
        ui.input_numeric("new_max", "New Max", value=100)
        ui.input_numeric("new_step", "New Step", value=5)
        ui.input_action_button(
            "update", "Update Numeric Input", class_="btn-primary mt-3"
        )


# Add effect to update the numeric input when button is clicked
@reactive.effect
@reactive.event(input.update)
def _():
    ui.update_numeric(
        id="number",
        label=input.new_label(),
        value=input.new_value(),
        min=input.new_min(),
        max=input.new_max(),
        step=input.new_step(),
    )
