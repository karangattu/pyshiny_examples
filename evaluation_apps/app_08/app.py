from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.navset_tab(
        ui.nav("Tab 1", ui.p("This is the first tab.")),
        ui.nav("Tab 2", ui.p("This is the second tab.")),
    )
)

def server(input, output, session):
    pass

app = App(app_ui, server)
