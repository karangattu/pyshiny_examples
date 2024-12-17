from datetime import date, timedelta
import random
import pandas as pd
import numpy as np

from shiny import reactive
from shiny.express import input, ui, render


# Generate synthetic data
def generate_synthetic_data():
    # Create a date range for the past year
    dates = pd.date_range(start=date(2023, 1, 1), end=date(2023, 12, 31))

    # Generate random sales data
    data = pd.DataFrame(
        {
            "date": dates,
            "sales": np.random.randint(100, 1000, len(dates)),
            "revenue": np.random.uniform(1000, 10000, len(dates)),
        }
    )

    return data


# Create the synthetic dataset
sales_data = generate_synthetic_data()

# Set page options
ui.page_opts(title="Input Date Range Showcase", fillable=True)

# Sidebar with various input_date_range configurations
with ui.sidebar():
    # Basic date range input
    ui.input_date_range(
        "basic_range", "Basic Date Range", start="2023-01-01", end="2023-12-31"
    )

    # Date range with min and max constraints
    ui.input_date_range(
        "constrained_range",
        "Date Range with Constraints",
        start="2023-06-01",
        end="2023-08-31",
        min="2023-01-01",
        max="2023-12-31",
    )

    # Date range with custom format
    ui.input_date_range(
        "custom_format_range",
        "Custom Format Date Range",
        start="2023-01-01",
        end="2023-12-31",
        format="mm/dd/yy",
    )

    # Date range with different language and week start
    ui.input_date_range(
        "international_range",
        "International Date Range",
        start="2023-01-01",
        end="2023-12-31",
        language="de",  # German
        weekstart=1,  # Monday as first day of week
    )

    # Date range with different start view
    ui.input_date_range(
        "decade_view_range",
        "Decade View Date Range",
        start="2023-01-01",
        end="2023-12-31",
        startview="decade",
    )

    # Date range with custom separator
    ui.input_date_range(
        "custom_separator_range",
        "Custom Separator Date Range",
        start="2023-01-01",
        end="2023-12-31",
        separator=" to ",
    )

    # Date range with autoclose disabled
    ui.input_date_range(
        "no_autoclose_range",
        "No Autoclose Date Range",
        start="2023-01-01",
        end="2023-12-31",
        autoclose=False,
    )

# Main content area with results
with ui.layout_columns():
    # Display selected date ranges
    @render.text
    def show_basic_range():
        return f"Basic Range: {input.basic_range()}"

    @render.text
    def show_constrained_range():
        return f"Constrained Range: {input.constrained_range()}"

    @render.text
    def show_custom_format_range():
        return f"Custom Format Range: {input.custom_format_range()}"

    @render.text
    def show_international_range():
        return f"International Range: {input.international_range()}"

    @render.text
    def show_decade_view_range():
        return f"Decade View Range: {input.decade_view_range()}"

    @render.text
    def show_custom_separator_range():
        return f"Custom Separator Range: {input.custom_separator_range()}"

    @render.text
    def show_no_autoclose_range():
        return f"No Autoclose Range: {input.no_autoclose_range()}"

    # Filtered data table based on selected date range
    @render.data_frame
    def filtered_sales_data():
        # Use the basic range for filtering
        start_date = input.basic_range()[0]
        end_date = input.basic_range()[1]

        # Filter the synthetic sales data
        filtered_df = sales_data[
            (sales_data["date"] >= start_date) & (sales_data["date"] <= end_date)
        ]

        return filtered_df
