import pandas as pd
import numpy as np

from shiny import reactive
from shiny.express import input, render, ui

# Create synthetic data
np.random.seed(42)
data = pd.DataFrame(
    {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Age": [25, 30, 35, 40, 45],
        "City": ["New York", "San Francisco", "Chicago", "Boston", "Seattle"],
        "Salary": [50000, 75000, 60000, 90000, 80000],
    }
)

# Page title and description
ui.page_opts(title="Radio Button Demo")

# Sidebar with radio buttons
with ui.sidebar():
    ui.input_radio_buttons(
        "selected_column",
        "Choose a column to display:",
        ["Name", "Age", "City", "Salary"],
    )


# Main content area
@render.table
def display_data():
    # Get the selected column from radio buttons
    selected_col = input.selected_column()

    # Return the dataframe with only the selected column
    return data[[selected_col]]
