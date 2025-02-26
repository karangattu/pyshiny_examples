from shiny import App, reactive, ui

# Define the UI
app_ui = ui.page_fillable(
    # Create a card to hold the buttons
    ui.card(
        ui.card_header("Modal Controls"),
        ui.layout_column_wrap(
            ui.input_action_button("show", "Show Modal", class_="btn-primary"),
            ui.input_action_button("remove", "Remove Modal", class_="btn-secondary"),
            width="200px",
        ),
    ),
    # Add instructions card
    ui.card(
        ui.card_header("Instructions"),
        """
        Click 'Show Modal' to display a modal dialog.
        
        The modal can be removed in three ways:
        1. Click the 'Close' button in the modal
        2. Click the 'Remove' button in the modal  
        3. Click the 'Remove Modal' button on this page
        
        The modal cannot be closed by clicking outside or pressing ESC 
        since easy_close=False.
        """,
    ),
)


# Define the server
def server(input, output, session):
    # Effect to show modal when show button is clicked
    @reactive.effect
    @reactive.event(input.show)
    def show_modal():
        m = ui.modal(
            "This is a modal dialog that can be removed programmatically.",
            title="Sample Modal",
            easy_close=False,
            footer=[
                ui.modal_button("Close", class_="btn-secondary"),
                ui.input_action_button(
                    "remove_from_modal", "Remove", class_="btn-primary"
                ),
            ],
        )
        ui.modal_show(m)

    # Effect to remove modal when either remove button is clicked
    @reactive.effect
    @reactive.event(input.remove, input.remove_from_modal)
    def remove_modal():
        ui.modal_remove()


# Create and return the app
app = App(app_ui, server)
