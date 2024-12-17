from shiny import reactive
from shiny.express import input, ui, render
import random
import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
data_types = {
    "sales": pd.DataFrame(
        {
            "product": ["A", "B", "C", "D", "E"],
            "revenue": np.random.randint(1000, 5000, 5),
            "units_sold": np.random.randint(100, 500, 5),
        }
    ),
    "customers": pd.DataFrame(
        {
            "segment": ["Enterprise", "SMB", "Startup", "Individual", "Partner"],
            "count": np.random.randint(50, 500, 5),
            "avg_spend": np.random.uniform(100, 1000, 5).round(2),
        }
    ),
    "marketing": pd.DataFrame(
        {
            "channel": ["Social Media", "Email", "Search", "Referral", "Direct"],
            "spend": np.random.randint(500, 3000, 5),
            "conversions": np.random.randint(10, 100, 5),
        }
    ),
}

# Page setup
ui.page_opts(title="NavSet Hidden Demo", fillable=True)

# Sidebar for controlling hidden navset
with ui.sidebar():
    ui.input_radio_buttons(
        "controller",
        "Select View",
        ["Sales", "Customers", "Marketing"],
        selected="Sales",
    )

# Hidden NavSet with various options
with ui.navset_hidden(
    id="hidden_tabs",
    selected="sales_panel",
    header=ui.markdown("## Business Performance Dashboard"),
    footer=ui.p("Data updated dynamically", class_="text-muted text-center"),
):
    # Sales Panel
    with ui.nav_panel(None, value="sales_panel"):

        @render.data_frame
        def sales_table():
            return data_types["sales"]

        @render.plot
        def sales_plot():
            df = data_types["sales"]
            plt = df.plot(kind="bar", x="product", y="revenue", title="Product Revenue")
            return plt

    # Customers Panel
    with ui.nav_panel(None, value="customers_panel"):

        @render.data_frame
        def customers_table():
            return data_types["customers"]

        @render.plot
        def customers_plot():
            df = data_types["customers"]
            plt = df.plot(
                kind="pie",
                y="count",
                labels=df["segment"],
                autopct="%1.1f%%",
                title="Customer Segments",
            )
            return plt

    # Marketing Panel
    with ui.nav_panel(None, value="marketing_panel"):

        @render.data_frame
        def marketing_table():
            return data_types["marketing"]

        @render.plot
        def marketing_plot():
            df = data_types["marketing"]
            plt = df.plot(
                kind="bar", x="channel", y="spend", title="Marketing Channel Spend"
            )
            return plt


# Reactive effect to update navset based on radio button
@reactive.effect
def _():
    # Map radio button selection to corresponding panel value
    panel_map = {
        "Sales": "sales_panel",
        "Customers": "customers_panel",
        "Marketing": "marketing_panel",
    }
    ui.update_navs("hidden_tabs", selected=panel_map[input.controller()])
