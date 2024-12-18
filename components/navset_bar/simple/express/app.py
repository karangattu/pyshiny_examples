from shiny import reactive
from shiny.express import input, render, ui
import pandas as pd
import numpy as np

# Generate some sample data
sales_data = pd.DataFrame(
    {
        "date": pd.date_range(start="2023-01-01", end="2023-12-31", freq="D"),
        "revenue": np.random.normal(1000, 100, 365),
        "units": np.random.randint(50, 150, 365),
        "region": np.random.choice(["North", "South", "East", "West"], 365),
    }
)

# Set page options and create navbar
ui.page_opts(title="Sales Dashboard", fillable=True)

with ui.navset_bar(title="Sales Analysis"):

    with ui.nav_panel("Overview"):
        ui.h2("Sales Overview")

        with ui.layout_columns():
            with ui.value_box(theme="primary"):
                "Total Revenue"
                f"${sales_data['revenue'].sum():,.0f}"

            with ui.value_box(theme="success"):
                "Total Units"
                f"{sales_data['units'].sum():,}"

        @render.table
        def sales_table():
            return sales_data.tail(5)

    with ui.nav_panel("By Region"):
        ui.h2("Regional Analysis")

        @render.table
        def region_summary():
            return (
                sales_data.groupby("region")
                .agg({"revenue": ["sum", "mean"], "units": ["sum", "mean"]})
                .round(2)
            )

    with ui.nav_menu("More Info"):
        with ui.nav_panel("About"):
            ui.h3("About this Dashboard")
            "This is a simple sales dashboard built with Shiny for Python."
            "It demonstrates the use of navset_bar in express mode."

        with ui.nav_panel("Help"):
            ui.h3("Help")
            "Use the navigation bar above to switch between different views."
