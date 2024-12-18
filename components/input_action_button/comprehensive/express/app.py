import random
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
sales_data = pd.DataFrame(
    {
        "date": pd.date_range(start="2023-01-01", periods=100),
        "product": np.random.choice(["A", "B", "C"], 100),
        "sales": np.random.randint(100, 1000, 100),
        "revenue": np.random.uniform(50, 500, 100),
    }
)

# Page options and styling
ui.page_opts(title="Input Action Button Showcase", fillable=True)

# Add Font Awesome CSS
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">'
    )
)

# Sidebar with various action button configurations
with ui.sidebar():
    # Basic action button
    ui.input_action_button("basic_btn", "Basic Button")

    # Button with icon
    ui.input_action_button(
        "icon_btn",
        "Button with Icon",
        icon=ui.tags.i(class_="fa-solid fa-chart-simple"),
    )

    # Disabled button
    ui.input_action_button("disabled_btn", "Disabled Button", disabled=True)

    # Button with custom width
    ui.input_action_button("width_btn", "Custom Width Button", width="200px")

    # Button with different Bootstrap themes
    ui.input_action_button("primary_btn", "Primary Button", class_="btn-primary")
    ui.input_action_button("success_btn", "Success Button", class_="btn-success")
    ui.input_action_button("danger_btn", "Danger Button", class_="btn-danger")

# Main content area with outputs
with ui.layout_columns():
    # Display button click counts
    with ui.card(full_screen=True):
        ui.card_header("Button Click Counts")

        @render.table
        def button_clicks():
            clicks = {
                "Basic Button": input.basic_btn(),
                "Icon Button": input.icon_btn(),
                "Primary Button": input.primary_btn(),
                "Success Button": input.success_btn(),
                "Danger Button": input.danger_btn(),
            }
            return pd.DataFrame.from_dict(clicks, orient="index", columns=["Clicks"])

    # Random plot generation based on button clicks
    with ui.card(full_screen=True):
        ui.card_header("Sales Visualization")

        @render.plot
        @reactive.event(input.primary_btn)
        def sales_plot():
            plt.figure(figsize=(10, 6))
            sample = sales_data.sample(n=min(50, len(sales_data)))
            plt.scatter(
                sample["sales"], sample["revenue"], c=sample["sales"], cmap="viridis"
            )
            plt.title(f"Sales vs Revenue (Click Count: {input.primary_btn()})")
            plt.xlabel("Sales")
            plt.ylabel("Revenue")
            plt.colorbar(label="Sales Volume")
            return plt.gcf()


# Notifications and effects
@reactive.effect
@reactive.event(input.icon_btn)
def _():
    ui.notification_show(
        f"Icon Button clicked {input.icon_btn()} times!", duration=3, type="message"
    )


@reactive.effect
@reactive.event(input.success_btn)
def _():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ui.notification_show(
        f"Success Button clicked at {current_time}", duration=5, type="success"
    )
