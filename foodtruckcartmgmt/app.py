import folium
import pandas as pd
from shiny import App, reactive, render, ui
from shinywidgets import *

# Sample data for demonstration
data = {
    "Business Name": [
        "Taco Loco",
        "Burger Bliss",
        "Pizza Paradise",
        "Hotdog Heaven",
        "Waffle Wagon",
        "Crepe Corner",
        "Sushi Shuttle",
        "Noodle Nomad",
        "BBQ Express",
        "Salad Sensation",
        "Taco Time",
        "Pasta Pronto",
        "Pho Frenzy",
        "Burrito Bliss",
        "Fry Factory",
    ],
    "Type": [
        "Truck",
        "Truck",
        "Cart",
        "Cart",
        "Truck",
        "Cart",
        "Truck",
        "Truck",
        "Truck",
        "Cart",
        "Truck",
        "Cart",
        "Truck",
        "Truck",
        "Cart",
    ],
    "Location": [
        "Downtown",
        "Midtown",
        "Uptown",
        "Downtown",
        "Midtown",
        "Uptown",
        "Downtown",
        "Midtown",
        "Uptown",
        "Downtown",
        "Midtown",
        "Uptown",
        "Downtown",
        "Midtown",
        "Downtown",
    ],
    "Latitude": [
        34.0522,
        34.0430,
        34.0612,
        34.0522,
        34.0430,
        34.0612,
        34.0522,
        34.0430,
        34.0612,
        34.0522,
        34.0430,
        34.0612,
        34.0522,
        34.0430,
        34.0522,
    ],
    "Longitude": [
        -118.2437,
        -118.2648,
        -118.2892,
        -118.2437,
        -118.2648,
        -118.2892,
        -118.2437,
        -118.2648,
        -118.2892,
        -118.2437,
        -118.2648,
        -118.2892,
        -118.2437,
        -118.2648,
        -118.2437,
    ],
}
df = pd.DataFrame(data)

app_ui = ui.page_fluid(
    ui.h2("Food Truck and Cart Tracker"),  # App title
    ui.head_content(
        ui.HTML(
            '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">'
        )
    ),
    ui.row(
        ui.column(
            4,
            ui.value_box(
                "Total Food Trucks",
                ui.output_text("total_trucks"),
                showcase=ui.HTML('<i class="fa-solid fa-truck"></i>'),
                theme="bg-primary text-white",
            ),
        ),
        ui.column(
            4,
            ui.value_box(
                "Total Food Carts",
                ui.output_text("total_carts"),
                showcase=ui.HTML('<i class="fa-solid fa-cart-shopping"></i>'),
                theme="bg-success text-white",
            ),
        ),
        ui.column(
            4,
            ui.value_box(
                "Busiest Location",
                ui.output_text("busiest_location_info"),
                showcase=ui.HTML('<i class="fa-solid fa-location-dot"></i>'),
                theme="bg-warning text-dark",
            ),
        ),
    ),
    ui.row(
        ui.column(6, ui.h4("Food Trucks"), ui.output_data_frame("trucks_table")),
        ui.column(6, ui.h4("Food Carts"), ui.output_data_frame("carts_table")),
        ui.column(12, ui.h4("Map"), ui.output_ui("map")),
    ),
)


def server(input, output, session):
    # Calculate total trucks and carts
    @render.text
    def total_trucks():
        return str(df[df["Type"] == "Truck"].shape[0])

    @render.text
    def total_carts():
        return str(df[df["Type"] == "Cart"].shape[0])

    # Reactive calculation for busiest location
    @reactive.calc
    def busiest_location_data():
        location_counts = df["Location"].value_counts()
        busiest_location = location_counts.index[0]
        busiest_business = df[df["Location"] == busiest_location]["Business Name"].iloc[
            0
        ]
        return busiest_location, busiest_business

    # Display busiest location
    @render.text
    def busiest_location_info():
        location, business = busiest_location_data()
        return f"{location} ({business})"

    # Display Data Tables for food trucks and carts
    @render.data_frame
    def trucks_table():
        return df[df["Type"] == "Truck"][
            ["Business Name", "Location", "Latitude", "Longitude"]
        ]

    @render.data_frame
    def carts_table():
        return df[df["Type"] == "Cart"][
            ["Business Name", "Location", "Latitude", "Longitude"]
        ]

    # Display map
    @render.ui
    def map():
        m = folium.Map(location=[34.0522, -118.2437], zoom_start=12)
        for index, row in df.iterrows():
            folium.Marker(
                [row["Latitude"], row["Longitude"]],
                popup=row["Business Name"],
                icon=folium.Icon(color="blue" if row["Type"] == "Truck" else "red"),
            ).add_to(m)
        return m


app = App(app_ui, server)
