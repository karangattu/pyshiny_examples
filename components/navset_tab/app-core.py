from shiny import App, reactive, render, ui

# Define the UI
app_ui = ui.page_fillable(
    # Add Font Awesome CSS to the head
    ui.tags.head(
        ui.tags.link(
            rel="stylesheet",
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css",
        )
    ),
    # Create navset_tab
    ui.navset_tab(
        # Regular nav panel
        ui.nav_panel(
            "Tab 1",
            ui.h3("Content for Tab 1"),
            ui.p("This is the content that appears in the first tab."),
            value="tab1",
        ),
        # Selected by default
        ui.nav_panel(
            "Tab 2",
            ui.h3("Content for Tab 2"),
            ui.p("This tab is selected by default because we set selected='tab2'"),
            value="tab2",
        ),
        # Nav panel with an icon
        ui.nav_panel(
            "Tab 3",
            ui.h3("Content for Tab 3"),
            ui.p("This tab has a chart icon from Font Awesome"),
            value="tab3",
            icon=ui.tags.i(class_="fa-solid fa-chart-simple"),
        ),
        # Nav menu (dropdown) with multiple panels
        ui.nav_menu(
            "More Tabs",
            ui.nav_panel(
                "Tab 4",
                ui.h3("Content for Tab 4"),
                ui.p("This content is in a dropdown menu"),
                value="tab4",
            ),
            ui.nav_panel(
                "Tab 5",
                ui.h3("Content for Tab 5"),
                ui.p("This is also in the dropdown menu"),
                value="tab5",
            ),
            ui.nav_spacer(),
            ui.nav_control(
                ui.a("Visit Shiny", href="https://shiny.posit.co", target="_blank")
            ),
            align="left",
        ),
        id="tabset",
        selected="tab2",
    ),
    ui.br(),
    # Output for selected tab
    ui.output_text("selected_tab"),
)


# Define the server
def server(input, output, session):
    @output
    @render.text
    def selected_tab():
        return f"Currently selected tab: {input.tabset()}"


# Create the app
app = App(app_ui, server)
