from shiny import App, reactive, render, ui

app_ui = ui.page_fillable(
    # Create a sidebar with all possible parameters
    ui.sidebar(
        "This sidebar demonstrates all possible parameters",
        ui.hr(),
        ui.input_text("txt", "Enter text", "Hello"),
        id="demo_sidebar",  # Required for reactive updates
        position="left",  # 'left' or 'right'
        open={"desktop": "open", "mobile": "closed"},  # Control initial state
        width="300px",  # Width of sidebar
        bg="#f8f9fa",  # Background color
        fg="#212529",  # Foreground (text) color
        class_="my-custom-class",  # Additional CSS classes
        max_height_mobile="300px",  # Max height on mobile
        gap="1rem",  # Gap between elements
        padding="1rem",  # Padding inside sidebar
    ),
    # Main content area
    ui.output_text("sidebar_state"),
)


def server(input, output, session):
    @render.text
    def sidebar_state():
        """Show the current state of the sidebar"""
        return f"Sidebar state: {input.demo_sidebar()}"


app = App(app_ui, server)
