import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, datetime, timedelta

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
numeric_data = pd.DataFrame(
    {"value": np.random.randn(len(dates)) * 10 + 50, "date": dates}
)

# Page setup with full width
ui.page_opts(title="Input Slider Showcase", full_width=True)

# Sidebar with various slider configurations
with ui.sidebar():
    # Basic numeric slider
    ui.input_slider("basic_slider", "Basic Numeric Slider", min=0, max=100, value=50)

    # Slider with step
    ui.input_slider("step_slider", "Slider with Step", min=0, max=100, value=50, step=5)

    # Slider with pre and post text
    ui.input_slider(
        "formatted_slider",
        "Formatted Slider",
        min=0,
        max=100,
        value=50,
        pre="$",
        post="%",
    )

    # Range slider
    ui.input_slider("range_slider", "Range Slider", min=0, max=100, value=(25, 75))

    # Slider with ticks
    ui.input_slider(
        "ticks_slider", "Slider with Ticks", min=0, max=100, value=50, ticks=True
    )

    # Date slider
    ui.input_slider(
        "date_slider",
        "Date Slider",
        min=date(2023, 1, 1),
        max=date(2023, 12, 31),
        value=date(2023, 6, 15),
    )

    # Date range slider
    ui.input_slider(
        "date_range_slider",
        "Date Range Slider",
        min=date(2023, 1, 1),
        max=date(2023, 12, 31),
        value=(date(2023, 3, 1), date(2023, 9, 30)),
    )

    # Datetime slider
    ui.input_slider(
        "datetime_slider",
        "Datetime Slider",
        min=datetime(2023, 1, 1),
        max=datetime(2023, 12, 31),
        value=datetime(2023, 6, 15, 12, 0),
        time_format="%Y-%m-%d %H:%M",
        timezone="+0000",
    )

    # Animated slider
    ui.input_slider(
        "animated_slider", "Animated Slider", min=0, max=100, value=50, animate=True
    )

# Main content area with outputs
with ui.layout_columns():
    # Basic slider output
    with ui.card():
        ui.card_header("Basic Slider Output")

        @render.text
        def basic_output():
            return f"Selected value: {input.basic_slider()}"

    # Step slider output
    with ui.card():
        ui.card_header("Step Slider Output")

        @render.text
        def step_output():
            return f"Selected value: {input.step_slider()}"

    # Formatted slider output
    with ui.card():
        ui.card_header("Formatted Slider Output")

        @render.text
        def formatted_output():
            return f"Selected value: {input.formatted_slider()}"

    # Range slider output
    with ui.card():
        ui.card_header("Range Slider Output")

        @render.text
        def range_output():
            return f"Selected range: {input.range_slider()}"

    # Ticks slider output
    with ui.card():
        ui.card_header("Ticks Slider Output")

        @render.text
        def ticks_output():
            return f"Selected value: {input.ticks_slider()}"

    # Date slider output
    with ui.card():
        ui.card_header("Date Slider Output")

        @render.text
        def date_output():
            return f"Selected date: {input.date_slider()}"

    # Date range slider output
    with ui.card():
        ui.card_header("Date Range Slider Output")

        @render.text
        def date_range_output():
            return f"Selected date range: {input.date_range_slider()}"

    # Datetime slider output
    with ui.card():
        ui.card_header("Datetime Slider Output")

        @render.text
        def datetime_output():
            return f"Selected datetime: {input.datetime_slider()}"

    # Animated slider output
    with ui.card():
        ui.card_header("Animated Slider Output")

        @render.text
        def animated_output():
            return f"Selected value: {input.animated_slider()}"

    # Plot based on slider selection
    with ui.card():
        ui.card_header("Data Visualization")

        @render.plot
        def dynamic_plot():
            plt.figure(figsize=(10, 5))

            # Filter data based on date slider
            start_date = input.date_slider()
            end_date = start_date + timedelta(days=30)

            filtered_data = numeric_data[
                (numeric_data["date"] >= start_date)
                & (numeric_data["date"] <= end_date)
            ]

            plt.plot(filtered_data["date"], filtered_data["value"])
            plt.title(f"Data from {start_date.date()} to {end_date.date()}")
            plt.xlabel("Date")
            plt.ylabel("Value")
            plt.xticks(rotation=45)
            return plt
