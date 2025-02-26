from shiny import App, reactive, ui

# Define the UI
app_ui = ui.page_fillable(
    # Add Font Awesome CSS
    ui.head_content(
        ui.HTML(
            '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css>'
        )
    ),
    # Create a container for the button
    ui.card(
        ui.card_header("Modal Demo"),
        ui.input_action_button("show", "Show Modal", class_="btn-primary m-3"),
    ),
    # Add instructions card
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Instructions"),
            "Click the button above to show a modal with different button styles.",
            "The modal can be closed by clicking any of the buttons or clicking outside the modal.",
        ),
    ),
)


# Define the server
def server(input, output, session):
    @reactive.effect
    @reactive.event(input.show)
    def show_modal():
        modal = ui.modal(
            ui.p("This modal demonstrates different modal button configurations"),
            title="Modal Button Demo",
            easy_close=True,
            footer=[
                ui.div(
                    # Basic modal button
                    ui.modal_button("Basic Button", class_="me-2"),
                    # Modal button with icon
                    ui.modal_button(
                        ui.span(
                            ui.tags.i(class_="fa-solid fa-check me-1"),
                            "Button with Icon",
                        ),
                        class_="btn-info me-2",
                    ),
                    # Styled modal button
                    ui.modal_button("Styled Button", class_="btn-success me-2"),
                    # Full featured modal button
                    ui.modal_button(
                        ui.span(
                            ui.tags.i(class_="fa-solid fa-star me-1"),
                            "Full Featured Button",
                        ),
                        class_="btn-warning",
                        id="full_featured_btn",
                    ),
                    class_="d-flex justify-content-end",
                )
            ],
        )
        ui.modal_show(modal)


# Create and return the app
app = App(app_ui, server)
