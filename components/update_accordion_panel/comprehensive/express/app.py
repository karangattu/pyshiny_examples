from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Accordion Panel Demo", fillable=True)

# Create some initial content
with ui.accordion(id="acc", open=["Section A"], multiple=True):
    for letter in "ABCDE":
        with ui.accordion_panel(f"Section {letter}", value=f"sec_{letter}"):
            f"Initial content for section {letter}"

# Controls for updating accordion panels
with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_text("new_title", "New Title", value="Updated Section")
        ui.input_text("new_value", "New Value", value="new_value")
        ui.input_text_area(
            "new_content", "New Content", value="This is updated content"
        )
        ui.input_select(
            "target_section",
            "Select Section to Update",
            choices=[f"sec_{letter}" for letter in "ABCDE"],
        )
        ui.input_switch("show_panel", "Show Panel", value=True)
        ui.input_action_button("update_btn", "Update Panel")
        ui.hr()
        ui.markdown(
            """
        ### Parameters being demonstrated:
        - id: The accordion's ID
        - target: The panel's value to update
        - body: New content
        - title: New title
        - value: New value
        - show: Whether to show/hide the panel
        """
        )


# Show current accordion state
@render.text
def current_state():
    return f"Currently selected accordion panel: {input.acc()}"


# Update accordion panel when button is clicked
@reactive.effect
@reactive.event(input.update_btn)
def _():
    # Fixed the update_accordion_panel call by placing body content first
    ui.update_accordion_panel(
        "acc",  # id
        input.target_section(),  # target
        input.new_content(),  # body content
        title=input.new_title(),
        value=input.new_value(),
        show=input.show_panel(),
    )
    # Show notification of update
    ui.notification_show(
        f"Updated panel {input.target_section()} with new settings", duration=3
    )


# Add some styling
ui.include_css(
    """
    .sidebar {
        background-color: #f8f9fa;
        padding: 1rem;
    }
    .accordion {
        margin-top: 1rem;
    }
"""
)
