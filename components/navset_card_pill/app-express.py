from shiny import reactive
from shiny.express import input, render, ui

# Initialize page options
ui.page_opts(title="Navset Card Pill Demo", fillable=True)

# Add Font Awesome CSS for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
    )
)

# Create a navset_card_pill
with ui.navset_card_pill(id="selected_card_pill"):
    # First nav panel
    with ui.nav_panel("A"):
        ui.h4("Panel A Content")
        ui.markdown("This is static content in Panel A")

        @render.text
        def text_a():
            return "This is dynamic content in Panel A"

    # Second nav panel
    with ui.nav_panel("B"):
        ui.h4("Panel B Content")
        ui.markdown("This is static content in Panel B")

        @render.text
        def text_b():
            return "This is dynamic content in Panel B"

    # Third nav panel with icon
    with ui.nav_panel("C", icon=ui.tags.i(class_="fa-solid fa-star")):
        ui.h4("Panel C Content")
        ui.markdown("This is static content in Panel C")

        @render.text
        def text_c():
            return "This is dynamic content in Panel C"

    # Fourth nav panel in a dropdown menu
    with ui.nav_menu("More Options"):
        with ui.nav_panel("D"):
            ui.h4("Panel D Content")
            ui.markdown("This is static content in Panel D")

            @render.text
            def text_d():
                return "This is dynamic content in Panel D"


# Show which panel is currently selected
ui.hr()
ui.h4("Selection Tracker")


@render.text
def selected_panel():
    return f"Currently selected panel: {input.selected_card_pill()}"
