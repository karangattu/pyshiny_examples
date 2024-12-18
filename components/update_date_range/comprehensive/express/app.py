from datetime import date, timedelta
import pandas as pd
import numpy as np

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
start_date = date(2023, 1, 1)
end_date = date(2023, 12, 31)
dates = pd.date_range(start=start_date, end=end_date)
data = pd.DataFrame(
    {
        "date": dates,
        "value": np.random.randn(len(dates)).cumsum(),
        "category": np.random.choice(["A", "B", "C"], size=len(dates)),
    }
)

# Page options
ui.page_opts(title="Date Range Update Demo", fillable=True)

# Sidebar with controls
with ui.sidebar():
    # Initial date range input
    ui.input_date_range(
        "original_date_range",
        "Original Date Range",
        start=start_date,
        end=end_date,
        min=start_date - timedelta(days=30),
        max=end_date + timedelta(days=30),
    )

    # Controls for updating date range
    ui.input_select(
        "update_type",
        "Update Type",
        choices=["Change Label", "Change Dates", "Change Min/Max", "Reset to Default"],
    )

    # Conditional inputs based on update type
    with ui.panel_conditional("input.update_type === 'Change Label'"):
        ui.input_text("new_label", "New Label")

    with ui.panel_conditional("input.update_type === 'Change Dates'"):
        ui.input_date("start_date", "New Start Date")
        ui.input_date("end_date", "New End Date")

    with ui.panel_conditional("input.update_type === 'Change Min/Max'"):
        ui.input_date("new_min", "New Minimum Date")
        ui.input_date("new_max", "New Maximum Date")

    # Update button
    ui.input_action_button("update_btn", "Update Date Range")

# Main panel with data display and current state
with ui.layout_columns():
    # Filtered data table
    @render.data_frame
    def filtered_data():
        # Filter data based on the current date range
        start, end = input.original_date_range()
        filtered = data[(data["date"].dt.date >= start) & (data["date"].dt.date <= end)]
        return filtered

    # Display current date range details
    @render.text
    def date_range_details():
        start, end = input.original_date_range()
        return f"Current Date Range: {start} to {end}"


# Reactive effect to handle date range updates
@reactive.effect
@reactive.event(input.update_btn)
def update_date_range():
    if input.update_type() == "Change Label":
        # Update label
        ui.update_date_range(
            "original_date_range", label=input.new_label() or "Updated Date Range"
        )

    elif input.update_type() == "Change Dates":
        # Update start and end dates
        start_date = input.start_date() or date(2023, 1, 1)
        end_date = input.end_date() or date(2023, 12, 31)

        ui.update_date_range("original_date_range", start=start_date, end=end_date)

    elif input.update_type() == "Change Min/Max":
        # Update min and max dates
        new_min = input.new_min() or (start_date - timedelta(days=60))
        new_max = input.new_max() or (end_date + timedelta(days=60))

        ui.update_date_range("original_date_range", min=new_min, max=new_max)

    elif input.update_type() == "Reset to Default":
        # Reset to original dates
        ui.update_date_range(
            "original_date_range",
            start=start_date,
            end=end_date,
            min=start_date - timedelta(days=30),
            max=end_date + timedelta(days=30),
            label="Original Date Range",
        )
