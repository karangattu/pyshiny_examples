from shiny import reactive
from shiny.express import input, ui, render

# Synthetic data for demonstration
pet_types = ["Dog", "Cat", "Bird", "Hamster", "Fish"]
pet_genders = ["Male", "Female"]

ui.page_opts(title="Text Area Update Demonstration")

with ui.layout_sidebar():
    with ui.sidebar():
        # Input controls to demonstrate different update scenarios
        ui.input_radio_buttons("pet_type", "Pet Type", choices=pet_types, inline=True)

        ui.input_radio_buttons(
            "pet_gender", "Pet Gender", choices=pet_genders, inline=True
        )

        ui.input_action_button("update_btn", "Update Text Area")

        ui.input_action_button("reset_btn", "Reset Text Area")

    # Text area with initial content
    ui.input_text_area(
        "pet_description",
        "Pet Description",
        value="Enter pet details here...",
        placeholder="Describe your pet",
        width="100%",
        rows=5,
    )

    # Display current text area state
    @render.text
    def display_current_state():
        return f"""
        Current Text Area State:
        - Value: {input.pet_description()}
        - Pet Type: {input.pet_type() or 'Not selected'}
        - Pet Gender: {input.pet_gender() or 'Not selected'}
        """


# Reactive effect to update text area based on selections
@reactive.effect
@reactive.event(input.update_btn)
def update_text_area():
    pet_type = input.pet_type() or "Unknown"
    pet_gender = input.pet_gender() or "Unknown"

    # Demonstrate multiple update parameters
    ui.update_text_area(
        "pet_description",
        # Update label dynamically
        label=f"{pet_type}'s Description",
        # Update value based on selections
        value=f"I have a {pet_gender.lower()} {pet_type.lower()} who is very special.",
        # Update placeholder text
        placeholder=f"Tell me more about your {pet_type.lower()}",
        # Optional: You could add width or other parameters if needed
        width="100%",
    )


# Reactive effect to reset text area
@reactive.effect
@reactive.event(input.reset_btn)
def reset_text_area():
    ui.update_text_area(
        "pet_description",
        label="Pet Description",
        value="Enter pet details here...",
        placeholder="Describe your pet",
    )
