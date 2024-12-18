from shiny import reactive
from shiny.express import input, ui, render

# Page title and options
ui.page_opts(title="Switch Demo", fillable=True)

# Create a switch input
ui.input_switch("show_data", "Show Data Table", value=True)

# Create some sample data
import pandas as pd
import numpy as np

# Generate sample data
np.random.seed(123)
data = pd.DataFrame(
    {
        "Name": [f"Person {i}" for i in range(1, 11)],
        "Age": np.random.randint(20, 80, 10),
        "Score": np.random.uniform(50, 100, 10).round(2),
    }
)


# Show data table conditionally based on switch
@render.data_frame
def table():
    if input.show_data():
        return data
    return pd.DataFrame()  # Return empty dataframe if switch is off


# Show text message based on switch state
@render.text
def status():
    if input.show_data():
        return "Data table is visible"
    return "Data table is hidden"
