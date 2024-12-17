from shiny import reactive, render
from shiny.express import input, ui

# Create synthetic data for the app
pet_types = ["Dog", "Cat", "Bird", "Fish", "Hamster"]
pet_colors = {
    "Dog": ["Brown", "Black", "White", "Golden", "Gray"],
    "Cat": ["Orange", "Black", "White", "Gray", "Calico"],
    "Bird": ["Blue", "Green", "Red", "Yellow", "White"],
    "Fish": ["Red", "Blue", "Orange", "Silver", "Gold"],
    "Hamster": ["Brown", "White", "Gray", "Black", "Tan"],
}

# Create the UI
ui.page_opts(title="Pet Color Selector")

# Main layout
with ui.layout_sidebar():
    # Sidebar with input controls
    with ui.sidebar():
        # First radio button group for pet type
        ui.input_radio_buttons(
            "pet_type",
            "Select Pet Type",
            pet_types,
            selected=pet_types[0],  # Set a default selection
        )

        # Second radio button group for pet color (dynamically updated)
        ui.input_radio_buttons(
            "pet_color",
            f"Select {pet_types[0]} Color",
            pet_colors[pet_types[0]],  # Populate with colors for first pet type
            selected=pet_colors[pet_types[0]][0],  # Set a default selection
        )

    # Output area to show selected pet details
    @render.text
    def pet_details():
        return f"You selected a {input.pet_color()} {input.pet_type()}!"


# Reactive effect to update color options based on selected pet type
@reactive.effect
def _():
    # Get the currently selected pet type
    selected_type = input.pet_type()

    # Get colors for the selected pet type
    color_choices = pet_colors.get(selected_type, [])

    # Update the color radio buttons based on the selected pet type
    ui.update_radio_buttons(
        "pet_color",  # ID of the color radio buttons
        label=f"Select {selected_type} Color",  # Dynamic label
        choices=color_choices,  # Get colors for selected pet type
        selected=(
            color_choices[0] if color_choices else None
        ),  # Select first color or None
    )
