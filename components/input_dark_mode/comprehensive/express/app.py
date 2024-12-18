from shiny import reactive
from shiny.express import input, ui, render

# Set page options with a title
ui.page_opts(title="Dark Mode Input Showcase")

# Add Font Awesome CSS for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">'
    )
)

# Create a layout with sidebar
with ui.layout_sidebar():
    # Sidebar with dark mode input and additional controls
    with ui.sidebar(id="sidebar"):
        # Dark mode input with various configurations
        ui.markdown("### Dark Mode Configurations")

        # Basic dark mode input
        ui.input_dark_mode(id="mode1")

        # Dark mode input with initial mode set
        ui.input_dark_mode(id="mode2", mode="dark")

        # Dark mode input with custom classes and styling
        ui.input_dark_mode(
            id="mode3", class_="custom-dark-mode-toggle", style="margin-top: 10px;"
        )

    # Main content area
    with ui.card():
        ui.card_header("Dark Mode Information")

        # Display current mode states
        @render.text
        def mode_states():
            return f"""
            Mode 1 (Default): {input.mode1()}
            Mode 2 (Initial Dark): {input.mode2()}
            Mode 3 (Custom Style): {input.mode3()}
            """

        # Demonstrate reactive effects with dark mode
        @render.ui
        def dynamic_content():
            # Change content based on dark mode state
            if input.mode1() == "dark":
                return ui.tags.div(
                    ui.tags.h3("Dark Mode Activated", style="color: white;"),
                    ui.tags.p(
                        "Content optimized for dark background.",
                        style="color: lightgray;",
                    ),
                )
            else:
                return ui.tags.div(
                    ui.tags.h3("Light Mode Active", style="color: black;"),
                    ui.tags.p(
                        "Content optimized for light background.",
                        style="color: darkgray;",
                    ),
                )

        # Add some interactive buttons to demonstrate mode switching
        ui.input_action_button("set_light", "Force Light Mode")
        ui.input_action_button("set_dark", "Force Dark Mode")


# Reactive effects to manually set mode
@reactive.effect
@reactive.event(input.set_light)
def _():
    ui.update_dark_mode("light")


@reactive.effect
@reactive.event(input.set_dark)
def _():
    ui.update_dark_mode("dark")
