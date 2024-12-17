import random
import string

from shiny import reactive
from shiny.express import input, render, ui

# Generate synthetic data for accordion panels
def generate_panel_data(num_panels):
    panels = []
    for i in range(num_panels):
        letter = random.choice(string.ascii_uppercase)
        description = f"This is a dynamically generated panel with letter {letter}"
        panels.append({
            "title": f"Section {letter}",
            "value": f"sec_{letter}",
            "content": description
        })
    return panels

# Initialize panel data
initial_panels = generate_panel_data(5)

ui.page_opts(title="Accordion Panel Removal Demo")

with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_numeric("num_panels", "Number of Panels", 
                         value=len(initial_panels), min=1, max=10)
        
        ui.input_selectize("panel_to_remove", "Select Panel to Remove", 
                           choices=[panel['value'] for panel in initial_panels], 
                           multiple=False)
        
        ui.input_action_button("remove_btn", "Remove Selected Panel")
        
        ui.input_action_button("reset_btn", "Reset Panels")

    with ui.card():
        ui.card_header("Accordion Panels")
        
        with ui.accordion(id="demo_accordion", multiple=True):
            for panel in initial_panels:
                with ui.accordion_panel(panel['title'], value=panel['value']):
                    panel['content']

        # Display current panel values
        @render.text
        def panel_values():
            return f"Current Panel Values: {[panel['value'] for panel in initial_panels]}"

# Reactive value to track current panels
current_panels = reactive.value(initial_panels)

@reactive.effect
@reactive.event(input.remove_btn)
def remove_panel():
    panels = current_panels()
    panel_to_remove = input.panel_to_remove()
    
    # Find and remove the selected panel
    panels = [panel for panel in panels if panel['value'] != panel_to_remove]
    
    # Update the current panels
    current_panels.set(panels)
    
    # Update the accordion
    ui.remove_accordion_panel("demo_accordion", panel_to_remove)
    
    # Update the selection choices
    ui.update_selectize("panel_to_remove", 
                        choices=[panel['value'] for panel in panels])

@reactive.effect
@reactive.event(input.reset_btn)
def reset_panels():
    # Regenerate panels based on the number input
    new_panels = generate_panel_data(input.num_panels())
    current_panels.set(new_panels)
    
    # Clear and repopulate the accordion
    ui.remove_accordion_panel("demo_accordion", 
                               [panel['value'] for panel in current_panels()])
    
    # Repopulate the accordion with new panels
    for panel in new_panels:
        ui.insert_accordion_panel("demo_accordion", 
                                   ui.accordion_panel(
                                       title=panel['title'], 
                                       value=panel['value'], 
                                       panel['content']
                                   ))
    
    # Update the selection choices
    ui.update_selectize("panel_to_remove", 
                        choices=[panel['value'] for panel in new_panels])