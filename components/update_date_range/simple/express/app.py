import pandas as pd
import numpy as np
from datetime import datetime, timedelta

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic sales data
np.random.seed(42)
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
date_range = pd.date_range(start=start_date, end=end_date, freq="D")

sales_data = pd.DataFrame(
    {
        "date": date_range,
        "sales": np.random.randint(100, 1000, size=len(date_range)),
        "category": np.random.choice(
            ["Electronics", "Clothing", "Groceries"], size=len(date_range)
        ),
    }
)

# App UI
ui.page_opts(title="Date Range Update Demo")

with ui.layout_sidebar():
    with ui.sidebar():
        # Initial date range input
        ui.input_date_range(
            "sales_date_range",
            "Select Sales Date Range",
            start="2023-01-01",
            end="2023-12-31",
            min="2023-01-01",
            max="2023-12-31",
        )

        # Buttons to update date range
        ui.input_action_button("update_quarter1", "Q1 (Jan-Mar)")
        ui.input_action_button("update_quarter2", "Q2 (Apr-Jun)")
        ui.input_action_button("update_quarter3", "Q3 (Jul-Sep)")
        ui.input_action_button("update_quarter4", "Q4 (Oct-Dec)")

    # Data table and summary statistics
    @render.data_frame
    def sales_table():
        # Filter data based on selected date range
        filtered_data = sales_data[
            (sales_data["date"] >= pd.to_datetime(input.sales_date_range()[0]))
            & (sales_data["date"] <= pd.to_datetime(input.sales_date_range()[1]))
        ]
        return filtered_data

    @render.text
    def sales_summary():
        filtered_data = sales_data[
            (sales_data["date"] >= pd.to_datetime(input.sales_date_range()[0]))
            & (sales_data["date"] <= pd.to_datetime(input.sales_date_range()[1]))
        ]
        return f"""
        Total Sales: ${filtered_data['sales'].sum():,.2f}
        Average Daily Sales: ${filtered_data['sales'].mean():,.2f}
        Number of Days: {len(filtered_data)}
        """


# Reactive effects to update date range
@reactive.effect
@reactive.event(input.update_quarter1)
def _():
    ui.update_date_range("sales_date_range", start="2023-01-01", end="2023-03-31")


@reactive.effect
@reactive.event(input.update_quarter2)
def _():
    ui.update_date_range("sales_date_range", start="2023-04-01", end="2023-06-30")


@reactive.effect
@reactive.event(input.update_quarter3)
def _():
    ui.update_date_range("sales_date_range", start="2023-07-01", end="2023-09-30")


@reactive.effect
@reactive.event(input.update_quarter4)
def _():
    ui.update_date_range("sales_date_range", start="2023-10-01", end="2023-12-31")
