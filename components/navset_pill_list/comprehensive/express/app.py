from shiny import reactive
from shiny.express import input, render, ui

# Sample data
data = {
    "East Coast": {
        "NY": "New York - Population: 8.8M",
        "NJ": "New Jersey - Population: 9.3M",
        "CT": "Connecticut - Population: 3.6M",
    },
    "West Coast": {
        "CA": "California - Population: 39.5M",
        "OR": "Oregon - Population: 4.2M",
        "WA": "Washington - Population: 7.7M",
    },
    "Midwest": {
        "IL": "Illinois - Population: 12.8M",
        "MI": "Michigan - Population: 10.0M",
        "WI": "Wisconsin - Population: 5.9M",
    },
}

# Set page options
ui.page_opts(title="Navset Pill List Demo", fillable=True)

# Create a header
ui.h2("Navigation Pills List Demo")
ui.markdown(
    """
This demo shows all possible parameters of navset_pill_list:
* id - for tracking selected panel
* selected - choose initial selected panel
* header/footer - optional content
* well - background styling
* widths - control layout proportions
"""
)

# Create the navset_pill_list with all available parameters
with ui.navset_pill_list(
    id="pill_demo",  # Enable tracking of selected panel
    selected="East Coast",  # Set initial selection
    well=True,  # Add background styling
    widths=[3, 9],  # Control layout proportions [nav_width, content_width]
    header=ui.h4("Regional Population Statistics"),  # Add header content
    footer=ui.p(
        "Data is for demonstration purposes only", class_="text-muted"
    ),  # Add footer content
):
    # Create navigation panels for each region
    for region in data:
        with ui.nav_panel(region):
            with ui.card():
                ui.card_header(f"{region} States")

                # Create content for each state in the region
                for state_code, state_info in data[region].items():
                    with ui.layout_column_wrap():
                        ui.h5(state_code)
                        ui.p(state_info)


# Show currently selected panel
@render.text
def selected_panel():
    return f"Currently selected panel: {input.pill_demo()}"


# Add some stats about selection
with ui.card():
    ui.card_header("Selection Statistics")

    @render.text
    def selection_stats():
        current = input.pill_demo()
        if current in data:
            state_count = len(data[current])
            return f"The {current} region contains {state_count} states in this demo."
        return "Please select a region"
