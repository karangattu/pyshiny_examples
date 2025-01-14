import pandas as pd
from shiny import reactive
from shiny.express import input, render, ui

# Sample data for demo
data = {
    "East Coast": {"NY": "New York", "NJ": "New Jersey", "CT": "Connecticut"},
    "West Coast": {"WA": "Washington", "OR": "Oregon", "CA": "California"},
    "Midwest": {"MN": "Minnesota", "WI": "Wisconsin", "IA": "Iowa"},
}

ui.page_opts(title="Navset Pill List Demo", fillable=True)

# Header section
ui.h2("Navset Pill List Demonstration", class_="mb-3")

# Main content using navset_pill_list with all possible parameters
with ui.navset_pill_list(
    id="selected_navset_pill_list",  # Input id to track selected panel
    well=True,  # Add a well (gray rounded rectangle) around navigation list
    widths=(3, 9),  # Column widths for nav list and content areas
):
    # Panel A with basic content
    with ui.nav_panel("Panel A"):
        ui.h4("Basic Panel Content")
        ui.input_text("text_input", "Enter some text", "Sample text")

        @render.text
        def text_output():
            return f"You entered: {input.text_input()}"

    # Panel B with a data table
    with ui.nav_panel("Panel B"):
        ui.h4("Data Table Example")
        ui.input_select("region", "Select Region", choices=list(data.keys()))

        @render.data_frame
        def show_data():
            region = input.region()
            if region:
                return pd.DataFrame(
                    list(data[region].items()), columns=["State Code", "State Name"]
                )
            return pd.DataFrame()

    # Panel C with interactive elements
    with ui.nav_panel("Panel C"):
        ui.h4("Interactive Elements")
        with ui.layout_sidebar():
            with ui.sidebar():
                ui.input_numeric("number", "Enter a number", 5)
                ui.input_slider("slider", "Adjust slider", 0, 100, 50)

            @render.text
            def calculation():
                return f"Number × Slider = {input.number() * input.slider()}"

    # Panel D with a menu
    with ui.nav_menu("More Options"):
        with ui.nav_panel("Panel D"):
            ui.h4("Additional Content")
            ui.markdown(
                """
                This is a panel within a nav_menu.
                - It demonstrates nested navigation
                - Shows menu functionality
                - Provides additional organization
            """
            )

# Show currently selected panel
ui.hr()
ui.h5("Selected Panel:")


@render.text
def selected_panel():
    return f"Currently selected: {input.selected_navset_pill_list()}"
