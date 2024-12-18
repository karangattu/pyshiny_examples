from shiny import reactive
from shiny.express import input, ui, render

ui.page_opts(title="Modal Button Demo", fillable=True)

# Add Font Awesome to use icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
    )
)

with ui.layout_columns(width=1 / 2):
    # Basic modal button
    ui.input_action_button("show_basic", "Show Basic Modal", class_="mb-3")

    # Modal button with icon
    ui.input_action_button("show_icon", "Show Modal with Icon", class_="mb-3")

    # Modal button with custom class
    ui.input_action_button(
        "show_custom", "Show Custom Styled Modal", class_="mb-3 btn-warning"
    )

    # Modal button with disabled state
    ui.input_action_button(
        "show_disabled", "Show Modal (Initially Disabled)", class_="mb-3"
    )

# Create reactive value to control disabled state
disabled_state = reactive.value(True)


@reactive.effect
def _():
    ui.update_action_button("show_disabled", disabled=disabled_state.get())


# Toggle disabled state every 3 seconds
@reactive.effect
def _():
    reactive.invalidate_later(3)
    disabled_state.set(not disabled_state.get())


@reactive.effect
@reactive.event(input.show_basic)
def _():
    m = ui.modal(
        "This is a basic modal with a simple dismiss button",
        title="Basic Modal",
        footer=ui.modal_button("Dismiss"),
    )
    ui.modal_show(m)


@reactive.effect
@reactive.event(input.show_icon)
def _():
    m = ui.modal(
        "This modal's button has an icon",
        title="Modal with Icon",
        footer=ui.modal_button(
            "Close", icon=ui.HTML('<i class="fa-solid fa-xmark"></i>')
        ),
    )
    ui.modal_show(m)


@reactive.effect
@reactive.event(input.show_custom)
def _():
    m = ui.modal(
        "This modal has a custom styled button",
        title="Custom Modal",
        footer=ui.modal_button("OK", class_="btn-success"),
    )
    ui.modal_show(m)


@reactive.effect
@reactive.event(input.show_disabled)
def _():
    m = ui.modal(
        "This modal was shown from a button that toggles disabled state",
        title="Toggle Disabled Modal",
        footer=[
            ui.modal_button("Primary", class_="btn-primary me-2"),
            ui.modal_button("Secondary", class_="btn-secondary"),
        ],
    )
    ui.modal_show(m)


# Display current state
@render.text
def show_disabled_state():
    return f"Disabled state: {disabled_state.get()}"
