import pandas as pd
import numpy as np
from shiny import reactive
from shiny.express import input, ui, render

# Generate some synthetic data
np.random.seed(123)
sales_data = pd.DataFrame(
    {
        "date": pd.date_range(start="2023-01-01", periods=100, freq="D"),
        "revenue": np.random.normal(1000, 100, 100).round(2),
        "units": np.random.randint(50, 150, 100),
        "region": np.random.choice(["North", "South", "East", "West"], 100),
    }
)

# Set page options
ui.page_opts(title="Sales Dashboard", fillable=True)

# Create navset with underlined tabs
with ui.navset_card_underline(id="nav"):
    with ui.nav_panel("Overview"):
        ui.h3("Sales Overview")

        @render.table
        def sales_summary():
            return (
                sales_data.groupby("region")
                .agg({"revenue": ["mean", "sum"], "units": ["mean", "sum"]})
                .round(2)
            )

    with ui.nav_panel("Revenue Trends"):
        ui.input_selectize(
            "region_select",
            "Select Region",
            choices=["All"] + list(sales_data["region"].unique()),
        )

        @render.table
        def revenue_table():
            df = sales_data.copy()
            if input.region_select() != "All":
                df = df[df["region"] == input.region_select()]
            return df.tail(5)[["date", "revenue", "region"]]

    with ui.nav_panel("Unit Sales"):
        ui.h3("Units Sold by Region")

        @render.table
        def units_table():
            return sales_data.pivot_table(
                values="units", index="region", aggfunc=["sum", "mean", "min", "max"]
            ).round(2)
