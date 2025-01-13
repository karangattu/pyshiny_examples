from shiny import reactive
from shiny.express import input, ui, render

# Page options and Font Awesome CSS
ui.page_opts(title="Tooltip Demo", fillable=True)
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
    )
)

# Create a layout with columns
with ui.layout_columns():
    # First column with controls
    with ui.card():
        ui.card_header("Tooltip Controls")
        ui.input_action_button("btn_show", "Show tooltip", class_="me-2")
        ui.input_action_button("btn_hide", "Hide tooltip", class_="me-2")
        ui.input_action_button("btn_update", "Update tooltip content", class_="me-2")
        ui.input_numeric("counter", "Update counter", value=1)

    # Second column with tooltip demo
    with ui.card():
        ui.card_header("Tooltip Demo")

        # Create a tooltip with an icon
        with ui.tooltip(id="tooltip_demo", placement="right"):
            ui.span(
                ui.tags.i(class_="fa-solid fa-circle-info", style="font-size: 2rem;"),
                style="cursor: pointer;",
            )
            "Initial tooltip content"

# Counter for content updates
content_counter = reactive.value(1)


@reactive.effect
@reactive.event(input.btn_show)
def show_tooltip():
    ui.update_tooltip("tooltip_demo", show=True)
    ui.notification_show("Tooltip shown", type="message")


@reactive.effect
@reactive.event(input.btn_hide)
def hide_tooltip():
    ui.update_tooltip("tooltip_demo", show=False)
    ui.notification_show("Tooltip hidden", type="warning")


@reactive.effect
@reactive.event(input.btn_update)
def update_tooltip_content():
    new_content = [
        ui.h4(f"Updated Content #{input.counter()}"),
        ui.p("This is a dynamic tooltip with:"),
        ui.tags.ul(
            ui.tags.li("Multiple elements"),
            ui.tags.li("HTML formatting"),
            ui.tags.li(ui.tags.i(class_="fa-solid fa-check"), " Icons"),
        ),
    ]

    # Update tooltip with new content and show it
    ui.update_tooltip("tooltip_demo", *new_content, show=True)
    ui.notification_show(f"Content updated to #{input.counter()}", type="message")


# Display current tooltip state
@render.text
def tooltip_status():
    return f"Tooltip visibility can be checked via input.tooltip_demo(): {input.tooltip_demo()}"
