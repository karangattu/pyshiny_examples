from datetime import datetime, timedelta
from shiny import App, reactive, render, ui

# Define the UI
app_ui = ui.page_fillable(
    # Set page title in the UI definition
    ui.panel_title("Slider Update Demo"),
    # First card with main slider
    ui.card(
        ui.card_header("Main Slider"),
        ui.input_slider(
            id="target_slider", label="Target Slider", min=0, max=100, value=50
        ),
        ui.output_text("current_value"),
    ),
    # Second card with control panel
    ui.card(
        ui.card_header("Control Panel"),
        ui.layout_column_wrap(
            # Controls for updating the target slider
            ui.input_text(id="new_label", label="New Label", value="Updated Label"),
            ui.input_numeric(id="new_value", label="New Value", value=50),
            ui.input_numeric(id="new_min", label="New Min", value=0),
            ui.input_numeric(id="new_max", label="New Max", value=100),
            ui.input_numeric(id="new_step", label="New Step", value=1),
            # Date-related inputs
            ui.input_checkbox(id="use_dates", label="Use Dates Instead", value=False),
            ui.input_text(
                id="time_format", label="Time Format (for dates)", value="%Y-%m-%d"
            ),
            ui.input_text(id="timezone", label="Timezone (for dates)", value="+0000"),
            ui.input_action_button(
                id="update", label="Update Slider", class_="btn-primary"
            ),
            width=1 / 3,
        ),
    ),
)


# Define the server
def server(input, output, session):
    @output
    @render.text
    def current_value():
        return f"Current slider value: {input.target_slider()}"

    @reactive.effect
    @reactive.event(input.update)
    def _():
        if input.use_dates():
            # Convert numeric values to dates for date slider
            base_date = datetime.now()
            value_date = base_date + timedelta(days=int(input.new_value()))
            min_date = base_date + timedelta(days=int(input.new_min()))
            max_date = base_date + timedelta(days=int(input.new_max()))

            ui.update_slider(
                id="target_slider",
                label=input.new_label(),
                value=value_date,
                min=min_date,
                max=max_date,
                step=input.new_step(),
                time_format=input.time_format(),
                timezone=input.timezone(),
            )
        else:
            # Regular numeric slider update
            ui.update_slider(
                id="target_slider",
                label=input.new_label(),
                value=input.new_value(),
                min=input.new_min(),
                max=input.new_max(),
                step=input.new_step(),
            )


# Create and return the app
app = App(app_ui, server)
