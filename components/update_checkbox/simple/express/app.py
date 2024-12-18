from shiny import reactive
from shiny.express import input, ui, render

# Create a synthetic dataset of pet information
pets = [
    {"name": "Fluffy", "type": "Cat", "age": 3, "vaccinated": False},
    {"name": "Buddy", "type": "Dog", "age": 5, "vaccinated": True},
    {"name": "Whiskers", "type": "Cat", "age": 7, "vaccinated": False},
    {"name": "Rex", "type": "Dog", "age": 2, "vaccinated": True},
    {"name": "Tweety", "type": "Bird", "age": 1, "vaccinated": False},
]

# UI Layout
ui.page_opts(title="Pet Vaccination Tracker")

with ui.layout_sidebar():
    with ui.sidebar():
        # Radio buttons to select pet type
        ui.input_radio_buttons(
            "pet_type", "Select Pet Type", ["All", "Dog", "Cat", "Bird"]
        )

        # Checkbox to show only unvaccinated pets
        ui.input_checkbox("unvaccinated_only", "Show Only Unvaccinated Pets")

    # Main panel to display the table
    @render.data_frame
    def pet_table():
        # Filter pets based on type and vaccination status
        filtered_pets = pets.copy()

        # Filter by pet type
        if input.pet_type() != "All":
            filtered_pets = [
                pet for pet in filtered_pets if pet["type"] == input.pet_type()
            ]

        # Filter by vaccination status
        if input.unvaccinated_only():
            filtered_pets = [pet for pet in filtered_pets if not pet["vaccinated"]]

        return filtered_pets

    # Reactive effect to update checkbox label dynamically
    @reactive.effect
    def _():
        # Dynamically update the checkbox label based on selected pet type
        label_text = (
            f"Show Only Unvaccinated {input.pet_type()} Pets"
            if input.pet_type() != "All"
            else "Show Only Unvaccinated Pets"
        )

        ui.update_checkbox("unvaccinated_only", label=label_text)
