from shiny import reactive
from shiny.express import input, ui, render
import random
import string


# Generate a sample text for initial value
def generate_random_text(length=100):
    """Generate a random text string."""
    return "".join(
        random.choices(string.ascii_letters + string.punctuation + " ", k=length)
    )


# Page setup with full width and title
ui.page_opts(title="Text Area Input Showcase", full_width=True)

# Sidebar for configuration
with ui.sidebar():
    # Demonstrate various parameters of input_text_area
    ui.input_text_area(
        id="basic_textarea",
        label="Basic Text Area",
        value=generate_random_text(),
        placeholder="Enter your text here...",
    )

    ui.input_text_area(
        id="custom_textarea",
        label="Customized Text Area",
        value=generate_random_text(200),
        placeholder="Enter a longer text...",
        width="400px",  # Custom width
        height="150px",  # Custom height
        rows=5,  # Specify number of visible rows
        cols=50,  # Specify number of visible columns
        resize="vertical",  # Allow vertical resizing
    )

    ui.input_text_area(
        id="advanced_textarea",
        label="Advanced Text Area",
        value=generate_random_text(250),
        placeholder="Enter text with special settings...",
        autoresize=True,  # Automatically resize based on content
        spellcheck="true",  # Enable browser spell checking
        autocomplete="on",  # Enable browser autocomplete
    )

# Main content area to display text area details
with ui.layout_columns():
    # Display basic text area details
    with ui.card():
        ui.card_header("Basic Text Area Details")

        @render.text
        def basic_details():
            return f"""
            Text Value: {input.basic_textarea()}
            Length: {len(input.basic_textarea())} characters
            """

    # Display customized text area details
    with ui.card():
        ui.card_header("Customized Text Area Details")

        @render.text
        def custom_details():
            return f"""
            Text Value: {input.custom_textarea()}
            Length: {len(input.custom_textarea())} characters
            Rows: 5
            Columns: 50
            Resize: Vertical
            """

    # Display advanced text area details
    with ui.card():
        ui.card_header("Advanced Text Area Details")

        @render.text
        def advanced_details():
            return f"""
            Text Value: {input.advanced_textarea()}
            Length: {len(input.advanced_textarea())} characters
            Autoresize: Enabled
            Spellcheck: Enabled
            Autocomplete: Enabled
            """


# Reactive effects to demonstrate dynamic updates
@reactive.effect
@reactive.event(input.basic_textarea)
def _():
    # Optional: Add a notification when text changes
    ui.notification_show(
        f"Basic Text Area updated. New length: {len(input.basic_textarea())}",
        duration=3,
    )
