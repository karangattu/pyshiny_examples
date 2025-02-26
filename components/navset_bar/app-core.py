from shiny import App, reactive, render, ui

# Define the UI
app_ui = ui.page_fillable(
    # Add Font Awesome CSS in the head section
    ui.tags.head(
        ui.tags.link(
            rel="stylesheet",
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css",
        )
    ),
    # Create navset_bar
    ui.navset_bar(
        # First nav panel
        ui.nav_panel(
            "Tab 1",
            ui.card(
                ui.card_header("Tab 1 Content"),
                "This is the content for Tab 1",
                ui.input_text("txt1", "Enter text:", "Sample text"),
            ),
            value="tab1",
        ),
        # Second nav panel with icon
        ui.nav_panel(
            "Tab 2",
            ui.card(
                ui.card_header("Tab 2 Content"),
                "This is the content for Tab 2",
                ui.input_numeric("num1", "Enter number:", 5),
                ui.tags.i(class_="fa-solid fa-chart-simple"),
            ),
            value="tab2",
        ),
        # Dropdown menu
        ui.nav_menu(
            "Dropdown Menu",
            ui.nav_panel(
                "Menu Item 1",
                ui.card(
                    ui.card_header("Menu Item 1"),
                    "Content for Menu Item 1",
                    ui.input_slider("slider1", "Select value:", 0, 100, 50),
                ),
                value="menu1",
            ),
            ui.nav_panel(
                "Menu Item 2",
                ui.card(
                    ui.card_header("Menu Item 2"),
                    "Content for Menu Item 2",
                    ui.input_checkbox("chk1", "Check this", True),
                ),
                value="menu2",
            ),
        ),
        # Nav control with external link
        ui.nav_control(
            ui.a(
                ui.tags.i(class_="fa-solid fa-external-link-alt me-1"),
                "Shiny",
                href="https://shiny.posit.co/py/",
                target="_blank",
                class_="nav-link",
            )
        ),
        # Nav spacer
        ui.nav_spacer(),
        # Last nav panel
        ui.nav_panel(
            "Tab 3",
            ui.card(
                ui.card_header("Tab 3 Content"),
                "This is the content for Tab 3",
                ui.input_date("date1", "Select date:"),
            ),
            value="tab3",
        ),
        id="nav_id",
        selected="tab1",
        title="Complete Navset Bar Demo",
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
    ),
    # Output for selected tab
    ui.output_text("selected_tab"),
)


# Define the server
def server(input, output, session):
    @output
    @render.text
    def selected_tab():
        return f"Currently selected: {input.nav_id()}"


# Create the app
app = App(app_ui, server)
