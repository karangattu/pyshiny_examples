from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

from shiny import reactive
from shiny.express import input, ui, render


# Generate synthetic data
def generate_sales_data(num_records=100):
    """Generate synthetic sales data."""
    products = ["Laptop", "Smartphone", "Tablet", "Smartwatch", "Headphones"]
    regions = ["North", "South", "East", "West", "Central"]

    data = {
        "Date": [datetime.now() - timedelta(days=x) for x in range(num_records)],
        "Product": [random.choice(products) for _ in range(num_records)],
        "Region": [random.choice(regions) for _ in range(num_records)],
        "Sales": np.random.randint(100, 1000, num_records),
        "Revenue": np.random.uniform(1000, 10000, num_records),
    }

    return pd.DataFrame(data)


# Generate synthetic data
sales_df = generate_sales_data()

# Page options
ui.page_opts(title="Nav Panel Showcase", fillable=True)

# Add Font Awesome CSS
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">'
    )
)

# Main Navigation Set
with ui.navset_card_tab(id="main_nav"):
    # Nav Panel with basic text and icon
    with ui.nav_panel("Overview", icon=ui.tags.i(class_="fa-solid fa-chart-simple")):
        ui.markdown("## Sales Dashboard Overview")
        ui.p("This dashboard provides insights into our sales performance.")

    # Nav Panel with a table
    with ui.nav_panel("Sales Data", icon=ui.tags.i(class_="fa-solid fa-table")):

        @render.data_frame
        def sales_table():
            return sales_df

    # Nav Panel with a plot
    with ui.nav_panel(
        "Sales by Product", icon=ui.tags.i(class_="fa-solid fa-chart-bar")
    ):
        with ui.layout_sidebar():
            with ui.sidebar():
                # Convert numpy array to list for choices
                ui.input_select(
                    "product_select",
                    "Select Product",
                    choices=sales_df["Product"].unique().tolist(),
                )

            @render.plot
            def product_sales_plot():
                product_data = sales_df[sales_df["Product"] == input.product_select()]
                plt.figure(figsize=(10, 6))
                plt.bar(product_data["Date"], product_data["Sales"])
                plt.title(f"Sales for {input.product_select()}")
                plt.xlabel("Date")
                plt.ylabel("Sales")
                plt.xticks(rotation=45)
                return plt.gcf()

    # Nav Panel with a value box
    with ui.nav_panel("KPIs", icon=ui.tags.i(class_="fa-solid fa-chart-pie")):
        with ui.layout_columns():
            with ui.value_box(
                showcase=ui.tags.i(class_="fa-solid fa-dollar-sign"),
                theme="bg-gradient-blue-purple",
            ):
                "Total Revenue"
                f"${sales_df['Revenue'].sum():.2f}"
                "Across all products and regions"

            with ui.value_box(
                showcase=ui.tags.i(class_="fa-solid fa-shopping-cart"),
                theme="bg-gradient-green-teal",
            ):
                "Total Sales"
                f"{sales_df['Sales'].sum()}"
                "Number of units sold"

    # Nav Panel with a conditional panel
    with ui.nav_panel("Advanced Filters", icon=ui.tags.i(class_="fa-solid fa-filter")):
        with ui.layout_sidebar():
            with ui.sidebar():
                # Convert numpy array to list for choices
                ui.input_select(
                    "region_select",
                    "Select Region",
                    choices=sales_df["Region"].unique().tolist(),
                    multiple=True,
                )

            @render.data_frame
            def filtered_sales():
                df = sales_df.copy()
                if input.region_select():
                    df = df[df["Region"].isin(input.region_select())]
                return df

    # Nav Panel with markdown and code
    with ui.nav_panel("Documentation", icon=ui.tags.i(class_="fa-solid fa-book")):
        ui.markdown(
            """
        ## Nav Panel Documentation

        This dashboard demonstrates the versatility of Shiny's `nav_panel` component.

        ### Features Demonstrated:
        - Basic text and icon usage
        - Data tables
        - Interactive plots
        - Value boxes
        - Conditional filtering
        """
        )

        ui.code(
            """
        # Example of creating a nav panel
        with ui.nav_panel("Panel Name", icon=ui.tags.i(class_="fa-solid fa-icon")):
            # Panel content goes here
        """
        )

# Add a footer with current timestamp
ui.tags.footer(
    f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
    class_="text-center text-muted mt-3",
)
