from shiny import reactive
from shiny.express import input, ui, render

# Page options for title
ui.page_opts(title="Update Accordion Panel Demo")

# Add Font Awesome CSS for icons in the head section
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
    )
)

# Create a container for better layout
with ui.layout_column_wrap(width=1):
    # Create an action button to trigger the update
    ui.input_action_button(
        "update_btn", "Update Panel Content", class_="btn-primary mb-3"
    )

    # Create an accordion with a panel that we'll update
    with ui.accordion(id="acc1", open=True):
        with ui.accordion_panel("Original Title", value="panel1"):
            ui.markdown("This is the original content")

    # Show the current state of the accordion
    @render.text
    def current_state():
        return f"Current accordion state: {input.acc1()}"


# Effect to update the accordion panel when button is clicked
@reactive.effect
@reactive.event(input.update_btn)
def _():
    ui.update_accordion_panel(
        id="acc1",
        target="panel1",
        title="Updated Title",
        value="new_value",
        icon=ui.tags.i(class_="fa-solid fa-star"),
        show=True,
    )
