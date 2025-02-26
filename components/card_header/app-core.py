from shiny import App, render, ui

# Define the UI
app_ui = ui.page_fillable(
    # Add Font Awesome in head
    ui.tags.head(
        ui.HTML(
            '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">'
        )
    ),
    # Main card with nested cards
    ui.card(
        # Basic header with title as string
        ui.card_header("Basic Header"),
        ui.p("This header shows the simplest usage with just a text string"),
        # Card with custom container header
        ui.card(
            ui.card_header("Custom Container Header", container=ui.tags.h3),
            ui.p("This header uses a custom h3 container instead of the default div"),
            height="100px",
            id="custom_card",
        ),
        # Card with complex header
        ui.card(
            ui.card_header(
                ui.tags.span("Complex Header with ", style="color: blue;"),
                ui.tags.strong("Multiple Elements"),
                class_="text-center",
                style="background-color: #f8f9fa;",
            ),
            ui.p("This header demonstrates using multiple elements and custom styling"),
            height="100px",
            id="complex_card",
        ),
        # Card with icon header
        ui.card(
            ui.card_header(
                ui.tags.i(class_="fa-solid fa-shield-halved", style="font-size: 2rem;"),
                " Header with Icon",
                container=ui.tags.h4,
                style="color: green;",
            ),
            ui.p("This header shows how to include a Font Awesome icon"),
            height="100px",
            id="icon_card",
        ),
        # Output for description
        ui.output_ui("description"),
        height="500px",
        id="demo_card",
    ),
)


# Define the server
def server(input, output, session):
    @output
    @render.ui
    def description():
        return ui.p(
            "This app demonstrates different ways to use ui.card_header in Shiny for Python"
        )


# Create the app
app = App(app_ui, server)
