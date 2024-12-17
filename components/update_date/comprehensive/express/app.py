from datetime import date, timedelta
import random
import pandas as pd

from shiny import reactive
from shiny.express import input, ui, render


# Create synthetic data
def generate_synthetic_dates(num_records=50):
    base_date = date(2023, 1, 1)
    data = {
        "event_date": [
            base_date + timedelta(days=random.randint(0, 365))
            for _ in range(num_records)
        ],
        "event_type": [
            random.choice(["Conference", "Meeting", "Workshop", "Seminar"])
            for _ in range(num_records)
        ],
        "attendees": [random.randint(10, 500) for _ in range(num_records)],
    }
    return pd.DataFrame(data)


# Generate the dataset
events_df = generate_synthetic_dates()

# Page options
ui.page_opts(title="Date Input Update Demonstration", fillable=True)

# Sidebar with interactive controls
with ui.sidebar():
    # Initial date input with various parameters
    ui.input_date(
        "base_date",
        "Base Date",
        value=date(2023, 7, 1),  # Default value
        min=date(2023, 1, 1),  # Minimum allowed date
        max=date(2023, 12, 31),  # Maximum allowed date
        format="mm/dd/yy",  # Custom date format
        language="en",  # Language for date picker
        startview="month",  # Start view of the date picker
    )

    # Slider to control date modifications
    ui.input_slider(
        "date_adjustment", "Date Adjustment", min=-30, max=30, value=0, step=1
    )

    # Buttons to demonstrate different update scenarios
    ui.input_action_button("reset_date", "Reset Date")
    ui.input_action_button("random_date", "Random Date")

# Main content area
with ui.layout_columns():
    # Filtered events table
    @render.data_frame
    def events_table():
        # Filter events based on the current date
        filtered_df = events_df[events_df["event_date"] >= input.base_date()]
        return filtered_df

    # Date details display
    @render.text
    def date_details():
        return f"""
        Current Date: {input.base_date()}
        Adjustment: {input.date_adjustment()} days
        Language: en
        Format: mm/dd/yy
        """


# Reactive effects to update the date
@reactive.effect
@reactive.event(input.date_adjustment)
def _():
    # Update date with adjustment
    adjusted_date = input.base_date() + timedelta(days=input.date_adjustment())
    ui.update_date(
        "base_date",
        value=adjusted_date,
        label=f"Adjusted Date (±{input.date_adjustment()} days)",
        min=date(2023, 1, 1),
        max=date(2023, 12, 31),
    )


@reactive.effect
@reactive.event(input.reset_date)
def _():
    # Reset to original date with custom label
    ui.update_date(
        "base_date",
        value=date(2023, 7, 1),
        label="Reset Base Date",
        min=date(2023, 1, 1),
        max=date(2023, 12, 31),
    )


@reactive.effect
@reactive.event(input.random_date)
def _():
    # Select a random date within the allowed range
    random_date = date(2023, 1, 1) + timedelta(days=random.randint(0, 365))
    ui.update_date(
        "base_date",
        value=random_date,
        label="Randomly Selected Date",
        min=date(2023, 1, 1),
        max=date(2023, 12, 31),
    )
