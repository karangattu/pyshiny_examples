import random
from datetime import datetime
from typing import List, Tuple

import pandas as pd
from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui

# Sample data for breweries and wineries
breweries = [
    {
        "name": "Hoppy Brewing Co.",
        "location": "San Francisco, CA",
        "founded": 2010,
        "production": 50000,
    },
    {
        "name": "Craft Ales",
        "location": "Portland, OR",
        "founded": 2015,
        "production": 30000,
    },
    {
        "name": "Barrel Aged Brews",
        "location": "Chicago, IL",
        "founded": 2012,
        "production": 40000,
    },
    {
        "name": "Hops & Grapes",
        "location": "Napa, CA",
        "founded": 2008,
        "production": 60000,
    },
    {
        "name": "Fermentation Station",
        "location": "Seattle, WA",
        "founded": 2018,
        "production": 20000,
    },
]

wineries = [
    {
        "name": "Vintner's Reserve",
        "location": "Napa, CA",
        "founded": 1985,
        "production": 100000,
    },
    {
        "name": "Grape Escape",
        "location": "Sonoma, CA",
        "founded": 1995,
        "production": 80000,
    },
    {
        "name": "Cellar Dwellers",
        "location": "Willamette Valley, OR",
        "founded": 2005,
        "production": 60000,
    },
    {
        "name": "Vino Veritas",
        "location": "Charlottesville, VA",
        "founded": 2015,
        "production": 40000,
    },
    {
        "name": "Barrel Bliss",
        "location": "Finger Lakes, NY",
        "founded": 2012,
        "production": 50000,
    },
]

# Shiny app UI
app_ui = ui.page_fluid(
    ui.panel_title("Brewery and Winery Management"),
    ui.layout_column_wrap(
        ui.value_box(
            "Total Breweries",
            str(len(breweries)),
            showcase=ui.HTML('<i class="bi bi-cup-straw"></i>'),
            theme="bg-gradient-orange-red",
        ),
        ui.value_box(
            "Total Wineries",
            str(len(wineries)),
            showcase=ui.HTML('<i class="bi bi-cup-straw"></i>'),
            theme="bg-gradient-orange-red",
        ),
        ui.value_box(
            "Total Production",
            f"{sum(b['production'] for b in breweries) + sum(w['production'] for w in wineries):,} gallons",
            showcase=ui.HTML('<i class="bi bi-bar-chart-line"></i>'),
            theme="bg-gradient-orange-red",
        ),
        width=1 / 3,
    ),
    ui.navset_tab(
        ui.nav_panel("Breweries", ui.output_data_frame("brewery_table")),
        ui.nav_panel("Wineries", ui.output_data_frame("winery_table")),
        id="tabs",
    ),
)


# Shiny app server
def server(input: Inputs, output: Outputs, session: Session):
    @reactive.calc
    def brewery_data():
        return pd.DataFrame(breweries)

    @reactive.calc
    def winery_data():
        return pd.DataFrame(wineries)

    @render.data_frame
    def brewery_table():
        return brewery_data()

    @render.data_frame
    def winery_table():
        return winery_data()


app = App(app_ui, server)
