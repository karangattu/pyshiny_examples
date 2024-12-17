import asyncio
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render


# Synthetic data generation function
def generate_dataset(n_samples):
    """Generate a synthetic dataset for demonstration."""
    np.random.seed(42)
    data = {
        "x": np.linspace(0, 10, n_samples),
        "y": np.random.normal(loc=5, scale=2, size=n_samples),
        "category": np.random.choice(["A", "B", "C"], size=n_samples),
    }
    return pd.DataFrame(data)


# Async task to simulate a long-running computation
@reactive.extended_task
async def long_computation(dataset, processing_time):
    """Simulate a long-running data processing task."""
    await asyncio.sleep(processing_time)  # Simulate processing time

    # Perform some data transformations
    dataset["processed_y"] = dataset["y"] * np.random.uniform(0.8, 1.2, len(dataset))
    dataset["log_y"] = np.log(np.abs(dataset["processed_y"]) + 1)

    return dataset


# UI and Server Logic
ui.page_opts(title="Task Button Demo")

with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_numeric("n_samples", "Number of Samples", value=100, min=10, max=1000)
        ui.input_slider(
            "processing_time",
            "Processing Time (seconds)",
            min=1,
            max=10,
            value=3,
            step=1,
        )
        ui.input_task_button("compute", "Compute Dataset")

    with ui.card():
        ui.card_header("Dataset Processing")

        @render.data_frame
        def processed_data():
            # Trigger computation when task button is clicked
            result = long_computation(
                generate_dataset(input.n_samples()), input.processing_time()
            )
            return result

        @render.plot
        def result_plot():
            # Trigger plot rendering when task is complete
            df = long_computation.result()

            plt.figure(figsize=(8, 4))
            for category in df["category"].unique():
                subset = df[df["category"] == category]
                plt.scatter(subset["x"], subset["log_y"], label=category, alpha=0.7)

            plt.title("Processed Dataset Visualization")
            plt.xlabel("X")
            plt.ylabel("Log Transformed Y")
            plt.legend()
            return plt.gcf()
