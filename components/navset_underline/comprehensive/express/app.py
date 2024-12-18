from shiny import reactive
from shiny.express import input, render, ui
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
sales_data = pd.DataFrame(
    {
        "Region": ["North", "South", "East", "West", "Central"],
        "Q1_Sales": np.random.randint(100000, 500000, 5),
        "Q2_Sales": np.random.randint(100000, 500000, 5),
        "Q3_Sales": np.random.randint(100000, 500000, 5),
        "Q4_Sales": np.random.randint(100000, 500000, 5),
    }
)

product_data = pd.DataFrame(
    {
        "Product": ["Laptop", "Smartphone", "Tablet", "Smartwatch", "Desktop"],
        "Units_Sold": np.random.randint(1000, 10000, 5),
        "Revenue": np.random.randint(500000, 2000000, 5),
    }
)

# Page options
ui.page_opts(title="NavSet Underline Demo", fillable=True)

# NavSet Underline with various parameters
with ui.navset_underline(
    id="main_navset",  # Unique identifier for the navset
    selected="Sales",  # Initially selected tab
    header=ui.markdown("## Sales and Product Performance Dashboard"),  # Optional header
    footer=ui.p("Data as of: 2023 Q4", class_="text-muted"),  # Optional footer
):
    # Sales Panel
    with ui.nav_panel("Sales", value="sales_panel"):
        with ui.layout_columns():
            with ui.card():
                ui.card_header("Quarterly Sales by Region")

                @render.plot
                def sales_plot():
                    plt.figure(figsize=(10, 6))
                    sales_data.plot(
                        x="Region",
                        y=["Q1_Sales", "Q2_Sales", "Q3_Sales", "Q4_Sales"],
                        kind="bar",
                    )
                    plt.title("Regional Sales Performance")
                    plt.xlabel("Region")
                    plt.ylabel("Sales ($)")
                    plt.tight_layout()
                    return plt.gcf()

            with ui.card():
                ui.card_header("Sales Data Table")

                @render.data_frame
                def sales_table():
                    return sales_data

    # Products Panel
    with ui.nav_panel("Products", value="products_panel"):
        with ui.layout_columns():
            with ui.card():
                ui.card_header("Product Sales Overview")

                @render.plot
                def product_plot():
                    plt.figure(figsize=(10, 6))
                    product_data.plot(x="Product", y="Units_Sold", kind="bar")
                    plt.title("Product Units Sold")
                    plt.xlabel("Product")
                    plt.ylabel("Units")
                    plt.tight_layout()
                    return plt.gcf()

            with ui.card():
                ui.card_header("Product Details")

                @render.data_frame
                def product_table():
                    return product_data

    # Analysis Panel
    with ui.nav_panel("Analysis", value="analysis_panel"):
        with ui.card():
            ui.card_header("Performance Insights")
            ui.markdown(
                """
            ### Key Observations
            - Regional sales show variation across quarters
            - Product performance differs by units sold and revenue
            - Detailed analysis available in respective tabs
            """
            )

    # Additional Navigation Menu
    with ui.nav_menu("More Options"):
        with ui.nav_panel("About"):
            ui.markdown(
                """
            ## Dashboard Information
            - Created using Shiny for Python
            - Demonstrates NavSet Underline features
            - Synthetic data for demonstration
            """
            )

        with ui.nav_panel("Contact"):
            ui.markdown(
                """
            ## Contact Information
            - Dashboard created by: Your Name
            - Email: example@company.com
            - Version: 1.0.0
            """
            )


# Optional: Render the currently selected navigation tab
@render.text
def current_tab():
    return f"Current Tab: {input.main_navset()}"
