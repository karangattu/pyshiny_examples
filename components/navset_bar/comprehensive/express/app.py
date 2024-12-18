import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
sales_data = pd.DataFrame(
    {
        "Date": dates,
        "Product A": np.random.randint(100, 1000, len(dates)),
        "Product B": np.random.randint(100, 1000, len(dates)),
        "Product C": np.random.randint(100, 1000, len(dates)),
    }
)

# Set page options with a title
ui.page_opts(title="NavSet Bar Demo", fillable=True)

# Add Font Awesome CSS for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">'
    )
)

# Create NavSet Bar with comprehensive parameters
with ui.navset_bar(
    title="Sales Dashboard",
    id="sales_dashboard",  # Allows tracking of selected nav item
    selected="overview",  # Default selected panel
    header=ui.tags.div(
        ui.tags.h4("Sales Performance Metrics"),
        ui.tags.p("Explore sales data across different products and time periods."),
    ),
    footer=ui.tags.div(ui.tags.small("© 2023 Sales Analytics Dashboard")),
    bg="primary",  # Background color
    inverse=False,  # Text color (dark in this case)
    underline=True,  # Underline active nav item
    collapsible=True,  # Collapse on mobile
    fluid=True,  # Use fluid layout
):
    # Sidebar (moved outside of navset_bar parameters)
    with ui.sidebar():
        ui.input_date_range(
            "date_range", "Select Date Range", start="2023-01-01", end="2023-12-31"
        ),
        ui.input_checkbox_group(
            "products",
            "Select Products",
            ["Product A", "Product B", "Product C"],
            selected=["Product A", "Product B", "Product C"],
        )

    # Overview Panel
    with ui.nav_panel(
        "Overview", value="overview", icon=ui.tags.i(class_="fa-solid fa-chart-pie")
    ):
        with ui.layout_columns():
            with ui.card():
                ui.card_header("Total Sales by Product")

                @render.plot
                def total_sales_plot():
                    filtered_data = sales_data[
                        (sales_data["Date"] >= pd.to_datetime(input.date_range()[0]))
                        & (sales_data["Date"] <= pd.to_datetime(input.date_range()[1]))
                    ]
                    products = input.products()

                    plt.figure(figsize=(10, 6))
                    plt.bar(products, [filtered_data[prod].sum() for prod in products])
                    plt.title("Total Sales by Product")
                    plt.xlabel("Products")
                    plt.ylabel("Total Sales")
                    return plt.gcf()

    # Trends Panel
    with ui.nav_panel(
        "Trends", value="trends", icon=ui.tags.i(class_="fa-solid fa-line-chart")
    ):
        with ui.card():
            ui.card_header("Sales Trends")

            @render.plot
            def sales_trends_plot():
                filtered_data = sales_data[
                    (sales_data["Date"] >= pd.to_datetime(input.date_range()[0]))
                    & (sales_data["Date"] <= pd.to_datetime(input.date_range()[1]))
                ]
                plt.figure(figsize=(12, 6))
                for prod in input.products():
                    plt.plot(filtered_data["Date"], filtered_data[prod], label=prod)
                plt.title("Sales Trends")
                plt.xlabel("Date")
                plt.ylabel("Sales")
                plt.legend()
                return plt.gcf()

    # Comparative Panel
    with ui.nav_panel(
        "Comparative",
        value="comparative",
        icon=ui.tags.i(class_="fa-solid fa-chart-bar"),
    ):
        with ui.card():
            ui.card_header("Product Comparison")

            @render.data_frame
            def product_comparison():
                filtered_data = sales_data[
                    (sales_data["Date"] >= pd.to_datetime(input.date_range()[0]))
                    & (sales_data["Date"] <= pd.to_datetime(input.date_range()[1]))
                ]
                comparison_df = pd.DataFrame(
                    {
                        "Product": input.products(),
                        "Total Sales": [
                            filtered_data[prod].sum() for prod in input.products()
                        ],
                        "Average Sales": [
                            filtered_data[prod].mean() for prod in input.products()
                        ],
                        "Max Sales": [
                            filtered_data[prod].max() for prod in input.products()
                        ],
                    }
                )
                return comparison_df

    # Other Links Menu
    with ui.nav_menu("More", icon=ui.tags.i(class_="fa-solid fa-ellipsis")):
        with ui.nav_panel("About", value="about"):
            ui.markdown(
                """
            ### Sales Dashboard
            
            This interactive dashboard allows you to:
            - View total sales by product
            - Analyze sales trends
            - Compare product performance
            """
            )

        with ui.nav_control():
            ui.a("Export Data", href="#", class_="dropdown-item")
            ui.a("Help", href="#", class_="dropdown-item")

# Display the currently selected nav item
ui.h5("Selected Navigation Item:")


@render.text
def selected_nav():
    return f"Current selection: {input.sales_dashboard()}"
