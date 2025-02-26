from shiny import reactive
from shiny.express import input, ui, render

ui.page_opts(fillable=True)

# Add Font Awesome for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">'
    )
)

with ui.layout_column_wrap(width="100%"):
    with ui.card():
        ui.card_header("Modal Examples")
        with ui.card_body():
            # Create buttons to demonstrate different modal configurations
            ui.input_action_button("show_small", "Show Small Modal", class_="me-2 mb-2")
            ui.input_action_button(
                "show_medium", "Show Medium Modal", class_="me-2 mb-2"
            )
            ui.input_action_button("show_large", "Show Large Modal", class_="me-2 mb-2")
            ui.input_action_button(
                "show_xl", "Show Extra Large Modal", class_="me-2 mb-2"
            )
            ui.input_action_button(
                "show_custom", "Show Custom Modal", class_="me-2 mb-2"
            )


@reactive.effect
@reactive.event(input.show_small)
def show_small_modal():
    m = ui.modal(
        "This is a small modal with minimal content.",
        title="Small Modal",
        size="s",
        easy_close=True,
        footer=ui.modal_button("Close", class_="btn-secondary"),
    )
    ui.modal_show(m)


@reactive.effect
@reactive.event(input.show_medium)
def show_medium_modal():
    m = ui.modal(
        "This is a medium modal (default size) with a title and footer.",
        title="Medium Modal",
        size="m",
        easy_close=False,
        footer=[
            ui.modal_button("Cancel", class_="btn-secondary me-2"),
            ui.modal_button("OK", class_="btn-primary"),
        ],
    )
    ui.modal_show(m)


@reactive.effect
@reactive.event(input.show_large)
def show_large_modal():
    m = ui.modal(
        "This is a large modal with an icon in the title.",
        title=ui.tags.div(
            ui.tags.i(class_="fa-solid fa-circle-info me-2"), "Large Modal with Icon"
        ),
        size="l",
        easy_close=True,
        footer=ui.modal_button("Got it!"),
    )
    ui.modal_show(m)


@reactive.effect
@reactive.event(input.show_xl)
def show_xl_modal():
    m = ui.modal(
        "This is an extra large modal with no fade animation.",
        title="Extra Large Modal",
        size="xl",
        fade=False,
        footer=ui.modal_button("Close"),
    )
    ui.modal_show(m)


@reactive.effect
@reactive.event(input.show_custom)
def show_custom_modal():
    m = ui.modal(
        ui.tags.div(
            ui.tags.h4("Custom Content"),
            ui.tags.p("This modal demonstrates:"),
            ui.tags.ul(
                ui.tags.li("Custom HTML content"),
                ui.tags.li("Custom styling"),
                ui.tags.li("Multiple footer buttons"),
                ui.tags.li("No easy close"),
            ),
            style="color: #2c3e50;",
        ),
        title=ui.tags.div(
            ui.tags.i(class_="fa-solid fa-gear me-2"),
            "Custom Modal",
            style="color: #3498db;",
        ),
        size="m",
        easy_close=False,
        footer=[
            ui.modal_button("Cancel", class_="btn-secondary me-2"),
            ui.modal_button("Save", class_="btn-success"),
        ],
    )
    ui.modal_show(m)
