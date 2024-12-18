import pandas as pd
import numpy as np
from shiny import reactive
from shiny.express import input, ui, render

# Sample data generation
sales_data = pd.DataFrame(
    {
        "date": pd.date_range(start="2023-01-01", end="2023-12-31", freq="D"),
        "revenue": np.random.normal(1000, 200, 365),
        "units": np.random.randint(50, 150, 365),
        "region": np.random.choice(["North", "South", "East", "West"], 365),
    }
)

# Set page options
ui.page_opts(title="Sales Dashboard", fillable=True)

# Create navigation with menu
with ui.navset_pill():
    with ui.nav_menu("Sales Analysis"):
        with ui.nav_panel("Revenue"):

            @render.plot
            def revenue_plot():
                return sales_data.plot(x="date", y="revenue", figsize=(10, 6))

            @render.data_frame
            def revenue_table():
                return (
                    sales_data.groupby("region")["revenue"]
                    .agg(["mean", "sum"])
                    .round(2)
                )

        with ui.nav_panel("Units"):

            @render.plot
            def units_plot():
                return sales_data.plot(x="date", y="units", figsize=(10, 6))

            @render.data_frame
            def units_table():
                return (
                    sales_data.groupby("region")["units"].agg(["mean", "sum"]).round(2)
                )

    with ui.nav_menu("Settings", align="right"):
        with ui.nav_panel("About"):
            ui.markdown(
                """
            ### About this Dashboard
            This is a simple demonstration of nav_menu in Shiny for Python.
            
            The data shown is randomly generated sales data including:
            * Daily revenue
            * Units sold
            * Regional breakdown
            """
            )

        with ui.nav_panel("Help"):
            ui.markdown(
                """
            ### Help Section
            To use this dashboard:
            1. Click on 'Sales Analysis' to view sales data
            2. Choose between Revenue or Units views
            3. Each view shows both a time series plot and summary table
            """
            )
