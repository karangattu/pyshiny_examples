import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Busy Indicators Demo", fillable=True)

# Add Font Awesome CSS for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">'
    )
)

# Customize busy indicators
ui.busy_indicators.options(
    spinner_type="bars3",  # Choose a specific spinner type
    spinner_color="#007bff",  # Bootstrap primary color
    spinner_size="50px",
    spinner_delay=0.5,  # Half-second delay before showing spinner
)


# Synthetic data generation function with artificial delay
def long_computation(n):
    time.sleep(2)  # Simulate a long computation
    np.random.seed(42)
    return pd.DataFrame(
        {
            "Category": [f"Group {i+1}" for i in range(n)],
            "Value": np.random.randint(10, 100, n),
            "Random Score": np.random.uniform(0, 1, n),
        }
    )


# Sidebar with controls
with ui.sidebar():
    ui.input_slider("n", "Number of Data Points", min=5, max=50, value=20)
    ui.input_action_button("compute", "Compute Data")

    # Busy indicator type selection
    ui.input_select(
        "spinner_type",
        "Spinner Type",
        {
            "bars3": "Bars 3",
            "dots": "Dots",
            "spinner": "Spinner",
        },
    )

    # Color selection
    ui.input_select(
        "spinner_color",
        "Spinner Color",
        {
            "#007bff": "Primary Blue",
            "#28a745": "Success Green",
            "#dc3545": "Danger Red",
            "#ffc107": "Warning Yellow",
        },
    )


# Update busy indicator options dynamically
@reactive.effect
def _():
    ui.busy_indicators.options(
        spinner_type=input.spinner_type(),
        spinner_color=input.spinner_color(),
        spinner_size="50px",
        spinner_delay=0.5,
    )


# Reactive computation with busy indicator
@reactive.calc
@reactive.event(input.compute)
def computed_data():
    return long_computation(input.n())


# Render data table
@render.data_frame
def result_table():
    return computed_data()


# Render plot
@render.plot
def result_plot():
    df = computed_data()
    plt.figure(figsize=(10, 6))
    plt.bar(df["Category"], df["Value"], color="skyblue")
    plt.title("Computed Data Visualization")
    plt.xlabel("Category")
    plt.ylabel("Value")
    plt.xticks(rotation=45)
    return plt.gcf()
