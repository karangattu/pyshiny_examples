from datetime import date, timedelta
import random
from shiny import reactive
from shiny.express import input, ui, render

# Set page options for a clean layout
ui.page_opts(title="Date Range Update Demo", fillable=True)

# Create a sidebar with controls
with ui.sidebar():
    ui.h4("Control Panel")

    ui.input_select(
        "param_to_update",
        "Parameter to Update",
        {
            "label": "Update Label",
            "start": "Update Start Date",
            "end": "Update End Date",
            "min": "Update Min Date",
            "max": "Update Max Date",
            "all": "Update All Parameters",
        },
    )

    ui.input_action_button("update_btn", "Apply Update", class_="btn-primary")

# Main content area
with ui.layout_columns():
    with ui.card():
        ui.card_header("Original Date Range Input")
        ui.input_date_range(
            "date_range1",
            "Select Date Range",
            start=date(2023, 1, 1),
            end=date(2023, 12, 31),
            min=date(2023, 1, 1),
            max=date(2024, 12, 31),
        )

    with ui.card():
        ui.card_header("Current Values")

        @render.ui
        def show_values():
            dates = input.date_range1()
            if dates is None:
                return "No dates selected"
            return ui.tags.div(
                ui.tags.p(f"Start Date: {dates[0]}"), ui.tags.p(f"End Date: {dates[1]}")
            )


# Function to generate random dates
def random_date(start, end):
    time_between = end - start
    days_between = time_between.days
    random_days = random.randrange(days_between)
    return start + timedelta(days=random_days)


# Effect to handle updates
@reactive.effect
@reactive.event(input.update_btn)
def _():
    param = input.param_to_update()
    base_date = date(2023, 1, 1)

    if param == "label":
        ui.update_date_range(
            "date_range1", label=f"Updated Label ({random.randint(1, 100)})"
        )

    elif param == "start":
        new_start = random_date(date(2023, 1, 1), date(2023, 6, 30))
        ui.update_date_range("date_range1", start=new_start)

    elif param == "end":
        new_end = random_date(date(2023, 7, 1), date(2023, 12, 31))
        ui.update_date_range("date_range1", end=new_end)

    elif param == "min":
        new_min = random_date(date(2022, 1, 1), date(2023, 1, 1))
        ui.update_date_range("date_range1", min=new_min)

    elif param == "max":
        new_max = random_date(date(2024, 1, 1), date(2024, 12, 31))
        ui.update_date_range("date_range1", max=new_max)

    elif param == "all":
        new_start = random_date(date(2023, 1, 1), date(2023, 6, 30))
        new_end = random_date(date(2023, 7, 1), date(2023, 12, 31))
        new_min = random_date(date(2022, 1, 1), date(2023, 1, 1))
        new_max = random_date(date(2024, 1, 1), date(2024, 12, 31))

        ui.update_date_range(
            "date_range1",
            label=f"Complete Update ({random.randint(1, 100)})",
            start=new_start,
            end=new_end,
            min=new_min,
            max=new_max,
        )


# Add notifications to show what's being updated
@reactive.effect
@reactive.event(input.update_btn)
def show_notification():
    param = input.param_to_update()
    ui.notification_show(f"Updated {param} parameter(s)", duration=3, type="message")
