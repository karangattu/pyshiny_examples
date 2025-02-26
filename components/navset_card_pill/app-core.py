from shiny import App, reactive, render, ui

# Define the UI
app_ui = ui.page_fillable(
    # Add Font Awesome CSS for icons
    ui.head_content(
        ui.HTML(
            '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css>'
        )
    ),
    # Create navset_card_pill
    ui.navset_card_pill(
        # First nav panel
        ui.nav_panel(
            "A",
            ui.h4("Panel A Content"),
            ui.markdown("This is static content in Panel A"),
            ui.output_text("text_a"),
        ),
        # Second nav panel
        ui.nav_panel(
            "B",
            ui.h4("Panel B Content"),
            ui.markdown("This is static content in Panel B"),
            ui.output_text("text_b"),
        ),
        # Third nav panel with icon
        ui.nav_panel(
            "C",
            ui.h4("Panel C Content"),
            ui.markdown("This is static content in Panel C"),
            ui.output_text("text_c"),
            icon=ui.tags.i(class_="fa-solid fa-star"),
        ),
        # Fourth nav panel in a dropdown menu
        ui.nav_menu(
            "More Options",
            ui.nav_panel(
                "D",
                ui.h4("Panel D Content"),
                ui.markdown("This is static content in Panel D"),
                ui.output_text("text_d"),
            ),
        ),
        id="selected_card_pill",
    ),
    # Selection tracker section
    ui.hr(),
    ui.h4("Selection Tracker"),
    ui.output_text("selected_panel"),
)


# Define the server
def server(input, output, session):
    @output
    @render.text
    def text_a():
        return "This is dynamic content in Panel A"

    @output
    @render.text
    def text_b():
        return "This is dynamic content in Panel B"

    @output
    @render.text
    def text_c():
        return "This is dynamic content in Panel C"

    @output
    @render.text
    def text_d():
        return "This is dynamic content in Panel D"

    @output
    @render.text
    def selected_panel():
        return f"Currently selected panel: {input.selected_card_pill()}"


# Create and return the app
app = App(app_ui, server)
