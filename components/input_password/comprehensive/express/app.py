from shiny import reactive
from shiny.express import input, ui, render

# Page title and options
ui.page_opts(title="Password Input Demo", fillable=True)

# Main layout with cards
with ui.layout_column_wrap(width="400px"):

    # Basic password input
    with ui.card(full_screen=True):
        ui.card_header("Basic Password Input")
        ui.input_password(id="pwd_basic", label="Enter Password:", value="default123")

        @render.text
        def show_basic():
            return f"Password entered: {input.pwd_basic()}"

    # Password with placeholder
    with ui.card(full_screen=True):
        ui.card_header("Password with Placeholder")
        ui.input_password(
            id="pwd_placeholder",
            label="Enter Password:",
            value="",
            placeholder="Type your secret password here",
        )

        @render.text
        def show_placeholder():
            return f"Password entered: {input.pwd_placeholder()}"

    # Password with custom width
    with ui.card(full_screen=True):
        ui.card_header("Password with Custom Width")
        ui.input_password(
            id="pwd_width", label="Enter Password:", value="", width="200px"
        )

        @render.text
        def show_width():
            return f"Password entered: {input.pwd_width()}"

    # Password with all parameters
    with ui.card(full_screen=True):
        ui.card_header("Password with All Parameters")
        ui.input_password(
            id="pwd_all",
            label="Enter Password:",
            value="secretpass",
            width="300px",
            placeholder="Enter your secure password",
        )

        @render.text
        def show_all():
            return f"Password entered: {input.pwd_all()}"


# Add a reactive effect to demonstrate password changes
@reactive.effect
def password_changed():
    if input.pwd_all():
        ui.notification_show(f"Password changed in 'All Parameters' input!", duration=3)


# Add some helpful text about the demo
ui.markdown(
    """
### Password Input Parameters Demo

This app demonstrates all possible parameters of `input_password`:

* **id**: The input identifier (required)
* **label**: The label text shown above the input (required)
* **value**: Initial value (default: '')
* **width**: CSS width of the input (e.g., '100px', '50%')
* **placeholder**: Placeholder text shown when input is empty
"""
)
