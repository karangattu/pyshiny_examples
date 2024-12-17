from shiny import reactive, render
from shiny.express import input, ui
import random
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


# Synthetic data generation
def generate_sales_data(num_entries=50):
    """Generate synthetic sales data."""
    regions = ["North", "South", "East", "West", "Central"]
    products = ["Electronics", "Clothing", "Furniture", "Groceries", "Automotive"]

    data = {
        "Date": [
            datetime.now() - timedelta(days=random.randint(1, 365))
            for _ in range(num_entries)
        ],
        "Region": [random.choice(regions) for _ in range(num_entries)],
        "Product": [random.choice(products) for _ in range(num_entries)],
        "Sales": np.random.randint(100, 10000, num_entries),
        "Profit": np.random.uniform(10, 1000, num_entries),
    }

    return pd.DataFrame(data)


# Global dataset
sales_df = generate_sales_data()

# Page setup
ui.page_opts(title="Accordion Showcase", fillable=True)

# Add Font Awesome for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">'
    )
)

# Main Accordion Demonstration
with ui.accordion(
    id="main_accordion", multiple=True, open=["Sales Overview", "Data Filters"]
):
    # Panel 1: Sales Overview
    with ui.accordion_panel(
        "Sales Overview", icon=ui.tags.i(class_="fa-solid fa-chart-simple")
    ):
        ui.markdown("### Total Sales by Region")

        @render.data_frame
        def regional_sales():
            return sales_df.groupby("Region")["Sales"].sum().reset_index()

    # Panel 2: Data Filters
    with ui.accordion_panel(
        "Data Filters", icon=ui.tags.i(class_="fa-solid fa-filter")
    ):
        ui.input_select(
            "region_select",
            "Select Region",
            choices=["All"] + list(sales_df["Region"].unique()),
        )
        ui.input_select(
            "product_select",
            "Select Product",
            choices=["All"] + list(sales_df["Product"].unique()),
        )

    # Panel 3: Filtered Data
    with ui.accordion_panel(
        "Filtered Data", icon=ui.tags.i(class_="fa-solid fa-table")
    ):

        @render.data_frame
        def filtered_data():
            df = sales_df.copy()

            if input.region_select() != "All":
                df = df[df["Region"] == input.region_select()]

            if input.product_select() != "All":
                df = df[df["Product"] == input.product_select()]

            return df

    # Panel 4: Visualization
    with ui.accordion_panel(
        "Sales Visualization", icon=ui.tags.i(class_="fa-solid fa-chart-bar")
    ):

        @render.plot
        def sales_plot():
            df = sales_df.copy()

            if input.region_select() != "All":
                df = df[df["Region"] == input.region_select()]

            if input.product_select() != "All":
                df = df[df["Product"] == input.product_select()]

            plt.figure(figsize=(10, 6))
            df.groupby("Product")["Sales"].sum().plot(kind="bar")
            plt.title("Sales by Product")
            plt.xlabel("Product")
            plt.ylabel("Total Sales")
            plt.xticks(rotation=45)
            plt.tight_layout()
            return plt.gcf()


# Accordion State Information
ui.h4("Accordion State")


@render.text
def accordion_state():
    return f"Current Open Panels: {input.main_accordion()}"


# Add a button to reset accordion
ui.input_action_button("reset_accordion", "Reset Accordion")


@reactive.effect
@reactive.event(input.reset_accordion)
def _():
    ui.update_accordion("main_accordion", show=["Sales Overview", "Data Filters"])
