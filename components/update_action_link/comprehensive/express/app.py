from shiny import reactive, render
from shiny.express import input, ui

# Synthetic data generation
import random
import string


# Generate random words for link labels
def generate_random_word(length=5):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


# Generate random icons
ICONS = ["🚀", "🌟", "🎉", "🔥", "🌈", "🍀", "🌞", "🚲", "🎸", "🍕"]

ui.page_opts(title="Update Action Link Showcase")

with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_action_button("update_link", "Update Action Link")
        ui.input_radio_buttons("icon_choice", "Choose Icon", ICONS, selected=ICONS[0])
        ui.input_text("custom_label", "Custom Label", value="Original Link")

    with ui.card():
        ui.card_header("Action Link Demonstration")
        ui.input_action_link("demo_link", "Initial Link")

        @render.text
        def link_details():
            return f"Current link value: {input.demo_link()}"


# Reactive effect to update the action link
@reactive.effect
@reactive.event(input.update_link)
def _():
    # Demonstrate various update scenarios

    # 1. Update label
    new_label = generate_random_word(random.randint(3, 8))

    # 2. Update icon (from radio button selection)
    selected_icon = input.icon_choice()

    # 3. Optional: Custom label from text input
    custom_label = input.custom_label()

    # Update the action link with different parameters
    ui.update_action_link(
        "demo_link",
        label=custom_label if custom_label else new_label,
        icon=selected_icon,
    )
