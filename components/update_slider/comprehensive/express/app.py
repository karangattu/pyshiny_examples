import random
from datetime import date, timedelta

from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Update Slider Demonstration", fillable=True)

# Create some sample data for demonstration
with ui.layout_sidebar():
    with ui.sidebar():
        # Controller slider to demonstrate various update scenarios
        ui.input_slider(
            "controller", "Controller Slider", min=0, max=100, value=50, step=1
        )

        # Buttons to trigger different update scenarios
        ui.input_action_button("update_value", "Update Value")
        ui.input_action_button("update_label", "Update Label")
        ui.input_action_button("update_min_max", "Update Min/Max")
        ui.input_action_button("update_step", "Update Step")
        ui.input_action_button("update_time_format", "Update Time Format")
        ui.input_action_button("update_timezone", "Update Timezone")

    # Sliders to demonstrate various update scenarios
    with ui.layout_columns():
        # Numeric slider
        ui.input_slider(
            "numeric_slider", "Numeric Slider", min=0, max=100, value=50, step=1
        )

        # Date slider
        ui.input_slider(
            "date_slider",
            "Date Slider",
            min=date(2023, 1, 1),
            max=date(2023, 12, 31),
            value=date(2023, 6, 15),
        )

        # Datetime slider
        ui.input_slider(
            "datetime_slider",
            "Datetime Slider",
            min=date(2023, 1, 1),
            max=date(2023, 12, 31),
            value=date(2023, 6, 15),
            time_format="%Y-%m-%d",
            timezone="+0000",
        )

    # Display current slider states
    @render.text
    def slider_states():
        return f"""
        Numeric Slider: 
        - Value: {input.numeric_slider()}
        
        Date Slider: 
        - Value: {input.date_slider()}
        
        Datetime Slider: 
        - Value: {input.datetime_slider()}
        """


# Reactive effects to update sliders
@reactive.effect
@reactive.event(input.update_value)
def _():
    # Update the value of the numeric slider
    ui.update_slider("numeric_slider", value=random.randint(0, 100))


@reactive.effect
@reactive.event(input.update_label)
def _():
    # Update the label of the numeric slider
    ui.update_slider(
        "numeric_slider", label=f"Numeric Slider (Updated at {random.randint(0, 1000)})"
    )


@reactive.effect
@reactive.event(input.update_min_max)
def _():
    # Update the min and max of the numeric slider
    new_min = random.randint(0, 50)
    new_max = random.randint(new_min + 10, 200)
    ui.update_slider(
        "numeric_slider",
        min=new_min,
        max=new_max,
        value=new_min,  # Ensure value is within new range
    )


@reactive.effect
@reactive.event(input.update_step)
def _():
    # Update the step of the numeric slider
    new_step = random.choice([1, 5, 10, 25])
    ui.update_slider("numeric_slider", step=new_step)


@reactive.effect
@reactive.event(input.update_time_format)
def _():
    # Update the time format of the datetime slider
    new_format = random.choice(["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d"])
    ui.update_slider("datetime_slider", time_format=new_format)


@reactive.effect
@reactive.event(input.update_timezone)
def _():
    # Update the timezone of the datetime slider
    new_timezone = random.choice(
        [
            "+0000",  # UTC
            "+0100",  # Central European Time
            "-0500",  # Eastern Standard Time
            "+0930",  # Australian Central Standard Time
        ]
    )
    ui.update_slider("datetime_slider", timezone=new_timezone)
