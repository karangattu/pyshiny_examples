import pandas as pd
import numpy as np
from datetime import date, timedelta

from shiny import reactive
from shiny.express import input, ui, render
from matplotlib import pyplot as plt

# Generate synthetic data
np.random.seed(42)
start_date = date(2023, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(365)]
sales = np.random.randint(100, 1000, size=len(dates))

df = pd.DataFrame({"date": dates, "sales": sales})

# Shiny App
ui.page_opts(title="Date Input Demo")

with ui.layout_sidebar():
    with ui.sidebar():
        # Demonstrate various input_date features
        ui.input_date(
            "selected_date",
            "Select a Date",
            value=date(2023, 6, 15),  # Default selected date
            min=date(2023, 1, 1),  # Minimum allowed date
            max=date(2023, 12, 31),  # Maximum allowed date
            format="mm/dd/yy",  # Custom date format
            language="en",  # Language for date picker
            startview="month",  # Start view of the date picker
        )

    # Render outputs based on selected date
    with ui.card():
        ui.card_header("Sales Information")

        @render.text
        def sales_text():
            selected_date = input.selected_date()
            matching_row = df[df["date"] == selected_date]

            if not matching_row.empty:
                return f"Sales on {selected_date}: ${matching_row['sales'].values[0]:,}"
            else:
                return "No sales data for this date"

        @render.plot
        def sales_plot():
            selected_date = input.selected_date()

            # Create a window of dates around the selected date
            window_start = selected_date - timedelta(days=30)
            window_end = selected_date + timedelta(days=30)

            window_df = df[(df["date"] >= window_start) & (df["date"] <= window_end)]

            plt.figure(figsize=(10, 4))
            plt.plot(window_df["date"], window_df["sales"], marker="o")
            plt.title(f"Sales Around {selected_date}")
            plt.xlabel("Date")
            plt.ylabel("Sales")
            plt.xticks(rotation=45)
            plt.tight_layout()
            return plt.gcf()
