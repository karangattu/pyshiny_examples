from shiny import reactive
from shiny.express import input, ui, render
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Synthetic data generation
def generate_sales_data(num_records=100):
    """Generate synthetic sales data."""
    regions = ["North", "South", "East", "West", "Central"]
    products = ["Electronics", "Clothing", "Furniture", "Groceries", "Automotive"]

    data = {
        "Region": [random.choice(regions) for _ in range(num_records)],
        "Product": [random.choice(products) for _ in range(num_records)],
        "Sales": np.random.randint(100, 10000, num_records),
        "Profit": np.random.randint(10, 1000, num_records),
    }
    return pd.DataFrame(data)


# Generate dataset
sales_df = generate_sales_data()

# Page setup
ui.page_opts(title="Nav Menu Showcase", fillable=True)

# Add Font Awesome CSS
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.0/css/all.min.css">'
    )
)

# Main Navigation with Nav Menu
with ui.navset_card_pill(id="main_nav"):
    # Nav Menu with multiple configurations
    with ui.nav_menu(
        "Sales Analysis",
        value="sales_menu",  # Unique identifier
        icon=ui.tags.i(class_="fa-solid fa-chart-simple"),  # Font Awesome icon
        align="left",  # Horizontal alignment
    ):
        # Sub Navigation Panels
        with ui.nav_panel("Regional Sales", value="regional"):
            with ui.layout_columns():

                @render.plot
                def regional_sales_plot():
                    plt.figure(figsize=(10, 6))
                    sales_df.groupby("Region")["Sales"].sum().plot(kind="bar")
                    plt.title("Total Sales by Region")
                    plt.xlabel("Region")
                    plt.ylabel("Total Sales")
                    plt.tight_layout()
                    return plt.gcf()

        with ui.nav_panel("Product Sales", value="product"):

            @render.plot
            def product_sales_plot():
                plt.figure(figsize=(10, 6))
                sales_df.groupby("Product")["Sales"].sum().plot(
                    kind="pie", autopct="%1.1f%%"
                )
                plt.title("Sales Distribution by Product")
                plt.tight_layout()
                return plt.gcf()

        with ui.nav_panel("Profit Analysis", value="profit"):

            @render.plot
            def profit_plot():
                plt.figure(figsize=(10, 6))
                sales_df.groupby("Region")["Profit"].mean().plot(kind="bar")
                plt.title("Average Profit by Region")
                plt.xlabel("Region")
                plt.ylabel("Average Profit")
                plt.tight_layout()
                return plt.gcf()

    # Second Nav Menu to demonstrate more features
    with ui.nav_menu(
        "Data Insights",
        value="data_menu",
        icon=ui.tags.i(class_="fa-solid fa-database"),
        align="right",  # Right-aligned menu
    ):
        with ui.nav_panel("Raw Data", value="raw_data"):

            @render.data_frame
            def display_raw_data():
                return sales_df

        with ui.nav_panel("Summary Statistics", value="summary"):

            @render.table
            def summary_stats():
                return sales_df.groupby("Region").agg(
                    {"Sales": ["mean", "sum"], "Profit": ["mean", "sum"]}
                )

    # Spacer in the nav menu (replaced "----" with ui.nav_spacer())
    ui.nav_spacer()

    # Control Nav Panel
    with ui.nav_control():
        ui.input_dark_mode(id="theme_toggle")

# Display selected navigation
ui.h5("Selected Navigation:")


@render.text
def show_selected_nav():
    return f"Main Nav: {input.main_nav()}"
