from shiny import reactive
from shiny.express import input, ui, render

# Synthetic data generation
import random
import pandas as pd
import numpy as np

# Create synthetic dataset
np.random.seed(42)
data = pd.DataFrame(
    {
        "temperature": np.random.normal(25, 5, 100),
        "humidity": np.random.uniform(40, 80, 100),
        "wind_speed": np.random.normal(10, 3, 100),
        "precipitation": np.random.exponential(5, 100),
    }
)

# Page options and styling
ui.page_opts(title="Input Switch Showcase", fillable=True)

# Add Font Awesome CSS for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">'
    )
)

# Sidebar with multiple input_switch demonstrations
with ui.sidebar():
    # Basic input_switch
    ui.input_switch("basic_switch", "Basic Switch")

    # Switch with initial value
    ui.input_switch("initial_switch", "Switch with Initial Value", value=True)

    # Switch with custom width
    ui.input_switch("width_switch", "Custom Width Switch", width="300px")

    # Switch with icon
    ui.input_switch(
        "icon_switch",
        ui.tags.span(
            "Switch with Icon ",
            ui.tags.i(class_="fa-solid fa-bolt", style="margin-left: 5px;"),
        ),
    )

# Main content area with reactive demonstrations
with ui.layout_columns():
    # Card showing switch states
    with ui.card():
        ui.card_header("Switch States")

        @render.text
        def switch_states():
            return f"""
            Basic Switch: {input.basic_switch()}
            Initial Switch: {input.initial_switch()}
            Width Switch: {input.width_switch()}
            Icon Switch: {input.icon_switch()}
            """

    # Card showing data filtering based on switches
    with ui.card():
        ui.card_header("Data Filtering")

        @render.data_frame
        def filtered_data():
            df = data.copy()

            if input.basic_switch():
                df = df[df["temperature"] > df["temperature"].mean()]

            if input.initial_switch():
                df = df[df["humidity"] > df["humidity"].median()]

            return df

    # Card showing dynamic visualization
    with ui.card():
        ui.card_header("Dynamic Visualization")

        @render.plot
        def dynamic_plot():
            import matplotlib.pyplot as plt

            plt.figure(figsize=(8, 4))

            if input.width_switch():
                plt.title("Temperature Distribution")
                plt.hist(
                    data["temperature"], bins=20, color="skyblue", edgecolor="black"
                )

            if input.icon_switch():
                plt.title("Humidity Distribution")
                plt.hist(
                    data["humidity"], bins=20, color="lightgreen", edgecolor="black"
                )

            return plt


# Reactive effects to demonstrate switch interactions
@reactive.effect
def _():
    # Example of dynamically updating switch based on conditions
    if input.basic_switch():
        ui.notification_show("Basic switch is ON!", type="message")
    else:
        ui.notification_show("Basic switch is OFF!", type="warning")


@reactive.effect
def _():
    # Example of disabling/enabling switches
    if input.initial_switch():
        ui.update_switch("width_switch", value=True)
    else:
        ui.update_switch("width_switch", value=False)
