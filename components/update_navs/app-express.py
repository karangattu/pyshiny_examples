from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Update Navs Demo", fillable=True)

# Create a sidebar with control buttons
with ui.sidebar():
    ui.h4("Navigation Controls")
    ui.input_action_button("goto1", "Go to Panel 1", class_="btn-primary w-100 mb-2")
    ui.input_action_button("goto2", "Go to Panel 2", class_="btn-primary w-100 mb-2")
    ui.input_action_button("goto3", "Go to Panel 3", class_="btn-primary w-100 mb-2")

    ui.hr()

    @render.text
    def current_panel():
        return f"Currently selected: {input.inTabset()}"


# Main content area with navset
with ui.navset_tab(id="inTabset"):
    with ui.nav_panel("Panel 1", value="panel1"):
        with ui.card():
            ui.card_header("Panel 1")
            "This is the content for Panel 1"

    with ui.nav_panel("Panel 2", value="panel2"):
        with ui.card():
            ui.card_header("Panel 2")
            "This is the content for Panel 2"

    with ui.nav_panel("Panel 3", value="panel3"):
        with ui.card():
            ui.card_header("Panel 3")
            "This is the content for Panel 3"


# Effects to handle button clicks
@reactive.effect
@reactive.event(input.goto1)
def _():
    ui.update_navs("inTabset", selected="panel1")


@reactive.effect
@reactive.event(input.goto2)
def _():
    ui.update_navs("inTabset", selected="panel2")


@reactive.effect
@reactive.event(input.goto3)
def _():
    ui.update_navs("inTabset", selected="panel3")
