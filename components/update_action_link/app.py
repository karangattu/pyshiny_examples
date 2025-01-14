from shiny import reactive
from shiny.express import input, render, ui

# Add Font Awesome to the app
ui.page_opts(
    title="Action Link Demo",
    head=ui.tags.head(
        ui.tags.link(
            rel="stylesheet",
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css",
        )
    ),
)

with ui.layout_column_wrap(width=1 / 2):
    # Create a card for the action link
    with ui.card(height="200px"):
        ui.card_header("Action Link")
        # Create the initial action link
        ui.input_action_link(
            id="my_link",
            label="Click me to update",
        )

        # Display current state of the action link
        @render.text
        def link_state():
            return f"Link has been clicked {input.my_link()} times"

    # Create a card for the update button
    with ui.card(height="200px"):
        ui.card_header("Controls")
        # Button to trigger updates
        ui.input_action_button("update", "Update the action link", class_="btn-primary")


# Effect to handle updating the action link
@reactive.effect
@reactive.event(input.update)
def _():
    # Update the action link with new label and icon
    ui.update_action_link(
        id="my_link",
        label=f"Updated {input.update()} times",
        icon=ui.tags.i(class_="fa-solid fa-arrow-right"),
    )
