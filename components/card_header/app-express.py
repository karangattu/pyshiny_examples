from shiny import reactive
from shiny.express import input, ui, render

# Add Font Awesome for icons in the head section
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">'
    )
)

# Set page title
ui.page_opts(title="Card Header Demo", fillable=True)

# Create a card with all possible card_header parameters
with ui.card(height="500px", id="demo_card"):
    # Basic header with title as string
    ui.card_header("Basic Header")
    ui.p("This header shows the simplest usage with just a text string")

    with ui.card(height="100px", id="custom_card"):
        # Header with custom container (h3 instead of default div)
        ui.card_header("Custom Container Header", container=ui.tags.h3)
        ui.p("This header uses a custom h3 container instead of the default div")

    with ui.card(height="100px", id="complex_card"):
        # Header with multiple elements and custom HTML attributes
        ui.card_header(
            ui.tags.span("Complex Header with ", style="color: blue;"),
            ui.tags.strong("Multiple Elements"),
            class_="text-center",
            style="background-color: #f8f9fa;",
        )
        ui.p("This header demonstrates using multiple elements and custom styling")

    with ui.card(height="100px", id="icon_card"):
        # Header with icon and custom styling
        ui.card_header(
            ui.tags.i(class_="fa-solid fa-shield-halved", style="font-size: 2rem;"),
            " Header with Icon",
            container=ui.tags.h4,
            style="color: green;",
        )
        ui.p("This header shows how to include a Font Awesome icon")


@render.ui
def description():
    return ui.p(
        "This app demonstrates different ways to use ui.card_header in Shiny for Python"
    )
