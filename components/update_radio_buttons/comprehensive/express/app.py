from shiny import reactive
from shiny.express import input, ui, render

# Create synthetic data for demonstration
pet_types = {
    "dog": "🐶 Dog",
    "cat": "🐱 Cat",
    "bird": "🦜 Bird",
    "fish": "🐠 Fish",
    "reptile": "🦎 Reptile",
}

pet_sizes = {
    "small": "Small (0-10 lbs)",
    "medium": "Medium (11-50 lbs)",
    "large": "Large (51+ lbs)",
}

ui.page_opts(title="Radio Button Update Demo")

with ui.layout_sidebar():
    with ui.sidebar():
        # Control buttons for demonstrating different update scenarios
        ui.input_action_button("update_label", "Update Label")
        ui.input_action_button("update_choices", "Update Choices")
        ui.input_action_button("update_selected", "Update Selected")
        ui.input_action_button("update_inline", "Toggle Inline")

        # Initial radio button input
        ui.input_radio_buttons(
            "pet_type", "Select Pet Type", choices=pet_types, selected="dog"
        )

        ui.input_radio_buttons(
            "pet_size", "Select Pet Size", choices=pet_sizes, selected="small"
        )

    with ui.card():
        ui.card_header("Radio Button Update Demonstration")

        @render.text
        def display_selections():
            return f"""
            Pet Type: {input.pet_type()}
            Pet Size: {input.pet_size()}
            """


# Reactive effects to demonstrate different update scenarios
@reactive.effect
@reactive.event(input.update_label)
def _():
    # Dynamically update the label
    ui.update_radio_buttons(
        "pet_type", label=f"Select Pet Type (Update {input.update_label()})"
    )


@reactive.effect
@reactive.event(input.update_choices)
def _():
    # Dynamically update the choices
    new_choices = {k: f"{v} (Updated)" for k, v in pet_types.items()}
    ui.update_radio_buttons("pet_type", choices=new_choices)


@reactive.effect
@reactive.event(input.update_selected)
def _():
    # Dynamically update the selected value
    current_choices = list(pet_types.keys())
    current_index = current_choices.index(input.pet_type())
    new_selected = current_choices[(current_index + 1) % len(current_choices)]

    ui.update_radio_buttons("pet_type", selected=new_selected)


@reactive.effect
@reactive.event(input.update_inline)
def _():
    # Toggle inline display
    current_inline = input.pet_type.get_inline()
    ui.update_radio_buttons("pet_type", inline=not current_inline)
