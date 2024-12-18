from shiny import reactive
from shiny.express import input, ui, render
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Synthetic data generation
np.random.seed(42)
categories = ["Electronics", "Clothing", "Books", "Home Goods", "Sports"]
sales_data = pd.DataFrame(
    {
        "Category": categories,
        "Sales": np.random.randint(1000, 10000, len(categories)),
        "Profit Margin": np.random.uniform(0.1, 0.5, len(categories)),
    }
)

# Page options
ui.page_opts(title="Accordion Panel Showcase", fillable=True)

# Add Font Awesome CSS
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">'
    )
)

# Main Accordion with various configurations
with ui.accordion(id="main_accordion", multiple=True):
    # Panel 1: Basic Panel with Title and Content
    with ui.accordion_panel("Sales Overview"):

        @render.table
        def sales_table():
            return sales_data

    # Panel 2: Panel with Icon
    with ui.accordion_panel(
        "Profit Margins", icon=ui.tags.i(class_="fa-solid fa-chart-simple")
    ):

        @render.plot
        def profit_plot():
            plt.figure(figsize=(8, 4))
            plt.bar(sales_data["Category"], sales_data["Profit Margin"])
            plt.title("Profit Margins by Category")
            plt.xlabel("Category")
            plt.ylabel("Profit Margin")
            plt.xticks(rotation=45)
            plt.tight_layout()
            return plt.gcf()

    # Panel 3: Panel with Custom Value
    with ui.accordion_panel(
        "Detailed Analytics",
        value="analytics_panel",
        icon=ui.tags.i(class_="fa-solid fa-magnifying-glass"),
    ):
        ui.input_slider(
            "sales_threshold", "Sales Threshold", min=0, max=10000, value=5000
        )

        @render.table
        def filtered_sales():
            threshold = input.sales_threshold()
            return sales_data[sales_data["Sales"] > threshold]

    # Panel 4: Disabled Panel
    with ui.accordion_panel(
        "Restricted Data", icon=ui.tags.i(class_="fa-solid fa-lock")
    ):
        ui.p("This panel contains sensitive information and is currently disabled.")

# Sidebar for accordion control
with ui.sidebar():
    ui.input_checkbox("enable_multiple", "Enable Multiple Open Panels", value=True)
    ui.input_action_button("toggle_analytics", "Toggle Analytics Panel")


# Reactive effects for dynamic accordion behavior
@reactive.effect
def _():
    # Toggle multiple panel opening
    ui.update_accordion("main_accordion", show=input.enable_multiple())


@reactive.effect
@reactive.event(input.toggle_analytics)
def _():
    # Toggle visibility of analytics panel
    current_open = input.main_accordion()
    if "analytics_panel" in current_open:
        ui.update_accordion(
            "main_accordion",
            show=[panel for panel in current_open if panel != "analytics_panel"],
        )
    else:
        ui.update_accordion("main_accordion", show=current_open + ["analytics_panel"])


# Display current accordion state
@render.text
def accordion_state():
    return f"Currently Open Panels: {input.main_accordion()}"
