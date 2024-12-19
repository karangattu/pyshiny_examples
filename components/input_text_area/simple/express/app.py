from shiny import reactive
from shiny.express import input, ui, render

# Page title
ui.page_opts(title="Text Area Demo")

# Create a text area input
ui.input_text_area(
    "story",
    "Write your story:",
    value="Once upon a time...",
    height="200px",
    placeholder="Start writing your story here...",
    autoresize=True,
)


# Display the story with some formatting
@render.text
def formatted_story():
    story = input.story()
    return f"Your story has {len(story.split())} words:\n\n{story}"
