import pandas as pd
import numpy as np
from shiny import reactive
from shiny.express import input, ui, render

# Generate some synthetic data
np.random.seed(123)
sales_data = pd.DataFrame(
    {
        "date": pd.date_range(start="2023-01-01", end="2023-12-31", freq="D"),
        "revenue": np.random.normal(1000, 200, 365),
        "units": np.random.randint(50, 150, 365),
        "category": np.random.choice(["Electronics", "Clothing", "Food"], 365),
    }
)

# Set page options
ui.page_opts(title="Sales Dashboard", fillable=True)

# Create navset card tab layout
with ui.navset_card_tab(id="tabset"):

    # Overview Tab
    with ui.nav_panel("Overview"):
        ui.h3("Sales Overview")

        @render.data_frame
        def sales_summary():
            summary = (
                sales_data.groupby("category")
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

    # Details Tab
    with ui.nav_panel("Details"):
        ui.input_select(
            "category",
            "Select Category",
            choices=["All"] + list(sales_data["category"].unique()),
        )

        @render.data_frame
        def filtered_data():
            if input.category() == "All":
                return sales_data
            return sales_data[sales_data["category"] == input.category()]

    # Statistics Tab
    with ui.nav_panel("Statistics"):
        ui.h3("Statistical Summary")

        @render.data_frame
        def stats_summary():
            stats = sales_data.describe().round(2)
            return stats[["revenue", "units"]]
