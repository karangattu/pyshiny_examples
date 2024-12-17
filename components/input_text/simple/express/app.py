from shiny import reactive
from shiny.express import input, render, ui

# Create synthetic data
names = ["Alice Smith", "Bob Johnson", "Charlie Brown", "Diana Prince", "Ethan Hunt"]

ages = [28, 35, 42, 31, 45]

occupations = ["Software Engineer", "Teacher", "Doctor", "Lawyer", "Scientist"]

# Create a synthetic DataFrame to work with
import pandas as pd

df = pd.DataFrame({"Name": names, "Age": ages, "Occupation": occupations})

# UI Components
ui.page_opts(title="Text Input Demo")

with ui.layout_sidebar():
    with ui.sidebar():
        # Text input for filtering names
        ui.input_text(
            "name_filter", "Filter Names", placeholder="Enter a name or part of a name"
        )

    # Main panel to display results
    @render.table
    def filtered_table():
        # If no input, return full table
        if not input.name_filter():
            return df

        # Filter table based on input
        filtered = df[df["Name"].str.contains(input.name_filter(), case=False)]
        return filtered

    # Render text output showing current filter
    @render.text
    def filter_status():
        if input.name_filter():
            return f"Filtering for: {input.name_filter()}"
        return "No filter applied"
