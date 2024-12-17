import random
import string
from datetime import datetime, timedelta

from shiny import reactive, render
from shiny.express import input, ui

# Generate synthetic data
def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_synthetic_data(num_items=10):
    return [
        {
            "id": f"item_{i}",
            "title": f"Section {chr(65 + i)}",
            "content": f"Dynamic content for section {chr(65 + i)}: {generate_random_string()}",
            "timestamp": datetime.now() - timedelta(days=random.randint(0, 30))
        } 
        for i in range(num_items)
    ]

# Initialize data
initial_data = generate_synthetic_data()

ui.page_opts(title="Accordion Panel Insertion Demo")

with ui.layout_sidebar():
    with ui.sidebar():
        # Inputs to control accordion panel insertion
        ui.input_text("new_panel_title", "New Panel Title", placeholder="Enter panel title")
        ui.input_text("new_panel_content", "Panel Content", placeholder="Enter panel content")
        
        # Position selection
        ui.input_radio_buttons(
            "insert_position", 
            "Insert Position", 
            ["after", "before"], 
            selected="after"
        )
        
        # Target panel selection
        ui.input_selectize(
            "target_panel", 
            "Target Panel", 
            [item['title'] for item in initial_data]
        )
        
        # Action button to insert panel
        ui.input_action_button("insert_panel", "Insert Panel")

    # Accordion with initial data
    with ui.accordion(id="demo_accordion", multiple=True):
        for item in initial_data:
            with ui.accordion_panel(item['title'], value=item['id']):
                ui.markdown(f"**Created at:** {item['timestamp']}")
                ui.p(item['content'])

    # Display current accordion state
    ui.h4("Current Accordion Panels")
    
    @render.text
    def accordion_state():
        return f"Current panels: {input.demo_accordion()}"

# Reactive effect to handle panel insertion
@reactive.effect
@reactive.event(input.insert_panel)
def _():
    # Validate inputs
    if not input.new_panel_title() or not input.new_panel_content():
        ui.notification_show(
            "Please provide both title and content", 
            type="warning"
        )
        return
    
    # Generate a unique ID for the new panel
    new_panel_id = f"item_{generate_random_string(5)}"
    
    # Create the new panel
    new_panel = ui.accordion_panel(
        input.new_panel_title(), 
        value=new_panel_id,
        ui.p(input.new_panel_content()),
        ui.p(f"**Inserted at:** {datetime.now()}")
    )
    
    # Insert the panel
    ui.insert_accordion_panel(
        "demo_accordion", 
        new_panel, 
        target=input.target_panel(), 
        position=input.insert_position()
    )