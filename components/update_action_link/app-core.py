from shiny import App, reactive, render, ui

# Define the UI
app_ui = ui.page_fluid(
    # Add Font Awesome to the app
    ui.tags.head(
        ui.tags.link(
            rel="stylesheet",
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css",
        )
    ),
    # Create layout with columns
    ui.layout_column_wrap(
        # Create a card for the action link
        ui.card(
            ui.card_header("Action Link"),
            # Create the initial action link
            ui.input_action_link(
                id="my_link",
                label="Click me to update",
            ),
            # Output for link state
            ui.output_text("link_state"),
            height="200px",
        ),
        # Create a card for the update button
        ui.card(
            ui.card_header("Controls"),
            # Button to trigger updates
            ui.input_action_button(
                "update", "Update the action link", class_="btn-primary"
            ),
            height="200px",
        ),
        width=1 / 2,
    ),
)


# Define the server
def server(input, output, session):
    # Display current state of the action link
    @output
    @render.text
    def link_state():
        return f"Link has been clicked {input.my_link()} times"

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


# Create and return the app
app = App(app_ui, server)
