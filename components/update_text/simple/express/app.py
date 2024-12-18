from shiny import reactive
from shiny.express import input, render, ui

# Create simple UI with text input and radio buttons
ui.input_radio_buttons(
    "pet_type", "Select pet type:", ["Dog", "Cat", "Bird"], inline=True
)

ui.input_text("pet_name", "Enter pet name:", value="Buddy")


# Effect to update the text input label based on pet type selection
@reactive.effect
def _():
    ui.update_text(
        "pet_name",
        label=(
            f"Enter {input.pet_type()}'s name:"
            if input.pet_type()
            else "Enter pet name:"
        ),
    )


# Display the current pet name
@render.text
def show_name():
    return f"Current name: {input.pet_name()}"
