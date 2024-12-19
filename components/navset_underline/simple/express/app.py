import pandas as pd
import numpy as np
from shiny import reactive
from shiny.express import input, render, ui

# Generate some sample data
np.random.seed(123)
sales_data = pd.DataFrame(
    {
        "date": pd.date_range(start="2023-01-01", periods=100, freq="D"),
        "sales": np.random.normal(1000, 200, 100).round(2),
        "region": np.random.choice(["North", "South", "East", "West"], 100),
    }
)

# Set page options
ui.page_opts(title="Sales Dashboard", fillable=True)

# Create navigation with underlined tabs
with ui.navset_underline(id="nav"):
    with ui.nav_panel("Overview"):
        with ui.layout_sidebar():
            with ui.sidebar():
                ui.input_select(
                    "region",
                    "Select Region",
                    choices=["All"] + list(sales_data["region"].unique()),
                )
                ui.input_date_range(
                    "date_range",
                    "Select Date Range",
                    start="2023-01-01",
                    end="2023-04-10",
                )

            @render.table
            def sales_table():
                df = sales_data.copy()
                if input.region() != "All":
                    df = df[df["region"] == input.region()]

                start_date = pd.to_datetime(input.date_range()[0])
                end_date = pd.to_datetime(input.date_range()[1])
                df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
                return df

    with ui.nav_panel("Summary Stats"):

        @render.text
        def summary_stats():
            df = sales_data.copy()
            if input.region() != "All":
                df = df[df["region"] == input.region()]

            start_date = pd.to_datetime(input.date_range()[0])
            end_date = pd.to_datetime(input.date_range()[1])
            df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

            stats = f"""
            Sales Statistics:
            ----------------
            Total Sales: ${df['sales'].sum():,.2f}
            Average Daily Sales: ${df['sales'].mean():,.2f}
            Minimum Daily Sales: ${df['sales'].min():,.2f}
            Maximum Daily Sales: ${df['sales'].max():,.2f}
            Number of Days: {len(df)}
            """
            return stats

    with ui.nav_panel("About"):
        ui.markdown(
            """
        ### Sales Dashboard
        
        This is a simple demonstration of the `navset_underline` component in Shiny for Python.
        
        Features:
        - Data filtering by region and date range
        - Summary statistics
        - Tabular data view
        
        The data shown is randomly generated for demonstration purposes.
        """
        )
