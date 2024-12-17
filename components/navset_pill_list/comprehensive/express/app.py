import random
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

from shiny import reactive
from shiny.express import input, ui, render
from matplotlib import pyplot as plt

# Generate synthetic data
np.random.seed(42)
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
companies = ["TechCorp", "DataInc", "InnoSoft", "GlobalSys", "FutureTech"]


def generate_financial_data():
    data = {
        "Date": dates,
        "TechCorp": np.cumsum(np.random.normal(0.1, 1, len(dates))),
        "DataInc": np.cumsum(np.random.normal(0.05, 0.8, len(dates))),
        "InnoSoft": np.cumsum(np.random.normal(0.15, 1.2, len(dates))),
        "GlobalSys": np.cumsum(np.random.normal(0.08, 0.7, len(dates))),
        "FutureTech": np.cumsum(np.random.normal(0.12, 0.9, len(dates))),
    }
    return pd.DataFrame(data).set_index("Date")


financial_df = generate_financial_data()

# Page options
ui.page_opts(title="NavSet Pill List Showcase", fillable=True)

# Main NavSet Pill List with various configurations
with ui.navset_pill_list(
    id="stock_nav",  # Unique identifier for the navset
    selected="Performance",  # Default selected panel
    well=True,  # Add a well (gray background) around the navigation list
    widths=(3, 9),  # Customize column widths for nav list and content
):
    with ui.nav_panel("Performance", value="performance"):
        with ui.layout_columns():
            with ui.card(full_screen=True):
                ui.card_header("Stock Performance Overview")

                @render.plot
                def performance_plot():
                    company = input.stock_nav()
                    plt_data = financial_df[company]
                    plt_data.plot(title=f"{company} Stock Performance")
                    plt.xlabel("Date")
                    plt.ylabel("Stock Price")
                    plt.xticks(rotation=45)

            with ui.card():
                ui.card_header("Performance Statistics")

                @render.table
                def performance_stats():
                    company = input.stock_nav()
                    stats = financial_df[company].describe()
                    return stats.reset_index()

    with ui.nav_panel("Volatility", value="volatility"):
        with ui.layout_columns():
            with ui.card():
                ui.card_header("Stock Volatility")

                @render.plot
                def volatility_plot():
                    plt.figure(figsize=(10, 6))
                    financial_df.pct_change().std().plot(kind="bar")
                    plt.title("Stock Volatility Comparison")
                    plt.xlabel("Companies")
                    plt.ylabel("Standard Deviation of Returns")
                    plt.xticks(rotation=45)

    with ui.nav_panel("Correlation", value="correlation"):
        with ui.card():
            ui.card_header("Stock Correlation Matrix")

            @render.plot
            def correlation_plot():
                corr_matrix = financial_df.pct_change().corr()
                plt.figure(figsize=(8, 6))
                plt.imshow(corr_matrix, cmap="coolwarm", aspect="auto")
                plt.colorbar(label="Correlation")
                plt.xticks(
                    range(len(corr_matrix.columns)), corr_matrix.columns, rotation=45
                )
                plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
                plt.title("Stock Return Correlation")

    with ui.nav_panel("About", value="about"):
        ui.markdown(
            """
        ## Stock Analysis Dashboard

        This dashboard provides insights into stock performance using synthetic financial data.

        ### Features:
        - Performance tracking
        - Volatility analysis
        - Correlation matrix
        """
        )

# Optional: Add some interactivity to show the selected nav item
ui.h5("Selected Navigation Item:")


@render.text
def nav_selection():
    return f"Current View: {input.stock_nav()}"
