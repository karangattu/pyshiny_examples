from datetime import date, timedelta
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
start_date = date(2023, 1, 1)
end_date = date(2024, 12, 31)


# Create a DataFrame with random dates and associated data
def generate_synthetic_data():
    num_records = 100
    dates = [
        start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        for _ in range(num_records)
    ]

    data = {
        "date": dates,
        "value": np.random.randint(1, 1000, num_records),
        "category": np.random.choice(["A", "B", "C"], num_records),
    }

    return pd.DataFrame(data)


# Create the synthetic dataset
df = generate_synthetic_data()

# Page options and title
ui.page_opts(title="Comprehensive input_date Demo", fillable=True)

# Sidebar with various input_date configurations
with ui.sidebar():
    # Basic date input
    ui.input_date("basic_date", "Basic Date Input")

    # Date input with initial value
    ui.input_date("initial_date", "Date with Initial Value", value="2024-01-15")

    # Date input with min and max constraints
    ui.input_date(
        "constrained_date",
        "Date with Min/Max",
        min="2023-01-01",
        max="2024-12-31",
        value="2024-06-15",
    )

    # Date input with different format
    ui.input_date(
        "formatted_date", "Custom Format Date", value="2024-02-14", format="mm/dd/yy"
    )

    # Date input with different language and week start
    ui.input_date(
        "international_date",
        "International Date",
        language="de",
        weekstart=1,  # Monday
        value="2024-03-20",
    )

    # Date input with decade view
    ui.input_date(
        "decade_view_date", "Decade View", startview="decade", value="2024-04-01"
    )

    # Date input with disabled specific dates and days of week
    ui.input_date(
        "disabled_date",
        "Disabled Dates/Days",
        value="2024-05-15",
        datesdisabled=["2024-05-01", "2024-05-02"],
        daysofweekdisabled=[0, 6],
    )  # Disable Sunday and Saturday

# Main content area with visualizations and tables
with ui.layout_columns():
    # Visualization of selected dates
    with ui.card(full_screen=True):
        ui.card_header("Date Selection Visualization")

        @render.plot
        def date_plot():
            selected_dates = [
                input.basic_date(),
                input.initial_date(),
                input.constrained_date(),
                input.formatted_date(),
                input.international_date(),
                input.decade_view_date(),
                input.disabled_date(),
            ]

            plt.figure(figsize=(10, 6))
            plt.title("Selected Dates Visualization")
            plt.scatter(
                selected_dates,
                range(len(selected_dates)),
                marker="o",
                s=100,
                c=range(len(selected_dates)),
                cmap="viridis",
            )
            plt.yticks(
                range(len(selected_dates)),
                [
                    "Basic",
                    "Initial",
                    "Constrained",
                    "Formatted",
                    "International",
                    "Decade View",
                    "Disabled",
                ],
            )
            plt.xlabel("Date")
            plt.xticks(rotation=45)
            return plt.gcf()

    # Table showing selected dates and their properties
    with ui.card(full_screen=True):
        ui.card_header("Selected Dates Details")

        @render.data_frame
        def date_details():
            selected_dates = {
                "Input Type": [
                    "Basic Date",
                    "Initial Date",
                    "Constrained Date",
                    "Formatted Date",
                    "International Date",
                    "Decade View Date",
                    "Disabled Dates Date",
                ],
                "Selected Date": [
                    input.basic_date(),
                    input.initial_date(),
                    input.constrained_date(),
                    input.formatted_date(),
                    input.international_date(),
                    input.decade_view_date(),
                    input.disabled_date(),
                ],
            }
            return pd.DataFrame(selected_dates)
