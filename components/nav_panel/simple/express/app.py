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
        "region": np.random.choice(["North", "South", "East", "West"], 365),
    }
)

# Set page options
ui.page_opts(title="Sales Dashboard", fillable=True)

# Navigation panels
with ui.nav_panel("Overview"):
    ui.h2("Sales Overview")
    with ui.layout_columns(col_widths=[6, 6]):

        @render.plot
        def revenue_plot():
            monthly_revenue = sales_data.groupby(sales_data["date"].dt.month)[
                "revenue"
            ].mean()
            fig, ax = plt.subplots()
            ax.bar(monthly_revenue.index, monthly_revenue.values)
            ax.set_xlabel("Month")
            ax.set_ylabel("Average Revenue")
            return fig

        @render.plot
        def units_plot():
            monthly_units = sales_data.groupby(sales_data["date"].dt.month)[
                "units"
            ].sum()
            fig, ax = plt.subplots()
            ax.plot(monthly_units.index, monthly_units.values, marker="o")
            ax.set_xlabel("Month")
            ax.set_ylabel("Total Units")
            return fig


with ui.nav_panel("Data"):
    ui.input_select(
        "region_filter",
        "Select Region",
        choices=["All"] + list(sales_data["region"].unique()),
    )

    @render.data_frame
    def sales_table():
        if input.region_filter() == "All":
            return sales_data
        return sales_data[sales_data["region"] == input.region_filter()]


with ui.nav_panel("Analysis"):
    ui.h3("Regional Performance")

    @render.table
    def region_summary():
        summary = (
            sales_data.groupby("region")
            .agg({"revenue": ["mean", "sum"], "units": ["mean", "sum"]})
            .round(2)
        )
        summary.columns = ["Avg Revenue", "Total Revenue", "Avg Units", "Total Units"]
        return summary
