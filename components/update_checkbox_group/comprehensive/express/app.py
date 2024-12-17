from shiny import reactive
from shiny.express import input, ui, render

# Create synthetic data for demonstration
pet_categories = {
    "Mammals": ["Dog", "Cat", "Horse", "Rabbit", "Elephant"],
    "Birds": ["Parrot", "Eagle", "Penguin", "Owl", "Sparrow"],
    "Reptiles": ["Snake", "Lizard", "Crocodile", "Turtle", "Chameleon"],
}

ui.page_opts(title="Checkbox Group Update Demo")

with ui.layout_sidebar():
    with ui.sidebar():
        # Initial checkbox group with basic choices
        ui.input_checkbox_group(
            "initial_pets",
            "Select Initial Pets",
            choices=["Dog", "Cat", "Parrot", "Snake"],
            selected=["Dog", "Cat"],
        )

        # Controls for demonstrating update parameters
        ui.input_action_button("update_btn", "Update Checkbox Group")

        # Additional controls to demonstrate different update scenarios
        ui.input_radio_buttons(
            "category_select", "Choose Category", choices=list(pet_categories.keys())
        )

        ui.input_checkbox("inline_toggle", "Toggle Inline", value=False)

    # Output area to show current state
    with ui.card():
        ui.card_header("Checkbox Group State")

        @render.text
        def checkbox_state():
            return f"Selected: {input.initial_pets() or 'None'}"


# Reactive effect to update checkbox group
@reactive.effect
@reactive.event(input.update_btn)
def update_checkbox_group():
    # Demonstrate various update parameters
    ui.update_checkbox_group(
        # Basic id parameter
        id="initial_pets",
        # Label parameter - dynamically change label
        label=f"Pets in {input.category_select()} Category",
        # Choices parameter - dynamically change choices based on selected category
        choices=pet_categories[input.category_select()],
        # Selected parameter - select first two items
        selected=pet_categories[input.category_select()][:2],
        # Inline parameter - toggle based on checkbox
        inline=input.inline_toggle(),
    )


# Optional: Add a render to show current state after update
@render.text
def update_details():
    return (
        f"Category: {input.category_select()}\n"
        f"Inline: {input.inline_toggle()}\n"
        f"Current Selection: {input.initial_pets() or 'None'}"
    )
