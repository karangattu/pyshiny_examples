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
    # Create a navset container for the nav panels
    ui.navset_tab(
        # Basic nav panel with title only
        ui.nav_panel("Basic Panel", "This is a basic nav panel with just a title"),
        # Nav panel with title and value
        ui.nav_panel(
            "Panel with Value",
            "This panel has a custom value that can be used for programmatic control",
            value="panel2",
        ),
        # Nav panel with title, value, and icon
        ui.nav_panel(
            "Panel with Icon",
            "This panel includes an icon from Font Awesome",
            value="panel3",
            icon=ui.tags.i(class_="fa-solid fa-chart-simple", style="font-size: 1rem;"),
        ),
        id="nav",
    ),
    ui.nav_spacer(),
    # Output for displaying selected panel
    ui.output_text("selected_panel"),
)


# Define the server
def server(input, output, session):
    @output
    @render.text
    def selected_panel():
        return f"Currently selected panel value: {input.nav()}"


# Create and return the app
app = App(app_ui, server)
