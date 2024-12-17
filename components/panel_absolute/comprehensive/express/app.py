import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from shiny import reactive
from shiny.express import input, ui, render

# Generate synthetic data
np.random.seed(42)
sales_data = pd.DataFrame(
    {
        "Region": ["North", "South", "East", "West", "Central"],
        "Sales": np.random.randint(100000, 500000, 5),
        "Profit": np.random.randint(10000, 50000, 5),
    }
)

# Page setup
ui.page_opts(title="Panel Absolute Showcase", fillable=True)

# Sidebar for controlling panel absolute parameters
with ui.sidebar():
    ui.input_select("position", "Panel Position", ["top", "left", "right", "bottom"])
    ui.input_slider("distance", "Distance from Edge", min=0, max=100, value=20)
    ui.input_slider("width", "Panel Width", min=100, max=500, value=250)
    ui.input_slider("height", "Panel Height", min=100, max=500, value=200)
    ui.input_checkbox("draggable", "Draggable", value=False)
    ui.input_checkbox("fixed", "Fixed Position", value=False)
    ui.input_select("cursor", "Cursor Style", ["auto", "move", "default", "inherit"])


# Main content area
@render.plot
def sales_plot():
    plt.figure(figsize=(10, 6))
    plt.bar(sales_data["Region"], sales_data["Sales"])
    plt.title("Regional Sales Performance")
    plt.xlabel("Region")
    plt.ylabel("Sales")
    return plt.gcf()


# Create a reactive function to determine panel positioning
@reactive.calc
def panel_positioning():
    position = input.position()
    distance = input.distance()
    width = input.width()
    height = input.height()

    # Determine positioning based on selected position
    if position == "top":
        return {
            "top": f"{distance}px",
            "left": "50%",
            "width": f"{width}px",
            "height": f"{height}px",
        }
    elif position == "left":
        return {
            "left": f"{distance}px",
            "top": "50%",
            "width": f"{width}px",
            "height": f"{height}px",
        }
    elif position == "right":
        return {
            "right": f"{distance}px",
            "top": "50%",
            "width": f"{width}px",
            "height": f"{height}px",
        }
    else:  # bottom
        return {
            "bottom": f"{distance}px",
            "left": "50%",
            "width": f"{width}px",
            "height": f"{height}px",
        }


# Absolute panel with dynamic parameters
with ui.panel_absolute(
    draggable=input.draggable(),
    fixed=input.fixed(),
    cursor=input.cursor(),
    **panel_positioning(),
):
    ui.card(
        ui.card_header("Panel Details"),
        f"Position: {input.position()}",
        f"Distance: {input.distance()}px",
        f"Width: {input.width()}px",
        f"Height: {input.height()}px",
        f"Draggable: {input.draggable()}",
        f"Fixed: {input.fixed()}",
        f"Cursor: {input.cursor()}",
    )
