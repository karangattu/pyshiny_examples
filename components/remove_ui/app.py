from shiny import reactive
from shiny.express import input, ui, render

ui.page_opts(title="Dynamic UI Example")

with ui.layout_column_wrap():
    with ui.card():
        ui.card_header("Controls")
        ui.input_action_button("add", "Add Content", class_="me-2")
        ui.input_action_button("remove", "Remove Content")

    with ui.card():
        ui.card_header("Dynamic Content Area")
        # Container for dynamically added/removed content
        ui.div(id="content_container")


@reactive.effect
@reactive.event(input.add)
def add_content():
    # Insert some UI elements that we can remove later
    ui.insert_ui(
        ui.div(
            ui.h4("Sample Content"),
            ui.p("This is some content that can be removed."),
            id="removable_content",
        ),
        selector="#content_container",
        where="beforeEnd",
    )


@reactive.effect
@reactive.event(input.remove)
def remove_content():
    # Remove the content when the remove button is clicked
    ui.remove_ui(
        selector="#removable_content",  # The selector to find elements to remove
        multiple=False,  # Remove only the first match
        immediate=False,  # Wait for other updates to complete
    )
