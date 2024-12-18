import random
import string

from shiny import reactive
from shiny.express import input, ui


# Function to generate a random string for panel content
def generate_random_content():
    return "".join(random.choices(string.ascii_letters, k=50))


# Function to generate a random panel name
def generate_panel_name():
    return "".join(random.choices(string.ascii_uppercase, k=3))


ui.page_opts(title="Insert Accordion Panel Demo")

# Initial accordion with some predefined panels
with ui.accordion(id="dynamic_accordion", multiple=True):
    with ui.accordion_panel("Initial Panel A"):
        "This is the first initial panel"

    with ui.accordion_panel("Initial Panel B"):
        "This is the second initial panel"

# Button to add a new panel
ui.input_action_button("add_panel", "Add Random Panel", class_="mt-3 mb-3")


# Reactive effect to handle panel insertion
@reactive.effect
@reactive.event(input.add_panel)
def _():
    # Generate a new panel with random name and content
    new_panel_name = generate_panel_name()
    new_panel_content = generate_random_content()

    # Create a new accordion panel and insert it
    new_panel = ui.accordion_panel(f"Dynamic Panel {new_panel_name}", new_panel_content)

    ui.insert_accordion_panel("dynamic_accordion", new_panel)
