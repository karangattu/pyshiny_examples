from shiny import reactive
from shiny.express import input, render, ui

# Sample data
product_data = {
    "Electronics": {
        "sales": [1200, 1500, 1300, 1700],
        "months": ["Jan", "Feb", "Mar", "Apr"],
        "growth": "+15%",
    },
    "Clothing": {
        "sales": [800, 950, 1000, 1100],
        "months": ["Jan", "Feb", "Mar", "Apr"],
        "growth": "+12%",
    },
    "Books": {
        "sales": [400, 380, 420, 450],
        "months": ["Jan", "Feb", "Mar", "Apr"],
        "growth": "+8%",
    },
}

# Set up page options
ui.page_opts(title="Product Performance Dashboard", fillable=True)

# Create navset_pill_list
with ui.navset_pill_list(id="product_nav"):
    # Electronics panel
    with ui.nav_panel("Electronics"):
        ui.h3("Electronics Department")

        @render.text
        def electronics_stats():
            data = product_data["Electronics"]
            return (
                f"Total Sales: ${sum(data['sales']):,}\n"
                f"Growth: {data['growth']}\n"
                f"Best Month: {data['months'][data['sales'].index(max(data['sales']))]}"
            )

    # Clothing panel
    with ui.nav_panel("Clothing"):
        ui.h3("Clothing Department")

        @render.text
        def clothing_stats():
            data = product_data["Clothing"]
            return (
                f"Total Sales: ${sum(data['sales']):,}\n"
                f"Growth: {data['growth']}\n"
                f"Best Month: {data['months'][data['sales'].index(max(data['sales']))]}"
            )

    # Books panel
    with ui.nav_panel("Books"):
        ui.h3("Books Department")

        @render.text
        def books_stats():
            data = product_data["Books"]
            return (
                f"Total Sales: ${sum(data['sales']):,}\n"
                f"Growth: {data['growth']}\n"
                f"Best Month: {data['months'][data['sales'].index(max(data['sales']))]}"
            )
