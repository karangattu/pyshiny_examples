from shiny import reactive
from shiny.express import input, ui, render

# Page title
ui.page_opts(title="Text Input Demo")

# Create a text input
ui.input_text("name", "Enter your name:", placeholder="Type your name here")

# Create a text area input for longer text
ui.input_text_area(
    "story", "Share a short story:", placeholder="Once upon a time...", height="100px"
)


# Display the inputs
@render.text
def greeting():
    """Show greeting using text input"""
    if input.name():
        return f"Hello {input.name()}!"
    return "Please enter your name above"


@render.text
def story_stats():
    """Show stats about entered story"""
    if input.story():
        word_count = len(input.story().split())
        char_count = len(input.story())
        return f"Your story has {word_count} words and {char_count} characters"
    return "Write your story above"
