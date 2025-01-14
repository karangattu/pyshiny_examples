from shiny import reactive
from shiny.express import input, render, ui

# Set page options for the app
ui.page_opts(title="Navset Tab Demo", fillable=True)

# First add Font Awesome CSS to the head of the document
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
    )
)

# Create a navset_tab with all possible parameters
with ui.navset_tab(
    id="tabset",  # Optional id to track selected tab
    selected="tab2",  # Choose which tab is initially selected
):
    # Regular nav panel
    with ui.nav_panel("Tab 1", value="tab1"):
        ui.h3("Content for Tab 1")
        ui.p("This is the content that appears in the first tab.")

    # Selected by default
    with ui.nav_panel("Tab 2", value="tab2"):
        ui.h3("Content for Tab 2")
        ui.p("This tab is selected by default because we set selected='tab2'")

    # Nav panel with an icon
    with ui.nav_panel(
        "Tab 3", value="tab3", icon=ui.tags.i(class_="fa-solid fa-chart-simple")
    ):
        ui.h3("Content for Tab 3")
        ui.p("This tab has a chart icon from Font Awesome")

    # Nav menu (dropdown) with multiple panels
    with ui.nav_menu("More Tabs", align="left"):
        with ui.nav_panel("Tab 4", value="tab4"):
            ui.h3("Content for Tab 4")
            ui.p("This content is in a dropdown menu")

        with ui.nav_panel("Tab 5", value="tab5"):
            ui.h3("Content for Tab 5")
            ui.p("This is also in the dropdown menu")

        ui.nav_spacer()  # Add a separator
        with ui.nav_control():
            ui.a("Visit Shiny", href="https://shiny.posit.co", target="_blank")

# Add some spacing
ui.br()


# Show which tab is currently selected
@render.text
def selected_tab():
    return f"Currently selected tab: {input.tabset()}"
