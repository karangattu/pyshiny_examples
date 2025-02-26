from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Modal Button Demo", fillable=True)

# Add Font Awesome CSS
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
    )
)

# Create a container for the button
with ui.card():
    ui.card_header("Modal Demo")
    ui.input_action_button("show", "Show Modal", class_="btn-primary m-3")


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
                        ui.tags.i(class_="fa-solid fa-check me-1"), "Button with Icon"
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


# Add some content to the page
with ui.layout_column_wrap():
    with ui.card():
        ui.card_header("Instructions")
        "Click the button above to show a modal with different button styles."
        "The modal can be closed by clicking any of the buttons or clicking outside the modal."
