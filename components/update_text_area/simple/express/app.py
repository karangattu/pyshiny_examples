from shiny import reactive
from shiny.express import input, ui, render

# Create some initial data
initial_pet_data = {
    "Dog": "Friendly golden retriever who loves to play fetch",
    "Cat": "Elegant Siamese with a regal demeanor",
    "Bird": "Colorful parrot with an impressive vocabulary",
}

ui.page_opts(title="Pet Description Editor")

with ui.layout_sidebar():
    with ui.sidebar():
        # Radio buttons to select pet type
        ui.input_radio_buttons(
            "pet_type", "Select Pet Type", list(initial_pet_data.keys()), inline=True
        )

        # Buttons to modify description
        ui.input_action_button("make_uppercase", "Uppercase")
        ui.input_action_button("make_lowercase", "Lowercase")
        ui.input_action_button("add_emoji", "Add Emoji")

    # Text area to display and edit pet description
    ui.input_text_area(
        "pet_description", "Pet Description", value=initial_pet_data["Dog"]
    )


# Reactive effect to update description based on pet type selection
@reactive.effect
def _():
    # Update text area with description for selected pet type
    ui.update_text_area("pet_description", value=initial_pet_data[input.pet_type()])


# Reactive effect to convert description to uppercase
@reactive.effect
@reactive.event(input.make_uppercase)
def _():
    current_desc = input.pet_description()
    ui.update_text_area("pet_description", value=current_desc.upper())


# Reactive effect to convert description to lowercase
@reactive.effect
@reactive.event(input.make_lowercase)
def _():
    current_desc = input.pet_description()
    ui.update_text_area("pet_description", value=current_desc.lower())


# Reactive effect to add an emoji to the description
@reactive.effect
@reactive.event(input.add_emoji)
def _():
    current_desc = input.pet_description()
    pet_type = input.pet_type()

    # Add emojis based on pet type
    emoji_map = {"Dog": "🐶 ", "Cat": "🐱 ", "Bird": "🦜 "}

    ui.update_text_area("pet_description", value=f"{emoji_map[pet_type]}{current_desc}")
