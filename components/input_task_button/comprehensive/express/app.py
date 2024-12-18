import asyncio
import random
import time
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
import plotly.express as px
from shiny import reactive, ui
from shiny.express import input, render


# Synthetic data generation
def generate_sales_data(num_records=100):
    """Generate synthetic sales data."""
    np.random.seed(42)
    dates = [datetime.now() - timedelta(days=x) for x in range(num_records)]
    regions = ["North", "South", "East", "West"]
    products = ["Laptop", "Smartphone", "Tablet", "Desktop"]

    data = {
        "date": dates,
        "region": np.random.choice(regions, num_records),
        "product": np.random.choice(products, num_records),
        "sales": np.random.randint(100, 1000, num_records),
        "revenue": np.random.uniform(1000, 10000, num_records),
    }

    return pd.DataFrame(data)


# Async task simulating data processing
@ui.bind_task_button(button_id="process_data")
@reactive.extended_task
async def process_sales_data(filter_region=None, min_sales=None):
    """Simulate a long-running data processing task."""
    await asyncio.sleep(3)  # Simulate processing time

    df = generate_sales_data()

    if filter_region:
        df = df[df["region"] == filter_region]

    if min_sales is not None:
        df = df[df["sales"] >= min_sales]

    return df


# Head content for Font Awesome
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">'
    )
)

# App UI and Logic
ui.page_opts(title="Task Button Demo", fillable=True)

with ui.layout_sidebar():
    with ui.sidebar():
        # Demonstrate various input_task_button parameters
        ui.input_task_button(
            "process_data",
            "Process Sales Data",
            label_busy="Processing...",  # Custom busy label
            icon=ui.tags.i(class_="fa-solid fa-chart-simple"),  # Font Awesome icon
            icon_busy=ui.tags.i(class_="fa-solid fa-spinner fa-spin"),  # Busy icon
            class_="btn-primary",  # Bootstrap class
            width="100%",  # Full width button
        )

        # Additional filter inputs
        ui.input_selectize(
            "region_filter",
            "Filter by Region",
            choices=["All", "North", "South", "East", "West"],
            multiple=False,
        )

        ui.input_numeric("min_sales", "Minimum Sales", value=0, min=0, max=1000)

    with ui.layout_columns():
        with ui.card(full_screen=True):
            ui.card_header("Sales Data Table")

            @render.data_frame
            def sales_table():
                # Get the processed data
                df = process_sales_data.result()
                return df

        with ui.card(full_screen=True):
            ui.card_header("Sales Distribution Plot")

            @render.plot
            def sales_plot():
                df = process_sales_data.result()
                fig = px.box(
                    df, x="region", y="sales", title="Sales Distribution by Region"
                )
                return fig

    with ui.card():
        ui.card_header("Task Button Status")

        @render.text
        def task_status():
            # Demonstrate task button status tracking
            return f"""
            Task Button Status:
            - Button Clicks: {input.process_data()}
            - Task Running: {process_sales_data.is_running()}
            - Task Result Available: {process_sales_data.is_done()}
            """


# Reactive effect to handle data processing
@reactive.effect
@reactive.event(input.process_data, ignore_none=False)
def _():
    # Determine filter parameters
    region_filter = None if input.region_filter() == "All" else input.region_filter()
    min_sales = input.min_sales()

    # Trigger data processing
    process_sales_data(region_filter, min_sales)


# Optional: Cancel button to demonstrate task cancellation
ui.input_action_button("cancel_task", "Cancel Processing Task")


@reactive.effect
@reactive.event(input.cancel_task)
def _():
    process_sales_data.cancel()
    ui.notification_show("Task cancelled!", type="warning")
