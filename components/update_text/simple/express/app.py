from shiny import reactive
from shiny.express import input, ui, render

# Create some initial data
pet_types = ["Dog", "Cat", "Bird", "Hamster", "Fish"]
pet_sexes = ["Male", "Female"]

ui.page_opts(title="Pet Name Generator")

with ui.layout_column_wrap(width=1 / 2):
    # Input for selecting pet type
    ui.input_radio_buttons("pet_type", "Pet Type", choices=pet_types, inline=True)

    # Input for selecting pet sex
    ui.input_radio_buttons("pet_sex", "Pet Sex", choices=pet_sexes, inline=True)

    # Initial text input for pet name
    ui.input_text("name", "Pet Name", "Charlie")

    # Initial text input for royal name
    ui.input_text("royal_name", "Royal Name", "King Charlie")


# Reactive effect to update pet name label based on pet type
@reactive.effect
@reactive.event(input.pet_type)
def _():
    # Update the label of the pet name input
    ui.update_text("name", label=f"{input.pet_type()}'s name")


# Reactive effect to update royal name based on pet name and sex
@reactive.effect
def _():
    # Update the value of the royal name input
    royal_noun = "King" if input.pet_sex() == "Male" else "Queen"
    ui.update_text("royal_name", value=f"{royal_noun} {input.name()}")
