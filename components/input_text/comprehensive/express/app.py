from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Text Input Demo", fillable=True)

with ui.layout_columns():
    # Basic text input
    ui.input_text("text1", "Basic Text Input", value="Default text", width="300px")

    # Text input with placeholder
    ui.input_text(
        "text2",
        "Text Input with Placeholder",
        value="",
        placeholder="Enter text here...",
        width="300px",
    )

    # Text input with autocomplete
    ui.input_text(
        "text3",
        "Text Input with Autocomplete",
        value="",
        placeholder="Try typing 'John'",
        autocomplete="name",
        width="300px",
    )

    # Text input with spellcheck enabled
    ui.input_text(
        "text4",
        "Text Input with Spellcheck",
        value="Try mispeling words",
        spellcheck="true",
        width="300px",
    )

    # Text input with spellcheck disabled
    ui.input_text(
        "text5",
        "Text Input with Spellcheck Disabled",
        value="Speling mistakes wont be highlighted",
        spellcheck="false",
        width="300px",
    )

# Display results in a card
with ui.card():
    ui.card_header("Input Values")

    @render.ui
    def show_values():
        return ui.tags.div(
            ui.tags.p(f"Basic Input: {input.text1()}"),
            ui.tags.p(f"Placeholder Input: {input.text2()}"),
            ui.tags.p(f"Autocomplete Input: {input.text3()}"),
            ui.tags.p(f"Spellcheck Input: {input.text4()}"),
            ui.tags.p(f"No Spellcheck Input: {input.text5()}"),
        )


# Add a reactive effect to demonstrate input updates
with ui.card():
    ui.card_header("Update Text Input Demo")
    ui.input_action_button("update_btn", "Update Text Inputs")

    @reactive.effect
    @reactive.event(input.update_btn)
    def _():
        # Update each text input with new values
        ui.update_text("text1", value="Updated text", label="Updated Basic Text Input")
        ui.update_text("text2", placeholder="Updated placeholder...")
        ui.update_text("text3", value="John Doe")
        ui.update_text("text4", value="New spellcheck text")
        ui.update_text("text5", value="New text without spellcheck")
