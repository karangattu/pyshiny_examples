from datetime import datetime, timedelta
from shiny import reactive
from shiny.express import input, render, ui

# Set page options
ui.page_opts(title="Slider Update Demo", fillable=True)

with ui.layout_sidebar():
    with ui.sidebar():
        # Controls for updating the numeric slider
        ui.h4("Numeric Slider Controls")
        ui.input_numeric("new_value", "New Value", 50, min=0, max=100)
        ui.input_numeric("new_min", "New Min", 0, min=0, max=100)
        ui.input_numeric("new_max", "New Max", 100, min=0, max=100)
        ui.input_numeric("new_step", "New Step Size", 1, min=0.1, max=10)
        ui.input_action_button("update_numeric", "Update Numeric Slider")

        ui.hr()

        # Controls for updating the date slider
        ui.h4("Date Slider Controls")
        ui.input_date("new_date", "New Date", value=datetime.now())
        ui.input_date(
            "new_date_min", "New Min Date", value=datetime.now() - timedelta(days=30)
        )
        ui.input_date(
            "new_date_max", "New Max Date", value=datetime.now() + timedelta(days=30)
        )
        ui.input_numeric("new_date_step", "New Step (days)", 1, min=1, max=7)
        ui.input_text("new_time_format", "New Time Format", value="%Y-%m-%d")
        ui.input_action_button("update_date", "Update Date Slider")

    # Main panel content
    with ui.card():
        ui.card_header("Numeric Slider")
        ui.input_slider(
            "numeric_slider", "Numeric Slider", min=0, max=100, value=50, step=1
        )

        @render.text
        def numeric_value():
            return f"Current value: {input.numeric_slider()}"

    with ui.card():
        ui.card_header("Date Slider")
        ui.input_slider(
            "date_slider",
            "Date Slider",
            min=datetime.now() - timedelta(days=30),
            max=datetime.now() + timedelta(days=30),
            value=datetime.now(),
            step=timedelta(days=1),
        )

        @render.text
        def date_value():
            return f"Current date: {input.date_slider()}"


# Update handlers for numeric slider
@reactive.effect
@reactive.event(input.update_numeric)
def update_numeric_slider():
    ui.update_slider(
        "numeric_slider",
        label=f"Numeric Slider (Last Updated: {datetime.now().strftime('%H:%M:%S')})",
        value=input.new_value(),
        min=input.new_min(),
        max=input.new_max(),
        step=input.new_step(),
    )


# Update handlers for date slider
@reactive.effect
@reactive.event(input.update_date)
def update_date_slider():
    ui.update_slider(
        "date_slider",
        label=f"Date Slider (Last Updated: {datetime.now().strftime('%H:%M:%S')})",
        value=input.new_date(),
        min=input.new_date_min(),
        max=input.new_date_max(),
        step=timedelta(days=input.new_date_step()),
        time_format=input.new_time_format(),
    )


# Add some helpful instructions
with ui.card():
    ui.card_header("Instructions")
    ui.markdown(
        """
    This app demonstrates all parameters of the `update_slider` function:
    
    * **label**: Updated automatically with timestamp
    * **value**: Set new value for the slider
    * **min**: Set new minimum value
    * **max**: Set new maximum value
    * **step**: Set new step size
    * **time_format**: For date sliders, set new time format (e.g., %Y-%m-%d)
    
    Try adjusting the controls in the sidebar and clicking the update buttons to see the changes.
    """
    )
