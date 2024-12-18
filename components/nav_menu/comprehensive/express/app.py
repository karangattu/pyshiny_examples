from shiny import reactive
from shiny.express import input, ui, render

# Custom CSS to make icons more visible
ui.head_content(
    ui.HTML(
        """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <style>
            .fa-solid { font-size: 1.2rem; margin-right: 5px; }
        </style>
        """
    )
)

ui.page_opts(title="Nav Menu Demo", fillable=True)

# Create a navigation bar with different nav_menu examples
with ui.navset_bar(title="Nav Menu Examples"):

    # Basic nav_menu with just title
    with ui.nav_menu("Basic Menu"):
        with ui.nav_panel("Panel 1"):
            ui.markdown("### Basic Menu - Panel 1")
            "This is a basic nav_menu with just a title parameter."
        with ui.nav_panel("Panel 2"):
            ui.markdown("### Basic Menu - Panel 2")
            "Another panel in the basic menu."

    # Nav menu with value parameter
    with ui.nav_menu("Menu with Value", value="value_menu"):
        with ui.nav_panel("Panel A", value="panel_a"):
            ui.markdown("### Value Menu - Panel A")
            "This menu has a specific value parameter set."

            @render.text
            def show_value():
                return f"Current menu value: value_menu"

    # Nav menu with icon
    with ui.nav_menu("Menu with Icon", icon=ui.tags.i(class_="fa-solid fa-gear")):
        with ui.nav_panel("Settings 1"):
            ui.markdown("### Icon Menu - Settings 1")
            "This menu has a gear icon."
        with ui.nav_panel("Settings 2"):
            ui.markdown("### Icon Menu - Settings 2")
            "Another settings panel."

    # Nav menu with right alignment
    with ui.nav_menu(
        "Right Aligned Menu",
        align="right",
        icon=ui.tags.i(class_="fa-solid fa-arrow-right"),
    ):
        with ui.nav_panel("Right Panel 1"):
            ui.markdown("### Right-aligned Menu - Panel 1")
            "This menu is aligned to the right."
        with ui.nav_panel("Right Panel 2"):
            ui.markdown("### Right-aligned Menu - Panel 2")
            "Another right-aligned panel."

    # Complex nav menu with all parameters
    with ui.nav_menu(
        title="Complete Menu",
        value="complete_menu",
        icon=ui.tags.i(class_="fa-solid fa-star"),
        align="left",
    ):
        with ui.nav_panel("Complete Panel 1", value="complete_1"):
            ui.markdown("### Complete Menu - Panel 1")
            "This menu demonstrates all possible parameters:"
            ui.markdown(
                """
            * title: "Complete Menu"
            * value: "complete_menu"
            * icon: star icon
            * align: "left"
            """
            )

            @render.text
            def show_complete_value():
                return f"Complete menu value: complete_menu"

        with ui.nav_panel("Complete Panel 2", value="complete_2"):
            ui.markdown("### Complete Menu - Panel 2")
            "Another panel in the complete menu example."

    # Add a nav spacer for better visual organization
    ui.nav_spacer()

    # Add a nav control with dark mode toggle
    with ui.nav_control():
        ui.input_dark_mode()
