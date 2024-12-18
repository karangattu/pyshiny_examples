from shiny import reactive, render
from shiny.express import input, ui
import random
import string

# Synthetic data generation
def generate_random_string(length=5):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def generate_sample_data(num_items=10):
    return [
        {
            'id': generate_random_string(),
            'name': f"Item {i+1}",
            'value': round(random.uniform(10, 100), 2)
        } for i in range(num_items)
    ]

# App Title and Page Options
ui.page_opts(title="insert_ui Demonstration", fillable=True)

# Sidebar with controls
with ui.sidebar():
    ui.input_radio_buttons(
        "where", 
        "Insertion Location", 
        ["beforeBegin", "afterBegin", "beforeEnd", "afterEnd"]
    )
    
    ui.input_radio_buttons(
        "selector", 
        "Selector Target", 
        ["#target_div", "#button_container"]
    )
    
    ui.input_checkbox("multiple", "Multiple Insertion", value=False)
    
    ui.input_action_button("insert_btn", "Insert UI")
    
    ui.input_action_button("remove_btn", "Remove Last Inserted")

# Main content area
with ui.layout_columns():
    # Target div for insertions
    ui.div(id="target_div", style="border: 2px solid blue; min-height: 200px;", 
           "Target Div for Insertions")
    
    # Button container for alternative insertions
    ui.div(id="button_container", style="border: 2px solid green; min-height: 100px;", 
           "Button Container")

# Reactive value to track inserted elements
inserted_elements = reactive.value([])

# Insert UI Effect
@reactive.effect
@reactive.event(input.insert_btn)
def _():
    # Generate sample data
    sample_data = generate_sample_data(3 if input.multiple() else 1)
    
    for item in sample_data:
        # Create a div with the item's information
        new_div = ui.div(
            f"ID: {item['id']}, Name: {item['name']}, Value: {item['value']}",
            id=f"inserted_{item['id']}",
            style="background-color: lightyellow; margin: 5px; padding: 10px;"
        )
        
        # Insert UI with dynamic parameters
        ui.insert_ui(
            new_div,
            selector=input.selector(),
            where=input.where(),
            multiple=input.multiple(),
            immediate=False  # Default behavior
        )
        
        # Track inserted elements
        current_elements = inserted_elements.get() if inserted_elements.is_set() else []
        current_elements.append(f"inserted_{item['id']}")
        inserted_elements.set(current_elements)

# Remove UI Effect
@reactive.effect
@reactive.event(input.remove_btn)
def _():
    if inserted_elements.is_set() and inserted_elements.get():
        last_element_id = inserted_elements.get()[-1]
        ui.remove_ui(f"#{last_element_id}")
        
        # Update the tracked elements
        current_elements = inserted_elements.get()
        current_elements.pop()
        inserted_elements.set(current_elements) if current_elements else inserted_elements.unset()

# Display currently inserted elements
@render.text
def show_inserted():
    if inserted_elements.is_set():
        return f"Currently Inserted Elements: {', '.join(inserted_elements.get())}"
    return "No elements inserted yet"