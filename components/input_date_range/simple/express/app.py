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
        "product": np.random.choice(
            ["Electronics", "Clothing", "Books", "Furniture"], len(date_range)
        ),
        "sales": np.random.randint(100, 1000, len(date_range)),
    }
)

# Shiny App UI and Server Logic
ui.page_opts(title="Sales Data Date Range Filter")

with ui.layout_sidebar():
    with ui.sidebar():
        # Date range input
        ui.input_date_range(
            "date_range",
            "Select Date Range",
            start="2023-01-01",
            end="2023-12-31",
            min="2023-01-01",
            max="2023-12-31",
        )

        # Product category filter
        ui.input_checkbox_group(
            "product_categories",
            "Select Product Categories",
            choices=sales_data["product"].unique().tolist(),
            selected=sales_data["product"].unique().tolist(),
        )

    # Render the filtered data table
    @render.data_frame
    def sales_table():
        # Convert input date range to datetime
        start_date = datetime.combine(input.date_range()[0], datetime.min.time())
        end_date = datetime.combine(input.date_range()[1], datetime.max.time())

        # Filter data based on date range and selected product categories
        filtered_data = sales_data[
            (sales_data["date"] >= start_date)
            & (sales_data["date"] <= end_date)
            & (sales_data["product"].isin(input.product_categories()))
        ]

        return filtered_data

    # Render summary statistics
    @render.text
    def summary_stats():
        # Convert input date range to datetime
        start_date = datetime.combine(input.date_range()[0], datetime.min.time())
        end_date = datetime.combine(input.date_range()[1], datetime.max.time())

        # Filter data based on date range and selected product categories
        filtered_data = sales_data[
            (sales_data["date"] >= start_date)
            & (sales_data["date"] <= end_date)
            & (sales_data["product"].isin(input.product_categories()))
        ]

        total_sales = filtered_data["sales"].sum()
        avg_sales = filtered_data["sales"].mean()

        return (
            f"Total Sales: ${total_sales:,.2f}\nAverage Daily Sales: ${avg_sales:,.2f}"
        )
