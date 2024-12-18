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
        "Salary": [50000, 60000, 75000, 90000, 100000],
        "Department": ["HR", "IT", "Finance", "Marketing", "Sales"],
    }
)

# Page options
ui.page_opts(title="Checkbox Example")

# Sidebar with checkbox input
with ui.sidebar():
    ui.input_checkbox("show_age", "Show Age Column", value=True)
    ui.input_checkbox("show_salary", "Show Salary Column", value=False)


# Render the table based on checkbox selections
@render.data_frame
def employee_table():
    columns_to_show = ["Name", "Department"]

    if input.show_age():
        columns_to_show.append("Age")

    if input.show_salary():
        columns_to_show.append("Salary")

    return data[columns_to_show]
