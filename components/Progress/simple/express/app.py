import asyncio
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render


# Simulate a time-consuming data generation and processing task
async def generate_data(n_samples):
    """Simulate a slow data generation process with a progress bar."""
    data = {"x": [], "y": [], "category": []}

    with ui.Progress(min=1, max=n_samples) as p:
        p.set(message="Generating data", detail="This may take a while...")

        for i in range(1, n_samples + 1):
            # Simulate some computation time
            await asyncio.sleep(0.1)

            # Generate random data
            x_val = random.uniform(0, 10)
            y_val = x_val * 2 + random.gauss(0, 1)
            category = random.choice(["A", "B", "C"])

            data["x"].append(x_val)
            data["y"].append(y_val)
            data["category"].append(category)

            # Update progress
            p.set(i, message="Generating data", detail=f"Processing sample {i}")

    return pd.DataFrame(data)


# UI Setup
ui.page_opts(title="Progress Bar Demo")

# Sidebar with input controls
with ui.sidebar():
    ui.input_slider("n_samples", "Number of Samples", 10, 200, 50)
    ui.input_action_button("generate", "Generate Data")

# Main panel for displaying results
with ui.layout_columns():

    @render.data_frame
    @reactive.event(input.generate)
    async def data_table():
        # Generate data with progress bar
        df = await generate_data(input.n_samples())
        return df

    @render.plot
    @reactive.event(input.generate)
    async def scatter_plot():
        # Generate data with progress bar
        df = await generate_data(input.n_samples())

        plt.figure(figsize=(8, 6))
        for category in df["category"].unique():
            subset = df[df["category"] == category]
            plt.scatter(subset["x"], subset["y"], label=category, alpha=0.7)

        plt.title(f"Scatter Plot (n={input.n_samples()})")
        plt.xlabel("X values")
        plt.ylabel("Y values")
        plt.legend()

        return plt.gcf()
