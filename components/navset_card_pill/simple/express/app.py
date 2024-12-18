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
        "Quarter": [
            "Q1",
            "Q1",
            "Q1",
            "Q1",
            "Q2",
            "Q2",
            "Q2",
            "Q2",
            "Q3",
            "Q3",
            "Q3",
            "Q3",
        ],
        "Sales": np.random.randint(50000, 200000, 12),
    }
)

# Set page options
ui.page_opts(title="Sales Dashboard")

# Create a navset card with pills
with ui.navset_card_pill(id="sales_nav"):
    with ui.nav_panel("Sales by Region"):

        @render.plot
        def region_plot():
            region_sales = sales_data.groupby("Region")["Sales"].sum()
            fig, ax = plt.subplots()
            region_sales.plot(kind="bar", ax=ax)
            ax.set_title("Total Sales by Region")
            ax.set_ylabel("Total Sales")
            return fig

    with ui.nav_panel("Sales by Quarter"):

        @render.plot
        def quarter_plot():
            quarter_sales = sales_data.groupby("Quarter")["Sales"].sum()
            fig, ax = plt.subplots()
            quarter_sales.plot(kind="bar", ax=ax)
            ax.set_title("Total Sales by Quarter")
            ax.set_ylabel("Total Sales")
            return fig

    with ui.nav_panel("Data Table"):

        @render.data_frame
        def sales_table():
            return sales_data
