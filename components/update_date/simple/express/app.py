from datetime import date, timedelta
import random
import pandas as pd

from shiny import reactive
from shiny.express import input, ui, render


# Create synthetic data
def generate_synthetic_data(base_date):
    """Generate a DataFrame with synthetic data based on a given date."""
    dates = [base_date + timedelta(days=i) for i in range(-30, 31)]
    data = {
        "date": dates,
        "value": [random.uniform(10, 100) for _ in dates],
        "category": random.choice(["A", "B", "C"]),
    }
    return pd.DataFrame(data)


# Initial data
initial_date = date(2023, 1, 1)
df = generate_synthetic_data(initial_date)

# Page setup
ui.page_opts(title="Date Update Demo")

# Sidebar with controls
with ui.sidebar():
    # Initial date input
    ui.input_date("base_date", "Base Date", value=initial_date)

    # Buttons to modify date
    ui.input_action_button("add_week", "Add 1 Week")
    ui.input_action_button("subtract_week", "Subtract 1 Week")
    ui.input_action_button("random_date", "Random Date")


# Main panel with data display
@render.data_frame
def data_table():
    # Filter data based on the current base date
    filtered_df = df[df["date"] == input.base_date()]
    return filtered_df


# Reactive effects to update the date
@reactive.effect
@reactive.event(input.add_week)
def _():
    new_date = input.base_date() + timedelta(weeks=1)
    ui.update_date("base_date", value=new_date)


@reactive.effect
@reactive.event(input.subtract_week)
def _():
    new_date = input.base_date() - timedelta(weeks=1)
    ui.update_date("base_date", value=new_date)


@reactive.effect
@reactive.event(input.random_date)
def _():
    # Generate a random date within the existing dataset
    random_date = random.choice(df["date"].tolist())
    ui.update_date("base_date", value=random_date)


# Additional reactive effect to regenerate data when date changes
@reactive.effect
def _():
    global df
    df = generate_synthetic_data(input.base_date())
