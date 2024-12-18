from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np

# Make up some sample data
data = pd.DataFrame(
    {
        "date": pd.date_range(start="2024-01-01", periods=10),
        "value": np.random.normal(100, 10, 10),
    }
)

# Page options
ui.page_opts(title="Panel Absolute Demo", fillable=True)

# Main content
with ui.card():
    ui.card_header("Main Content Area")

    @render.table
    def data_table():
        df = data.copy()
        if not input.show_dates():
            df = df.drop("date", axis=1)
        return df.head(input.n_rows())


# Floating panel with controls
with ui.panel_absolute(right="20px", top="20px", width="200px", draggable=True):
    with ui.card():
        ui.card_header("Controls")
        ui.input_slider("n_rows", "Number of Rows", min=1, max=10, value=5)
        ui.input_switch("show_dates", "Show Dates", True)

# Add a floating info box at the bottom
with ui.panel_absolute(left="20px", bottom="20px", width="300px"):
    with ui.card():
        "💡 Drag the controls panel around the screen!"
        ui.br()
        "The panels will stay fixed relative to the viewport."
