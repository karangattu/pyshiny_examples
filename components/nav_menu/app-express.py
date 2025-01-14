from shiny import reactive
from shiny.express import input, ui, render

# Add Font Awesome CSS in the head section
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">'
    )
)

# Page options
ui.page_opts(title="Nav Menu Demo", fillable=True)

# Create a nav menu with all possible parameters
with ui.navset_card_tab(id="selected_nav"):
    with ui.nav_menu(
        "Menu Demo",  # Title parameter
        value="menu1",  # Value parameter
        icon=ui.HTML(
            '<i class="fa-solid fa-bars" style="font-size: 1.2rem;"></i>'
        ),  # Icon parameter
        align="left",  # Align parameter
    ):
        with ui.nav_panel("Panel A", value="panel_a"):
            ui.markdown("Content for Panel A")

        with ui.nav_panel("Panel B", value="panel_b"):
            ui.markdown("Content for Panel B")

        with ui.nav_panel("Panel C", value="panel_c"):
            ui.markdown("Content for Panel C")

    # Add a regular nav panel for comparison
    with ui.nav_panel("Regular Panel"):
        ui.markdown("This is a regular nav panel")


# Show current selection
@render.text
def current_selection():
    """Display the currently selected nav item"""
    return f"Currently selected: {input.selected_nav()}"
