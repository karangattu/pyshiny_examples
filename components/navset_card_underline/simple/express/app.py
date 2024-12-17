import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render

# Synthetic data generation
np.random.seed(42)
sales_data = pd.DataFrame(
    {
        "Region": ["North", "South", "East", "West"],
        "Q1 Sales": np.random.randint(100000, 500000, 4),
        "Q2 Sales": np.random.randint(100000, 500000, 4),
        "Q3 Sales": np.random.randint(100000, 500000, 4),
        "Q4 Sales": np.random.randint(100000, 500000, 4),
    }
)

# Page options
ui.page_opts(title="Sales Dashboard")

# Navigation set with card underline
with ui.navset_card_underline(id="sales_nav"):
    with ui.nav_panel("Sales Overview"):

        @render.table
        def sales_table():
            return sales_data

    with ui.nav_panel("Quarterly Trends"):

        @render.plot
        def sales_trend():
            plt.figure(figsize=(10, 6))
            sales_data.plot(
                x="Region",
                y=["Q1 Sales", "Q2 Sales", "Q3 Sales", "Q4 Sales"],
                kind="bar",
            )
            plt.title("Quarterly Sales by Region")
            plt.xlabel("Region")
            plt.ylabel("Sales Amount")
            plt.tight_layout()
            return plt.gcf()

    with ui.nav_panel("Performance Metrics"):

        @render.ui
        def performance_metrics():
            total_sales = (
                sales_data[["Q1 Sales", "Q2 Sales", "Q3 Sales", "Q4 Sales"]].sum().sum()
            )
            avg_quarterly_sales = total_sales / 4

            return ui.div(
                ui.h4("Annual Performance"),
                ui.tags.ul(
                    ui.tags.li(f"Total Annual Sales: ${total_sales:,.2f}"),
                    ui.tags.li(f"Average Quarterly Sales: ${avg_quarterly_sales:,.2f}"),
                ),
            )


# Sidebar for additional interaction
with ui.sidebar():
    ui.input_select(
        "region_filter",
        "Select Region",
        choices=["All"] + list(sales_data["Region"]),
        selected="All",
    )


# Render a reactive text showing selected region
@render.text
def region_selection():
    return f"Selected Region: {input.region_filter()}"
