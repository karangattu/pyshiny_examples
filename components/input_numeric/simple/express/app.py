from shiny import reactive
from shiny.express import input, ui, render

# Page title
ui.page_opts(title="Numeric Input Demo")

# Input numeric control
ui.input_numeric("num", "Enter a number", value=5, min=0, max=100, step=1)


# Show current value
@render.text
def current_value():
    return f"Current value is: {input.num()}"


# Show value squared
@render.text
def squared():
    return f"Value squared is: {input.num() ** 2}"


# Show value cubed
@render.text
def cubed():
    return f"Value cubed is: {input.num() ** 3}"
