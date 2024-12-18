import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="M")
sales_data = pd.DataFrame(
    {
        "Date": dates,
        "Region": np.random.choice(["North", "South", "East", "West"], size=len(dates)),
        "Sales": np.random.randint(50000, 200000, size=len(dates)),
        "Profit": np.random.randint(10000, 50000, size=len(dates)),
    }
)

# Set page options
ui.page_opts(title="NavSet Card Tab Showcase", fillable=True)

# Create a sidebar for interactive controls
with ui.sidebar():
    ui.input_select(
        "region",
        "Select Region",
        choices=["All"] + list(sales_data["Region"].unique()),
        selected="All",
    )
    ui.input_checkbox_group(
        "metrics",
        "Select Metrics",
        choices=["Sales", "Profit"],
        selected=["Sales", "Profit"],
    )

# Main NavSet Card Tab with various parameters
with ui.navset_card_tab(
    id="main_navset",  # Adding an ID for reactive tracking
    selected="Sales Overview",  # Default selected tab
    title="Sales Dashboard",  # Optional title
):
    # Sales Overview Tab
    with ui.nav_panel("Sales Overview", value="sales_overview"):

        @render.plot
        def sales_plot():
            filtered_data = sales_data.copy()
            if input.region() != "All":
                filtered_data = filtered_data[filtered_data["Region"] == input.region()]

            plt.figure(figsize=(10, 6))
            if "Sales" in input.metrics():
                plt.plot(
                    filtered_data["Date"],
                    filtered_data["Sales"],
                    label="Sales",
                    marker="o",
                )
            if "Profit" in input.metrics():
                plt.plot(
                    filtered_data["Date"],
                    filtered_data["Profit"],
                    label="Profit",
                    marker="s",
                )

            plt.title(f"Sales and Profit Trends ({input.region()} Region)")
            plt.xlabel("Date")
            plt.ylabel("Amount")
            plt.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()
            return plt.gcf()

    # Regional Breakdown Tab
    with ui.nav_panel("Regional Breakdown", value="regional_breakdown"):

        @render.data_frame
        def regional_summary():
            filtered_data = sales_data.copy()
            if input.region() != "All":
                filtered_data = filtered_data[filtered_data["Region"] == input.region()]

            summary = filtered_data.groupby("Region")[["Sales", "Profit"]].sum()
            return summary

    # Detailed Data Tab
    with ui.nav_panel("Detailed Data", value="detailed_data"):

        @render.data_frame
        def full_data_table():
            filtered_data = sales_data.copy()
            if input.region() != "All":
                filtered_data = filtered_data[filtered_data["Region"] == input.region()]

            return filtered_data

    # Performance Metrics Tab
    with ui.nav_panel("Performance Metrics", value="performance_metrics"):

        @render.ui
        def performance_summary():
            filtered_data = sales_data.copy()
            if input.region() != "All":
                filtered_data = filtered_data[filtered_data["Region"] == input.region()]

            total_sales = filtered_data["Sales"].sum()
            total_profit = filtered_data["Profit"].sum()
            avg_monthly_sales = filtered_data["Sales"].mean()
            avg_monthly_profit = filtered_data["Profit"].mean()

            return ui.div(
                ui.h4("Performance Metrics"),
                ui.tags.ul(
                    ui.tags.li(f"Total Sales: ${total_sales:,.2f}"),
                    ui.tags.li(f"Total Profit: ${total_profit:,.2f}"),
                    ui.tags.li(f"Average Monthly Sales: ${avg_monthly_sales:,.2f}"),
                    ui.tags.li(f"Average Monthly Profit: ${avg_monthly_profit:,.2f}"),
                ),
            )


# Footer for additional context
ui.markdown("### Sales Dashboard using NavSet Card Tab")


# Reactive display of selected tab
@render.text
def selected_tab():
    return f"Currently selected tab: {input.main_navset()}"
