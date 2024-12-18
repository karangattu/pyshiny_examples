import random
import pandas as pd
from shiny import reactive
from shiny.express import input, render, ui

# Generate synthetic data
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry"]
cities = [
    "New York",
    "San Francisco",
    "Chicago",
    "Boston",
    "Seattle",
    "Miami",
    "Denver",
    "Austin",
]
jobs = [
    "Engineer",
    "Designer",
    "Manager",
    "Scientist",
    "Teacher",
    "Doctor",
    "Artist",
    "Researcher",
]

# Create a synthetic DataFrame
df = pd.DataFrame(
    {
        "Name": names,
        "City": cities,
        "Job": jobs,
        "Age": [random.randint(25, 55) for _ in range(len(names))],
        "Salary": [random.randint(50000, 150000) for _ in range(len(names))],
    }
)

# Page title and description
ui.page_opts(title="Action Link Demo")
ui.h2("Interactive Employee Data Explorer")
ui.markdown("*Click the action links to explore different views of the data*")

# Sidebar with action links
with ui.sidebar():
    ui.input_action_link("show_names", "Show Names")
    ui.input_action_link("show_cities", "Show Cities")
    ui.input_action_link("show_jobs", "Show Jobs")
    ui.input_action_link("show_full", "Show Full Details")


# Render output based on action link clicks
@render.table
def employee_data():
    if input.show_names():
        return df[["Name", "Age"]]
    elif input.show_cities():
        return df[["Name", "City"]]
    elif input.show_jobs():
        return df[["Name", "Job", "Salary"]]
    else:
        return df
