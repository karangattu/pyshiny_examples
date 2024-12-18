from shiny import reactive
from shiny.express import input, ui, render
import random
import pandas as pd
import numpy as np


# Synthetic data generation
def generate_random_data(n=50):
    return pd.DataFrame(
        {
            "name": [f"Person_{i}" for i in range(n)],
            "age": np.random.randint(18, 80, n),
            "salary": np.random.randint(30000, 150000, n),
            "department": random.choices(
                ["HR", "IT", "Sales", "Marketing", "Finance"], k=n
            ),
        }
    )


# Global data
df = generate_random_data()

# Page setup
ui.page_opts(title="Remove UI Demonstration", fillable=True)

# Sidebar for controls
with ui.sidebar():
    ui.input_radio_buttons(
        "selector_type",
        "Selector Type",
        ["ID Selector", "Class Selector", "Tag Selector", "Attribute Selector"],
    )

    ui.input_checkbox("multiple_flag", "Multiple Removal", value=False)

    ui.input_action_button("remove_btn", "Remove UI Elements")
    ui.input_action_button("reset_btn", "Reset UI")

# Main content area
with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Dynamic UI Removal Demonstration")

        # Different types of UI elements to demonstrate removal
        with ui.div(id="id_demo_container"):
            ui.p("ID-based element 1", id="id_element1")
            ui.p("ID-based element 2", id="id_element2")
            ui.p("ID-based element 3", id="id_element3")

        with ui.div(class_="class_demo_container"):
            ui.p("Class-based element 1", class_="class_element")
            ui.p("Class-based element 2", class_="class_element")
            ui.p("Class-based element 3", class_="class_element")

        with ui.div(id="tag_demo_container"):
            ui.tags.span("Tag-based span 1", id="tag_span1")
            ui.tags.span("Tag-based span 2", id="tag_span2")
            ui.tags.span("Tag-based span 3", id="tag_span3")

        with ui.div(id="attribute_demo_container"):
            ui.p("Attribute-based element 1", **{"data-type": "demo"})
            ui.p("Attribute-based element 2", **{"data-type": "demo"})
            ui.p("Attribute-based element 3", **{"data-type": "demo"})


# Reactive effects for UI removal and reset
@reactive.effect
@reactive.event(input.remove_btn)
def remove_ui_elements():
    if input.selector_type() == "ID Selector":
        selector = "#id_element1"
        if input.multiple_flag():
            selector = "#id_demo_container > p"

    elif input.selector_type() == "Class Selector":
        selector = ".class_element"

    elif input.selector_type() == "Tag Selector":
        selector = "span#tag_span1"
        if input.multiple_flag():
            selector = "#tag_demo_container > span"

    elif input.selector_type() == "Attribute Selector":
        selector = "p[data-type='demo']"

    ui.remove_ui(
        selector=selector,
        multiple=input.multiple_flag(),
        immediate=False,  # Default behavior
    )


@reactive.effect
@reactive.event(input.reset_btn)
def reset_ui():
    # Reload the page to reset all UI elements
    ui.notification_show("UI Reset", type="message", duration=2)
