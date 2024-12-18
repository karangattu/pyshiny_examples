from datetime import date, timedelta
from shiny import reactive
from shiny.express import input, render, ui

# Set page title
ui.page_opts(title="Date Range Update Demo")

# Create a slider to control the date range window size
ui.input_slider("window_size", "Date window size (days)", min=1, max=30, value=7)

# Create a date range input
ui.input_date_range(
    "date_range",
    "Select date range",
    start=date.today() - timedelta(days=7),
    end=date.today(),
)

# Create a button to center the date range on today
ui.input_action_button("center_today", "Center on Today", class_="btn-primary")

# Create a button to shift range backwards
ui.input_action_button("shift_back", "⬅️ Shift Back", class_="m-2")

# Create a button to shift range forward
ui.input_action_button("shift_forward", "Shift Forward ➡️", class_="m-2")


@reactive.effect
@reactive.event(input.center_today)
def _():
    window = input.window_size() // 2
    ui.update_date_range(
        "date_range",
        start=date.today() - timedelta(days=window),
        end=date.today() + timedelta(days=window),
    )


@reactive.effect
@reactive.event(input.shift_back)
def _():
    current_start = input.date_range()[0]
    current_end = input.date_range()[1]
    window = (current_end - current_start).days

    ui.update_date_range(
        "date_range",
        start=current_start - timedelta(days=window),
        end=current_end - timedelta(days=window),
    )


@reactive.effect
@reactive.event(input.shift_forward)
def _():
    current_start = input.date_range()[0]
    current_end = input.date_range()[1]
    window = (current_end - current_start).days

    ui.update_date_range(
        "date_range",
        start=current_start + timedelta(days=window),
        end=current_end + timedelta(days=window),
    )


# Display current selection
@render.text
def selected_range():
    start, end = input.date_range()
    return f"Selected range: {start} to {end} ({(end-start).days + 1} days)"
