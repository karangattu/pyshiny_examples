from shiny import reactive
from shiny.express import input, ui, render

# Synthetic data for pet categories
pet_categories = {
    "Mammals": ["Dog", "Cat", "Horse", "Rabbit", "Hamster"],
    "Birds": ["Parrot", "Canary", "Eagle", "Owl", "Penguin"],
    "Reptiles": ["Snake", "Lizard", "Turtle", "Crocodile", "Gecko"],
    "Fish": ["Goldfish", "Shark", "Clownfish", "Betta", "Angelfish"],
}

# Initial checkbox group with all categories
ui.page_opts(title="Pet Category Selector")

with ui.layout_sidebar():
    with ui.sidebar():
        # Initial checkbox group to select categories
        ui.input_checkbox_group(
            "category_select", "Select Pet Categories", list(pet_categories.keys())
        )

        # Button to update the pets checkbox group
        ui.input_action_button("update_pets", "Update Pets")

    # Display the selected pets
    @render.text
    def pet_list():
        # Ensure a category is selected
        if not input.category_select():
            return "Please select a category"

        # Collect pets from selected categories
        pets = []
        for category in input.category_select():
            pets.extend(pet_categories[category])

        return f"Available Pets: {', '.join(pets)}"

    # Checkbox group for specific pets (to be updated)
    @render.ui
    def pet_checkbox():
        # If no category is selected, return nothing
        if not input.category_select():
            return ui.p("Select a category first")

        # Collect pets from selected categories
        pets = []
        for category in input.category_select():
            pets.extend(pet_categories[category])

        return ui.input_checkbox_group("selected_pets", "Choose Specific Pets", pets)

    # Reactive effect to update the pets checkbox group when the update button is clicked
    @reactive.effect
    @reactive.event(input.update_pets)
    def _():
        # Get currently selected categories
        categories = input.category_select()

        # If no categories are selected, do nothing
        if not categories:
            return

        # Collect all pets from selected categories
        all_pets = []
        for category in categories:
            all_pets.extend(pet_categories[category])

        # Update the checkbox group with pets from selected categories
        ui.update_checkbox_group(
            "selected_pets",
            label=f"Choose Pets from {', '.join(categories)} Categories",
            choices=all_pets,
            selected=all_pets[:2],  # Select first two pets by default
        )

    # Show the selected specific pets
    @render.text
    def selected_pets_output():
        # Check if any pets are selected
        if not input.selected_pets():
            return "No pets selected"

        return f"Selected Pets: {', '.join(input.selected_pets())}"
