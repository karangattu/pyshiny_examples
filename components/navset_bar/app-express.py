from shiny import reactive
from shiny.express import input, ui, render

# Add Font Awesome CSS in the head section
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
    )
)

# Set page options
ui.page_opts(title="Navset Bar Demo", fillable=True)

# Create a navset_bar
with ui.navset_bar(
    title="Complete Navset Bar Demo",
    id="nav_id",
    selected="tab1",
    sidebar=None,
    fillable=True,
    padding="1rem",
    position="static-top",
    header="Header Content",
    footer="Footer Content",
    bg="#f8f9fa",
    inverse=False,
    underline=True,
    collapsible=True,
    fluid=True,
):
    # First nav panel
    with ui.nav_panel("Tab 1", value="tab1"):
        with ui.card():
            ui.card_header("Tab 1 Content")
            "This is the content for Tab 1"
            ui.input_text("txt1", "Enter text:", "Sample text")

    # Second nav panel with icon
    with ui.nav_panel("Tab 2", value="tab2"):
        with ui.card():
            ui.card_header("Tab 2 Content")
            "This is the content for Tab 2"
            ui.input_numeric("num1", "Enter number:", 5)
            ui.tags.i(class_="fa-solid fa-chart-simple")

    # Dropdown menu
    with ui.nav_menu("Dropdown Menu"):
        with ui.nav_panel("Menu Item 1", value="menu1"):
            with ui.card():
                ui.card_header("Menu Item 1")
                "Content for Menu Item 1"
                ui.input_slider("slider1", "Select value:", 0, 100, 50)

        with ui.nav_panel("Menu Item 2", value="menu2"):
            with ui.card():
                ui.card_header("Menu Item 2")
                "Content for Menu Item 2"
                ui.input_checkbox("chk1", "Check this", True)

    # Add a nav control with external link
    with ui.nav_control():
        ui.a(
            ui.tags.i(class_="fa-solid fa-external-link-alt me-1"),
            "Shiny",
            href="https://shiny.posit.co/py/",
            target="_blank",
            class_="nav-link",
        )

    # Add spacer
    ui.nav_spacer()

    # Last nav panel
    with ui.nav_panel("Tab 3", value="tab3"):
        with ui.card():
            ui.card_header("Tab 3 Content")
            "This is the content for Tab 3"
            ui.input_date("date1", "Select date:")


# Show selected tab value
@render.text
def selected_tab():
    return f"Currently selected: {input.nav_id()}"
