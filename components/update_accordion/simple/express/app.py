from shiny import reactive
from shiny.express import input, ui

# Create synthetic data for the accordion
sections_data = {
    "Section A": "This is the content for Section A. It provides some interesting information about the first section.",
    "Section B": "Section B contains details about a different topic. Learn more about its unique characteristics here.",
    "Section C": "Explore the fascinating world of Section C. This section reveals intriguing insights.",
    "Section D": "Section D rounds out our collection with its own special narrative and perspective.",
}

# Page setup
ui.page_opts(title="Accordion Update Demo")

# Create an accordion with multiple sections
with ui.accordion(id="demo_accordion", multiple=True):
    for title, content in sections_data.items():
        with ui.accordion_panel(title, value=f"panel_{title}"):
            content

# Sidebar with controls
with ui.sidebar():
    ui.input_radio_buttons(
        "section_select", "Select Section to Update", list(sections_data.keys())
    )
    ui.input_text("new_content", "New Content")
    ui.input_action_button("update_btn", "Update Section")


# Reactive effect to update accordion panel
@reactive.effect
@reactive.event(input.update_btn)
def _():
    # Update the selected section with new content
    ui.update_accordion_panel(
        "demo_accordion",
        f"panel_{input.section_select()}",
        input.new_content(),
        title=f"Updated {input.section_select()}",
    )


# Optional: Show current selected section
@reactive.effect
def _():
    ui.notification_show(f"You selected: {input.section_select()}")
