from shiny import reactive
from shiny.express import input, ui, render

# Synthetic data generation
import random
import string


# Generate a list of pet names
def generate_pet_names(num_names=10):
    prefixes = [
        "Fluffy",
        "Whiskers",
        "Shadow",
        "Mittens",
        "Buddy",
        "Luna",
        "Max",
        "Charlie",
        "Bella",
        "Rocky",
    ]
    suffixes = [
        "Jr",
        "Senior",
        "the Great",
        "Mighty",
        "Tiny",
        "Brave",
        "Wise",
        "Noble",
        "Swift",
        "Clever",
    ]

    return [
        f"{random.choice(prefixes)} {random.choice(suffixes)}" for _ in range(num_names)
    ]


# Generate a list of pet types
pet_types = ["Dog", "Cat", "Bird", "Hamster", "Rabbit", "Fish", "Turtle", "Lizard"]


# Generate a list of random descriptions
def generate_descriptions(num_descriptions=10):
    adjectives = [
        "Playful",
        "Lazy",
        "Energetic",
        "Curious",
        "Shy",
        "Friendly",
        "Intelligent",
        "Mischievous",
    ]
    return [
        f"{random.choice(adjectives)} {random.choice(pet_types)}"
        for _ in range(num_descriptions)
    ]


# Preset data
pet_names = generate_pet_names()
descriptions = generate_descriptions()

# App UI
ui.page_opts(title="Text Input Update Demonstration")

with ui.layout_column_wrap(width=1 / 2):
    # Original text input
    ui.input_text("original_name", "Original Pet Name", value=pet_names[0])

    # Demonstration text inputs
    ui.input_text("update_label", "Update Label", placeholder="Enter new label")
    ui.input_text("update_value", "Update Value", placeholder="Enter new value")
    ui.input_text(
        "update_placeholder", "Update Placeholder", placeholder="Enter new placeholder"
    )

# Action buttons for demonstrations
with ui.layout_column_wrap():
    ui.input_action_button("update_label_btn", "Update Label")
    ui.input_action_button("update_value_btn", "Update Value")
    ui.input_action_button("update_placeholder_btn", "Update Placeholder")
    ui.input_action_button("reset_btn", "Reset")


# Render output to show current state
@render.text
def current_state():
    return f"""
    Current Original Name Input:
    - Label: Original Pet Name
    - Value: {input.original_name()}
    - Placeholder: {input.original_name.attrs.get('placeholder', 'No placeholder')}
    """


# Update label reactive effect
@reactive.effect
@reactive.event(input.update_label_btn)
def _():
    new_label = input.update_label() if input.update_label() else "Original Pet Name"
    ui.update_text("original_name", label=new_label)


# Update value reactive effect
@reactive.effect
@reactive.event(input.update_value_btn)
def _():
    new_value = (
        input.update_value() if input.update_value() else random.choice(pet_names)
    )
    ui.update_text("original_name", value=new_value)


# Update placeholder reactive effect
@reactive.effect
@reactive.event(input.update_placeholder_btn)
def _():
    new_placeholder = (
        input.update_placeholder()
        if input.update_placeholder()
        else random.choice(descriptions)
    )
    ui.update_text("original_name", placeholder=new_placeholder)


# Reset button reactive effect
@reactive.effect
@reactive.event(input.reset_btn)
def _():
    ui.update_text(
        "original_name",
        label="Original Pet Name",
        value=pet_names[0],
        placeholder="Enter pet name",
    )
