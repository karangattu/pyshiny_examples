import random
import pandas as pd
from shiny import reactive
from shiny.express import input, ui, render


# Create synthetic data
def generate_random_data():
    """Generate a random DataFrame with some sample data."""
    return pd.DataFrame(
        {
            "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
            "Age": [random.randint(20, 65) for _ in range(5)],
            "Score": [random.randint(60, 100) for _ in range(5)],
        }
    )


# Initialize the data
data = generate_random_data()

# Create the UI with an action button
ui.page_opts(title="Random Data Generator")

with ui.sidebar():
    ui.input_action_button("generate", "Generate New Data")


# Render the data table
@render.data_frame
def display_data():
    return data


# Reactive effect to update data when button is clicked
@reactive.effect
@reactive.event(input.generate)
def _():
    global data
    data = generate_random_data()


# Optional: Add a text output to show when data was last generated
@render.text
def timestamp():
    input.generate()  # Create a dependency
    return f"Data last generated at: {pd.Timestamp.now()}"
