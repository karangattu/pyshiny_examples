from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np

# Create synthetic data
np.random.seed(42)
data = pd.DataFrame(
    {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Age": np.random.randint(25, 55, 5),
        "Salary": np.random.randint(50000, 120000, 5),
    }
)

# Set the page title using panel_title
ui.panel_title("Employee Dashboard", window_title="Employee Stats")

# Create a sidebar with input controls
with ui.sidebar():
    ui.input_select(
        "selected_column", "Select Column to Highlight", choices=["Age", "Salary"]
    )


# Display the data table
@render.data_frame
def employee_table():
    df = data.copy()
    highlight_col = input.selected_column()

    # Add conditional styling based on selected column
    if highlight_col == "Age":
        df["Age"] = df["Age"].apply(lambda x: f"**{x}**")
    elif highlight_col == "Salary":
        df["Salary"] = df["Salary"].apply(lambda x: f"**${x:,}**")

    return df


# Run the app
