from shiny import reactive
from shiny.express import input, ui, render
import random
import string


# Generate some synthetic data
def generate_random_text(length=10):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


# Set page options
ui.page_opts(title="Input Text Showcase", fillable=True)

# Sidebar with various input_text configurations
with ui.sidebar():
    # Basic text input
    ui.input_text("basic_text", "Basic Text Input", value="Default Value")

    # Text input with placeholder
    ui.input_text(
        "placeholder_text",
        "Text with Placeholder",
        placeholder="Enter some text here...",
    )

    # Text input with width
    ui.input_text("width_text", "Text Input with Width", width="100%")

    # Text input with autocomplete
    ui.input_text(
        "autocomplete_text", "Text Input with Autocomplete", autocomplete="on"
    )

    # Text input with spell check
    ui.input_text("spellcheck_text", "Text Input with Spellcheck", spellcheck="true")

# Main panel to display input details
with ui.layout_columns():
    # Card to show basic text input details
    with ui.card():
        ui.card_header("Basic Text Input Details")

        @render.text
        def basic_text_details():
            return f"""
            Current Value: {input.basic_text()}
            Length: {len(input.basic_text())}
            """

    # Card to show placeholder text input details
    with ui.card():
        ui.card_header("Placeholder Text Input Details")

        @render.text
        def placeholder_text_details():
            return f"""
            Current Value: {input.placeholder_text()}
            Placeholder: {input.placeholder_text.label}
            """

    # Card to show width text input details
    with ui.card():
        ui.card_header("Width Text Input Details")

        @render.text
        def width_text_details():
            return f"""
            Current Value: {input.width_text()}
            Width: 100%
            """

    # Card to show autocomplete text input details
    with ui.card():
        ui.card_header("Autocomplete Text Input Details")

        @render.text
        def autocomplete_text_details():
            return f"""
            Current Value: {input.autocomplete_text()}
            Autocomplete: On
            """

    # Card to show spellcheck text input details
    with ui.card():
        ui.card_header("Spellcheck Text Input Details")

        @render.text
        def spellcheck_text_details():
            return f"""
            Current Value: {input.spellcheck_text()}
            Spellcheck: Enabled
            """


# Add a section to demonstrate dynamic updates
with ui.card():
    ui.card_header("Dynamic Text Input Update")

    ui.input_action_button("update_text", "Update Text Inputs")

    @reactive.effect
    @reactive.event(input.update_text)
    def _():
        # Dynamically update text inputs
        ui.update_text("basic_text", value=generate_random_text())
        ui.update_text(
            "placeholder_text",
            placeholder=f"Random placeholder: {generate_random_text()}",
        )
