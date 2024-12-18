import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
sales_data = pd.DataFrame(
    {
        "Region": ["North", "South", "East", "West"] * 3,
        "Product": ["Gadget", "Widget", "Doohickey"] * 4,
        "Sales": np.random.randint(100, 1000, 12),
    }
)

# Create the Shiny app
ui.page_opts(title="Sales Dashboard")

with ui.navset_tab(id="sales_nav"):
    with ui.nav_panel("Sales Overview"):
        with ui.layout_columns():
            with ui.card():
                ui.card_header("Total Sales by Region")

                @render.plot
                def region_sales():
                    region_totals = sales_data.groupby("Region")["Sales"].sum()
                    fig, ax = plt.subplots()
                    region_totals.plot(kind="bar", ax=ax)
                    plt.title("Total Sales by Region")
                    plt.xlabel("Region")
                    plt.ylabel("Total Sales")
                    plt.tight_layout()
                    return fig

            with ui.card():
                ui.card_header("Sales Distribution")

                @render.plot
                def sales_distribution():
                    fig, ax = plt.subplots()
                    sales_data["Sales"].hist(ax=ax)
                    plt.title("Sales Distribution")
                    plt.xlabel("Sales Amount")
                    plt.ylabel("Frequency")
                    plt.tight_layout()
                    return fig

    with ui.nav_panel("Product Performance"):
        with ui.layout_columns():
            with ui.card():
                ui.card_header("Sales by Product")

                @render.plot
                def product_sales():
                    product_totals = sales_data.groupby("Product")["Sales"].sum()
                    fig, ax = plt.subplots()
                    product_totals.plot(kind="pie", autopct="%1.1f%%", ax=ax)
                    plt.title("Sales Percentage by Product")
                    plt.tight_layout()
                    return fig

            with ui.card():
                ui.card_header("Product Sales Details")

                @render.table
                def product_table():
                    return sales_data.groupby("Product")["Sales"].agg(
                        ["sum", "mean", "max"]
                    )

    with ui.nav_panel("Detailed Data"):

        @render.data_frame
        def full_data_table():
            return sales_data
