from shiny import reactive
from shiny.express import input, ui, render
import random
import datetime


# Synthetic data generation
def generate_sample_data():
    return {
        "A": {
            "description": "First section with initial content",
            "details": f"Created at: {datetime.datetime.now()}",
            "value": "sec_A",
        },
        "B": {
            "description": "Second section with changeable content",
            "details": f"Last updated: {datetime.datetime.now()}",
            "value": "sec_B",
        },
        "C": {
            "description": "Third section with icon support",
            "details": f"Timestamp: {datetime.datetime.now()}",
            "value": "sec_C",
        },
    }


# Page setup
ui.page_opts(title="Update Accordion Panel Demo", fillable=True)

# Sidebar with controls
with ui.sidebar():
    ui.input_switch("toggle_panel", "Toggle Panel Visibility")
    ui.input_switch("update_content", "Update Panel Content")
    ui.input_selectize("select_panel", "Select Panel", choices=["A", "B", "C"])
    ui.input_text("custom_title", "Custom Title", placeholder="Enter new title")

# Main accordion
with ui.accordion(id="demo_accordion", multiple=True):
    sample_data = generate_sample_data()

    for letter, data in sample_data.items():
        with ui.accordion_panel(f"Section {letter}", value=data["value"]):
            ui.markdown(f"**{data['description']}**")
            ui.p(data["details"])


# Reactive effects for updating accordion panels
@reactive.effect
@reactive.event(input.toggle_panel)
def _():
    # Demonstrate show parameter
    show_state = bool(input.toggle_panel() % 2 == 1)
    for letter, data in sample_data.items():
        ui.update_accordion_panel("demo_accordion", data["value"], show=show_state)


@reactive.effect
@reactive.event(input.update_content)
def _():
    # Demonstrate updating body, title, and icon
    update_state = bool(input.update_content() % 2 == 1)

    for letter, data in sample_data.items():
        icon = ui.tags.i(class_="fa-solid fa-star") if update_state else None

        ui.update_accordion_panel(
            "demo_accordion",
            data["value"],
            (
                f"Updated content for Section {letter}"
                if update_state
                else data["description"]
            ),
            title=f"Modified Section {letter}" if update_state else f"Section {letter}",
            icon=icon,
        )


@reactive.effect
@reactive.event(input.select_panel, input.custom_title)
def _():
    # Demonstrate updating a specific panel with a custom title
    panel_letter = input.select_panel()
    custom_title = input.custom_title() or f"Section {panel_letter}"

    ui.update_accordion_panel(
        "demo_accordion", sample_data[panel_letter]["value"], title=custom_title
    )


# Optional: Display current accordion state
@render.text
def accordion_state():
    return f"Current accordion state: {input.demo_accordion()}"
