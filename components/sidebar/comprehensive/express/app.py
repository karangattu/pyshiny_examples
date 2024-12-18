from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
sales_data = pd.DataFrame(
    {
        "date": dates,
        "region": np.random.choice(["North", "South", "East", "West"], len(dates)),
        "sales": np.random.randint(100, 1000, len(dates)),
        "product_category": np.random.choice(
            ["Electronics", "Clothing", "Furniture", "Groceries"], len(dates)
        ),
    }
)

# Page options
ui.page_opts(title="Sidebar Showcase", fillable=True)

# Sidebar with multiple configurations
with ui.sidebar(
    id="demo_sidebar",  # Adding an id for reactivity
    title="Sidebar Configurations",  # Custom title
    position="left",  # Sidebar position
    width=250,  # Sidebar width
    open={"desktop": "open", "mobile": "closed"},  # Open state configuration
    bg="light",  # Background color
    class_="custom-sidebar",  # Additional CSS class
    padding=[10, 15, 10, 15],  # Padding [top, right, bottom, left]
):
    # Sidebar content with various input types
    ui.input_dark_mode(id="dark_mode")  # Dark mode toggle

    ui.input_select(
        "region",
        "Select Region",
        choices=["All"] + list(sales_data["region"].unique()),
        multiple=True,
    )

    ui.input_checkbox_group(
        "product_categories",
        "Product Categories",
        choices=list(sales_data["product_category"].unique()),
        selected=list(sales_data["product_category"].unique()),
    )

    ui.input_date_range(
        "date_range",
        "Date Range",
        start=sales_data["date"].min(),
        end=sales_data["date"].max(),
    )

    ui.input_slider(
        "sales_range",
        "Sales Range",
        min=sales_data["sales"].min(),
        max=sales_data["sales"].max(),
        value=[sales_data["sales"].min(), sales_data["sales"].max()],
    )

    # Conditional panel demonstrating dynamic UI
    with ui.panel_conditional("input.region.length > 0"):
        ui.markdown("### Region Details")
        ui.input_action_button("show_region_details", "Show Region Details")

# Main content area
with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Sales Overview")

        @render.plot
        def sales_plot():
            # Filter data based on sidebar inputs
            filtered_data = sales_data.copy()

            if input.region() and "All" not in input.region():
                filtered_data = filtered_data[
                    filtered_data["region"].isin(input.region())
                ]

            if input.product_categories():
                filtered_data = filtered_data[
                    filtered_data["product_category"].isin(input.product_categories())
                ]

            # Date range filter
            start_date = datetime.combine(input.date_range()[0], datetime.min.time())
            end_date = datetime.combine(input.date_range()[1], datetime.min.time())
            filtered_data = filtered_data[
                (filtered_data["date"] >= start_date)
                & (filtered_data["date"] <= end_date)
            ]

            # Sales range filter
            filtered_data = filtered_data[
                (filtered_data["sales"] >= input.sales_range()[0])
                & (filtered_data["sales"] <= input.sales_range()[1])
            ]

            # Plot
            plt.figure(figsize=(10, 6))
            filtered_data.groupby("date")["sales"].sum().plot(title="Daily Sales")
            plt.xlabel("Date")
            plt.ylabel("Sales")
            plt.xticks(rotation=45)
            plt.tight_layout()
            return plt.gcf()

    with ui.card(full_screen=True):
        ui.card_header("Sales Summary")

        @render.data_frame
        def sales_summary():
            filtered_data = sales_data.copy()

            if input.region() and "All" not in input.region():
                filtered_data = filtered_data[
                    filtered_data["region"].isin(input.region())
                ]

            if input.product_categories():
                filtered_data = filtered_data[
                    filtered_data["product_category"].isin(input.product_categories())
                ]

            # Date range filter
            start_date = datetime.combine(input.date_range()[0], datetime.min.time())
            end_date = datetime.combine(input.date_range()[1], datetime.min.time())
            filtered_data = filtered_data[
                (filtered_data["date"] >= start_date)
                & (filtered_data["date"] <= end_date)
            ]

            # Sales range filter
            filtered_data = filtered_data[
                (filtered_data["sales"] >= input.sales_range()[0])
                & (filtered_data["sales"] <= input.sales_range()[1])
            ]

            return (
                filtered_data.groupby(["region", "product_category"])["sales"]
                .agg(["sum", "mean", "count"])
                .reset_index()
            )


# Reactive effect for region details
@reactive.effect
@reactive.event(input.show_region_details)
def _():
    if input.region() and "All" not in input.region():
        ui.modal_show(
            ui.modal(
                *[
                    ui.p(f"Region {region}: Detailed information")
                    for region in input.region()
                ],
                title="Region Details",
                footer=ui.modal_button("Close"),
            )
        )
    else:
        ui.notification_show("Please select specific regions", type="warning")
