import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, render, ui

# Create synthetic data
np.random.seed(42)
data = pd.DataFrame(
    {"x": np.random.normal(0, 1, 1000), "y": np.random.normal(0, 1, 1000)}
)

# Shiny App
ui.page_opts(title="Numeric Input Demonstration")

with ui.sidebar():
    ui.input_numeric(
        "obs", "Number of observations:", value=500, min=10, max=1000, step=10
    )


@render.plot(alt="Histogram of random data")
def plot():
    # Use input value to control number of observations
    n = input.obs()

    fig, ax = plt.subplots()
    ax.hist(data["x"][:n], bins=30, density=True, alpha=0.7, color="skyblue")
    ax.set_title(f"Histogram of {n} Observations")
    ax.set_xlabel("Value")
    ax.set_ylabel("Density")

    return fig


@render.text
def summary_stats():
    n = input.obs()
    subset = data["x"][:n]
    return f"""
    Summary Statistics (first {n} observations):
    Mean: {subset.mean():.2f}
    Standard Deviation: {subset.std():.2f}
    Min: {subset.min():.2f}
    Max: {subset.max():.2f}
    """
