from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Card Header Demo", fillable=True)

# Create a container that demonstrates all card_header parameters
with ui.layout_column_wrap(width=1 / 2):

    # Example 1: Basic card header with title
    with ui.card():
        ui.card_header("Basic Card Header")
        "This shows a basic card header with just a title"

    # Example 2: Card header with custom container (h3)
    with ui.card():
        ui.card_header(
            "Header with Custom Container", container=ui.tags.h3, class_="text-primary"
        )
        "This shows a card header using an h3 tag as container"

    # Example 3: Card header with multiple elements
    with ui.card():
        ui.card_header(
            ui.h4("Complex Header"),
            ui.span("With subtitle", class_="text-muted"),
            ui.input_action_button("btn1", "Action", class_="float-end"),
            class_="d-flex justify-content-between align-items-center",
        )
        "This shows a card header with multiple elements and flex layout"

    # Example 4: Card header with icon and dynamic content
    with ui.card():
        ui.card_header(
            ui.tags.i(class_="fa-solid fa-chart-line me-2"),
            "Dynamic Header",
            class_="d-flex align-items-center",
        )

        @render.text
        def dynamic_text():
            return "Updated content"

    # Example 5: Card header with custom styling
    with ui.card():
        ui.card_header(
            "Custom Styled Header",
            style="background-color: #e3f2fd; color: #1976d2; font-weight: bold;",
        )
        "This shows a card header with custom CSS styling"

    # Example 6: Interactive card header
    with ui.card():
        ui.card_header(
            "Interactive Header",
            ui.input_switch("toggle", "Toggle View", value=True),
            class_="d-flex justify-content-between",
        )

        @render.ui
        def conditional_content():
            if input.toggle():
                return "Content is visible"
            return "Content is hidden"


# Add Font Awesome for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">'
    )
)
