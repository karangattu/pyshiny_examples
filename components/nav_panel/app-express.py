from shiny import reactive
from shiny.express import input, ui, render

# Add Font Awesome CSS in the head section first
ui.head_content(
    ui.tags.link(
        rel="stylesheet",
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css",
    )
)

# Set page options
ui.page_opts(title="Nav Panel Demo", fillable=True)

# Create a navset container for the nav panels
with ui.navset_tab(id="nav"):
    # Using nav_panel with title only
    with ui.nav_panel("Basic Panel"):
        "This is a basic nav panel with just a title"

    # Using nav_panel with title and value
    with ui.nav_panel("Panel with Value", value="panel2"):
        "This panel has a custom value that can be used for programmatic control"

    # Using nav_panel with title, value, and icon
    with ui.nav_panel(
        "Panel with Icon",
        value="panel3",
        icon=ui.tags.i(class_="fa-solid fa-chart-simple", style="font-size: 1rem;"),
    ):
        "This panel includes an icon from Font Awesome"

ui.nav_spacer()


# Display the currently selected panel value
@render.text
def selected_panel():
    return f"Currently selected panel value: {input.nav()}"
