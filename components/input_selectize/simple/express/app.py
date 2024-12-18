from shiny import reactive
from shiny.express import input, ui, render

# Sample data - dictionary with categories and items
items = {
    "Fruits": {
        "apple": "Red Apple",
        "banana": "Yellow Banana",
        "orange": "Fresh Orange",
        "grape": "Purple Grape",
    },
    "Vegetables": {
        "carrot": "Orange Carrot",
        "broccoli": "Green Broccoli",
        "spinach": "Fresh Spinach",
        "tomato": "Red Tomato",
    },
}

# Set page options
ui.page_opts(title="Selectize Demo", fillable=True)

# Create selectize input
ui.input_selectize(
    "item_select",
    "Select Items",
    choices=items,
    multiple=True,
    options={"placeholder": "Choose items..."},
)


@render.text
def selection():
    """Show the current selection"""
    selected = input.item_select()
    if not selected:
        return "No items selected"
    return f"You selected: {', '.join(selected)}"
