from shiny import reactive
from shiny.express import input, render, ui

# Create some sample data
data = {
    "Page A": "This is content for Page A",
    "Page B": "This is content for Page B",
    "Page C": "This is content for Page C",
}

# Add action links for navigation
ui.input_action_link("link_a", "Go to Page A", class_="me-3")
ui.input_action_link("link_b", "Go to Page B", class_="me-3")
ui.input_action_link("link_c", "Go to Page C")

ui.hr()


# Display content based on which link was clicked
@render.text
@reactive.event(input.link_a, input.link_b, input.link_c)
def content():
    if input.link_a():
        return data["Page A"]
    elif input.link_b():
        return data["Page B"]
    elif input.link_c():
        return data["Page C"]
    else:
        return "Click a link above to see content"
