from shiny import reactive
from shiny.express import input, render, ui

# Page options
ui.page_opts(title="navset_hidden Demo", fillable=True)

# Controller for switching panels
with ui.sidebar():
    ui.input_radio_buttons(
        "controller",
        "Select Panel",
        choices=["panel1", "panel2", "panel3"],
        selected="panel1",
    )

# navset_hidden with panels
with ui.navset_hidden(id="hidden_nav"):
    # Panel 1
    with ui.nav_panel(None, value="panel1"):
        ui.h3("Panel 1")
        ui.p("This is the content for Panel 1")
        with ui.card():
            "Some card content in Panel 1"

    # Panel 2
    with ui.nav_panel(None, value="panel2"):
        ui.h3("Panel 2")
        ui.p("This is the content for Panel 2")
        with ui.card(full_screen=True):
            "Some card content in Panel 2"

    # Panel 3
    with ui.nav_panel(None, value="panel3"):
        ui.h3("Panel 3")
        ui.p("This is the content for Panel 3")
        with ui.card():
            "Some card content in Panel 3"


# Effect to update selected panel based on radio input
@reactive.effect
def _():
    ui.update_navs("hidden_nav", selected=input.controller())
