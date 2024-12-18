from shiny import reactive
from shiny.express import input, render, ui
import pandas as pd
import numpy as np

# Generate some sample data
np.random.seed(123)
sales_data = pd.DataFrame(
    {
        "Product": ["Widget A", "Widget B", "Widget C", "Widget D"] * 3,
        "Region": ["North", "South", "East", "West"] * 3,
        "Sales": np.random.randint(100, 1000, 12),
        "Quarter": ["Q1", "Q2", "Q3"] * 4,
    }
)

# Set page options
ui.page_opts(title="Sales Dashboard", fillable=True)

# Create a navset card with pills
with ui.navset_card_pill(id="selected_card_pill"):

    # First nav panel for data table
    with ui.nav_panel("Data View"):

        @render.data_frame
        def sales_table():
            return sales_data

    # Second nav panel for summary stats
    with ui.nav_panel("Summary Stats"):

        @render.data_frame
        def summary_stats():
            return pd.DataFrame(
                {
                    "Metric": ["Total Sales", "Average Sale", "Max Sale", "Min Sale"],
                    "Value": [
                        sales_data["Sales"].sum(),
                        round(sales_data["Sales"].mean(), 2),
                        sales_data["Sales"].max(),
                        sales_data["Sales"].min(),
                    ],
                }
            )

    # Third nav panel for filtered view
    with ui.nav_panel("Regional View"):
        ui.input_select(
            "region", "Select Region:", choices=sorted(sales_data["Region"].unique())
        )

        @render.data_frame
        def filtered_data():
            return sales_data[sales_data["Region"] == input.region()]


# Show which panel is currently selected
ui.h5("Selected Panel:")


@render.text
def current_panel():
    return f"Currently viewing: {input.selected_card_pill()}"
