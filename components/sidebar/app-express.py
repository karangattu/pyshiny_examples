from shiny import reactive
from shiny.express import input, ui, render

# Configure page options
ui.page_opts(title="Sidebar Demo", fillable=True)

# Create a sidebar with all possible parameters
with ui.sidebar(
    id="demo_sidebar",  # Required for reactive updates
    position="left",  # 'left' or 'right'
    open={"desktop": "open", "mobile": "closed"},  # Control initial state
    width="300px",  # Width of sidebar
    title="Sidebar Demo",  # Title at top of sidebar
    bg="#f8f9fa",  # Background color
    fg="#212529",  # Foreground (text) color
    class_="my-custom-class",  # Additional CSS classes
    max_height_mobile="300px",  # Max height on mobile
    gap="1rem",  # Gap between elements
    padding="1rem",  # Padding inside sidebar
):
    "This sidebar demonstrates all possible parameters"
    ui.hr()
    ui.input_text("txt", "Enter text", "Hello")


# Main content area - minimal for demonstration
@render.text
def sidebar_state():
    """Show the current state of the sidebar"""
    return f"Sidebar state: {input.demo_sidebar()}"
