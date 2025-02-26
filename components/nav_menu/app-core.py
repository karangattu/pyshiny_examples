from shiny import App, reactive, render, ui

# Define the UI
app_ui = ui.page_fillable(
    # Add Font Awesome CSS in the head section
    ui.tags.head(
        ui.HTML(
            '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">'
        )
    ),
    
    # Create a nav menu with all possible parameters
    ui.navset_card_tab(
        ui.nav_menu(
            "Menu Demo",  # Title parameter
            value="menu1",  # Value parameter
            icon=ui.HTML(
                '<i class="fa-solid fa-bars" style="font-size: 1.2rem;"></i>'
            ),  # Icon parameter
            align="left",  # Align parameter
            ui.nav_panel(
                "Panel A", 
                ui.markdown("Content for Panel A"),
                value="panel_a"
            ),
            ui.nav_panel(
                "Panel B", 
                ui.markdown("Content for Panel B"),
                value="panel_b"
            ),
            ui.nav_panel(
                "Panel C", 
                ui.markdown("Content for Panel C"),
                value="panel_c"
            ),
        ),
        # Add a regular nav panel for comparison
        ui.nav_panel(
            "Regular Panel",
            ui.markdown("This is a regular nav panel")
        ),
        id="selected_nav"
    ),
    
    # Output for current selection
    ui.output_text("current_selection"),
)

# Define the server
def server(input, output, session):
    @output
    @render.text
    def current_selection():
        """Display the currently selected nav item"""
        return f"Currently selected: {input.selected_nav()}"

# Create the app
app = App(app_ui, server)