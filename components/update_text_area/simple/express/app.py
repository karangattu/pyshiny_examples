from shiny import reactive
from shiny.express import input, render, ui

# Page title
ui.page_opts(title="Text Area Update Demo")

# Create a card to hold our inputs and outputs
with ui.card():
    ui.card_header("Text Area Update Demo")

    # Create a text area input
    ui.input_text_area(
        "story", "Write your story:", value="Once upon a time...", height="150px"
    )

    # Add some radio buttons to select story templates
    ui.input_radio_buttons(
        "template",
        "Select a story template:",
        {
            "adventure": "Adventure Story",
            "mystery": "Mystery Story",
            "fantasy": "Fantasy Story",
        },
    )

    # Add a button to apply the template
    ui.input_action_button("apply", "Apply Template", class_="btn-primary mt-3")


# Create a reactive effect to update the text area when button is clicked
@reactive.effect
@reactive.event(input.apply)
def _():
    template_text = {
        "adventure": """Once upon a time, a brave explorer named Alex ventured into 
        the dense jungle. With only a map and a compass...""",
        "mystery": """The old mansion stood silent in the moonlight. Detective 
        Sarah Parker approached the creaky front door, knowing that inside...""",
        "fantasy": """In the magical realm of Eldoria, where dragons soared through 
        crystal skies and wizards practiced ancient spells...""",
    }

    # Update the text area with the selected template
    ui.update_text_area(
        "story",
        value=template_text[input.template()],
        label=f"Write your {input.template()} story:",
    )


# Display the current text
@render.text
def current_text():
    return f"Current text length: {len(input.story())} characters"
