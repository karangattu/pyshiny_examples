from shiny import App, reactive, render, ui

app_ui = ui.page_fillable(
    # First card
    ui.card(
        ui.card_header("Update Numeric Demo"),
        # Create a numeric input that we'll update
        ui.input_numeric("number", "Number", value=5),
        # Display current value
        ui.output_text("show_value"),
    ),
    # Second card
    ui.card(
        ui.card_header("Control Panel"),
        # Create controls to demonstrate each parameter of update_numeric
        ui.layout_column_wrap(
            ui.input_text("new_label", "New Label", value="Updated Number"),
            ui.input_numeric("new_value", "New Value", value=10),
            ui.input_numeric("new_min", "New Min", value=0),
            ui.input_numeric("new_max", "New Max", value=100),
            ui.input_numeric("new_step", "New Step", value=5),
            ui.input_action_button(
                "update", "Update Numeric Input", class_="btn-primary mt-3"
            ),
            width=1 / 2,
        ),
    ),
)


def server(input, output, session):
    # Display current value
    @output
    @render.text
    def show_value():
        return f"Current value: {input.number()}"

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


app = App(app_ui, server)
