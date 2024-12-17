from shiny import reactive
from shiny.express import input, ui, render

# Create synthetic data
pet_types = ["Dog", "Cat", "Bird", "Fish"]
dog_breeds = ["Labrador", "German Shepherd", "Golden Retriever", "Poodle"]
cat_breeds = ["Siamese", "Persian", "Maine Coon", "Bengal"]
bird_breeds = ["Parrot", "Canary", "Cockatiel", "Finch"]
fish_breeds = ["Goldfish", "Betta", "Guppy", "Angelfish"]

# Page setup
ui.page_opts(title="Pet Selector")

# Main UI
with ui.layout_sidebar():
    with ui.sidebar():
        # First level selection: Pet Type
        ui.input_radio_buttons("pet_type", "Select Pet Type", choices=pet_types)

        # Conditional panel for breed selection based on pet type
        with ui.panel_conditional("input.pet_type === 'Dog'"):
            ui.input_radio_buttons("dog_breed", "Select Dog Breed", choices=dog_breeds)

        with ui.panel_conditional("input.pet_type === 'Cat'"):
            ui.input_radio_buttons("cat_breed", "Select Cat Breed", choices=cat_breeds)

        with ui.panel_conditional("input.pet_type === 'Bird'"):
            ui.input_radio_buttons(
                "bird_breed", "Select Bird Breed", choices=bird_breeds
            )

        with ui.panel_conditional("input.pet_type === 'Fish'"):
            ui.input_radio_buttons(
                "fish_breed", "Select Fish Breed", choices=fish_breeds
            )

    # Output area
    @render.text
    def pet_details():
        # Validate that a pet type is selected
        req(input.pet_type())

        # Determine breed based on pet type
        breed = None
        if input.pet_type() == "Dog" and input.dog_breed():
            breed = input.dog_breed()
        elif input.pet_type() == "Cat" and input.cat_breed():
            breed = input.cat_breed()
        elif input.pet_type() == "Bird" and input.bird_breed():
            breed = input.bird_breed()
        elif input.pet_type() == "Fish" and input.fish_breed():
            breed = input.fish_breed()

        # Return details
        return f"You selected a {breed} {input.pet_type()}"
