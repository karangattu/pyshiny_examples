import asyncio
import random
import time
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render


# Synthetic data generation function
def generate_synthetic_data(n):
    """Generate synthetic time series data."""
    dates = [datetime.now() + timedelta(days=i) for i in range(n)]
    values = np.cumsum(np.random.normal(0, 1, n))
    return pd.DataFrame(
        {
            "date": dates,
            "value": values,
            "category": np.random.choice(["A", "B", "C"], n),
        }
    )


# Page setup
ui.page_opts(title="Progress Component Demonstration", fillable=True)

# Sidebar with various input controls
with ui.sidebar():
    ui.input_slider("n", "Number of Data Points", 10, 500, 100)
    ui.input_slider("duration", "Task Duration (seconds)", 1, 10, 5)
    ui.input_radio_buttons(
        "progress_type",
        "Progress Type",
        ["Basic", "With Message", "With Detail", "Incremental"],
    )
    ui.input_action_button("run_task", "Run Task")

# Main content area
with ui.layout_columns():
    # Task output display
    @render.text
    def task_output():
        return f"Task Status: {task_status()}"

    # Plot output
    @render.plot
    def result_plot():
        return plot_result()


# Reactive value to store task status
task_status = reactive.value("Not Started")

# Reactive value to store generated data
result_data = reactive.value(None)


# Main task execution with Progress demonstration
@reactive.effect
@reactive.event(input.run_task)
async def _():
    # Reset task status
    task_status.set("Running")

    # Prepare data generation parameters
    n_points = input.n()
    task_duration = input.duration()
    progress_type = input.progress_type()

    try:
        # Different Progress demonstrations based on selected type
        if progress_type == "Basic":
            # Basic progress bar
            with ui.Progress(min=1, max=n_points) as p:
                data = await generate_data_with_progress(n_points, task_duration, p)
                result_data.set(data)
                task_status.set("Completed")

        elif progress_type == "With Message":
            # Progress bar with message
            with ui.Progress(min=1, max=n_points) as p:
                p.set(message="Generating Data")
                data = await generate_data_with_progress(n_points, task_duration, p)
                result_data.set(data)
                task_status.set("Completed")

        elif progress_type == "With Detail":
            # Progress bar with message and detail
            with ui.Progress(min=1, max=n_points) as p:
                p.set(
                    message="Generating Complex Dataset",
                    detail="This may take a moment...",
                )
                data = await generate_data_with_progress(n_points, task_duration, p)
                result_data.set(data)
                task_status.set("Completed")

        elif progress_type == "Incremental":
            # Incremental progress demonstration
            with ui.Progress(min=1, max=n_points) as p:
                data = []
                for i in range(1, n_points + 1):
                    p.inc(
                        amount=1,
                        message="Generating Data",
                        detail=f"Processing point {i}",
                    )
                    await asyncio.sleep(task_duration / n_points)
                    data.append(random.random())

                result_data.set(pd.DataFrame(data, columns=["random_value"]))
                task_status.set("Completed")

    except Exception as e:
        task_status.set(f"Error: {str(e)}")


# Async data generation with progress tracking
async def generate_data_with_progress(n_points, duration, progress):
    """Simulate data generation with asyncio and progress tracking."""
    data = []
    for i in range(1, n_points + 1):
        progress.set(i, message="Generating Data")
        await asyncio.sleep(duration / n_points)
        data.append(random.random())
    return pd.DataFrame(data, columns=["random_value"])


# Plot result visualization
def plot_result():
    df = result_data()
    if df is None:
        return None

    plt.figure(figsize=(10, 6))

    if len(df.columns) > 1:  # Time series data
        plt.plot(df["date"], df["value"], label="Value")
        plt.title("Synthetic Time Series")
        plt.xlabel("Date")
        plt.ylabel("Value")
    else:  # Random values
        plt.bar(range(len(df)), df["random_value"])
        plt.title("Random Values")
        plt.xlabel("Index")
        plt.ylabel("Value")

    plt.tight_layout()
    return plt.gcf()
