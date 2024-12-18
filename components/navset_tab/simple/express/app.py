import pandas as pd
import numpy as np
from shiny import reactive
from shiny.express import input, render, ui

# Generate some synthetic data
np.random.seed(123)
sales_data = pd.DataFrame(
    {
        "date": pd.date_range(start="2023-01-01", periods=100, freq="D"),
        "revenue": np.random.normal(1000, 200, 100).round(2),
        "units": np.random.randint(50, 150, 100),
        "region": np.random.choice(["North", "South", "East", "West"], 100),
    }
)

# Set page options
ui.page_opts(title="Sales Dashboard", fillable=True)

# Create tabset with navigation
with ui.navset_tab(id="tabs"):

    with ui.nav_panel("Overview"):
        ui.h2("Sales Overview")

        @render.table
        def sales_summary():
            summary = (
                sales_data.groupby("region")
                .agg({"revenue": ["mean", "sum"], "units": ["mean", "sum"]})
                .round(2)
            )
            summary.columns = [
                "Avg Revenue",
                "Total Revenue",
                "Avg Units",
                "Total Units",
            ]
            return summary

    with ui.nav_panel("Data Table"):
        ui.h2("Raw Data")

        with ui.layout_sidebar():
            with ui.sidebar():
                ui.input_select(
                    "region_filter",
                    "Select Region",
                    choices=["All"] + list(sales_data["region"].unique()),
                )

            @render.data_frame
            def filtered_data():
                if input.region_filter() == "All":
                    return sales_data
                return sales_data[sales_data["region"] == input.region_filter()]

    with ui.nav_panel("Statistics"):
        ui.h2("Statistical Summary")

        @render.table
        def stats_summary():
            stats = sales_data.describe().round(2)
            return stats[["revenue", "units"]]
