from shiny import reactive
from shiny.express import input, render, ui

# Set page options
ui.page_opts(title="Modal Demo", fillable=True)

# Create a card to hold the buttons
with ui.card():
    ui.card_header("Modal Controls")

    # Action buttons for showing/removing modal
    with ui.layout_column_wrap(width="200px"):
        ui.input_action_button("show", "Show Modal", class_="btn-primary")
        ui.input_action_button("remove", "Remove Modal", class_="btn-secondary")


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
            ui.input_action_button("remove_from_modal", "Remove", class_="btn-primary"),
        ],
    )
    ui.modal_show(m)


# Effect to remove modal when either remove button is clicked
@reactive.effect
@reactive.event(input.remove, input.remove_from_modal)
def remove_modal():
    ui.modal_remove()


# Add some content below
with ui.card():
    ui.card_header("Instructions")
    """
    Click 'Show Modal' to display a modal dialog.
    
    The modal can be removed in three ways:
    1. Click the 'Close' button in the modal
    2. Click the 'Remove' button in the modal  
    3. Click the 'Remove Modal' button on this page
    
    The modal cannot be closed by clicking outside or pressing ESC 
    since easy_close=False.
    """
