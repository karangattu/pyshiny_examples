import random
from datetime import datetime, timedelta
from typing import List, Tuple

from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui

# Mock data for flights and hotels
FLIGHTS = [
    ("New York", "Los Angeles", "2024-05-01", "2024-05-05", 500),
    ("Chicago", "Miami", "2024-06-15", "2024-06-20", 400),
    ("Seattle", "Boston", "2024-07-10", "2024-07-15", 600),
    ("Denver", "Atlanta", "2024-08-20", "2024-08-25", 450),
]

HOTELS = [
    ("New York", "The Grand Gotham", 200, 4),
    ("Los Angeles", "Pacific Breeze Suites", 300, 5),
    ("Miami", "Ocean View Resort", 150, 3),
    ("Boston", "Harborfront Inn", 250, 4),
]

app_ui = ui.page_fluid(
    ui.tags.head(
        ui.tags.link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"),
        ui.tags.style(
            """
            body {
                font-family: 'Roboto', sans-serif;
                background-color: #f4f7f6;
                color: #333;
            }
            .panel-title {
                text-align: center;
                font-size: 2.5em;
                color: #0056b3;
                margin-bottom: 1em;
                font-weight: bold;
            }
            .card {
                background-color: #fff;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
                padding: 20px;
                transition: box-shadow 0.3s ease;
            }
            .card:hover {
                 box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            }
            .card-header {
                background-color: #0056b3;
                color: white;
                padding: 15px;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                font-weight: 600;
                font-size: 1.2em;
                margin-bottom: 15px;
            }
            .form-control {
                border-radius: 5px;
                border: 1px solid #ddd;
                padding: 10px;
                margin-bottom: 15px;
            }
            .shiny-download-link {
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                text-decoration: none;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            .shiny-download-link:hover {
                background-color: #0056b3;
            }
            .shiny-download-link i {
                margin-right: 5px;
            }
            .verbatim-text-output {
                background-color: #f8f9fa;
                border: 1px solid #ddd;
                padding: 10px;
                border-radius: 5px;
                white-space: pre-wrap;
            }
            """
        )
    ),
    ui.div(
        {"class": "panel-title"},
        ui.tags.i(class_="fas fa-plane-departure", style="margin-right: 10px;"),
        "Flight and Hotel Booking",
        ui.tags.i(class_="fas fa-hotel", style="margin-left: 10px;"),
    ),
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Flight Booking"),
            ui.input_select(
                "from_city", "From", [city for city, _, _, _, _ in FLIGHTS]
            ),
            ui.input_select("to_city", "To", [city for city, _, _, _, _ in FLIGHTS]),
            ui.input_date("depart_date", "Depart Date"),
            ui.input_date("return_date", "Return Date"),
            ui.output_text_verbatim("flight_summary"),
            ui.download_button("book_flight", ui.tags.span(ui.tags.i(class_="fas fa-check-circle"), "Book Flight")),
        ),
        ui.card(
            ui.card_header("Hotel Booking"),
            ui.input_select("hotel_city", "City", [city for city, _, _, _ in HOTELS]),
            ui.input_numeric("nights", "Nights", min=1, max=30, value=1),
            ui.output_text_verbatim("hotel_summary"),
            ui.download_button("book_hotel", ui.tags.span(ui.tags.i(class_="fas fa-check-circle"), "Book Hotel")),
        ),
        width=1 / 2,
    ),
)

def server(input: Inputs, output: Outputs, session: Session):
    @reactive.calc
    def nights():
        return input.nights()
    
    @reactive.calc
    def available_flights() -> List[Tuple[str, str, str, str, float]]:
        from_city = input.from_city()
        to_city = input.to_city()
        depart_date = input.depart_date()
        return_date = input.return_date()

        if depart_date is None or return_date is None:
            return []

        return [
            flight
            for flight in FLIGHTS
            if flight[0] == from_city
            and flight[1] == to_city
            and flight[2] <= depart_date.strftime("%Y-%m-%d")
            and flight[3] >= return_date.strftime("%Y-%m-%d")
        ]

    @render.text
    def flight_summary():
        flights = available_flights()
        req(flights)
        return "\n".join(
            f"Flight from {from_city} to {to_city} on {depart_date} - {return_date}: ${price:.2f}"
            for from_city, to_city, depart_date, return_date, price in flights
        )

    @render.download
    def book_flight():
        flights = available_flights()
        req(flights)
        return f"Booking flight from {flights[0][0]} to {flights[0][1]} on {flights[0][2]} - {flights[0][3]}"

    @reactive.calc
    def available_hotels() -> List[Tuple[str, str, float, int]]:
        hotel_city = input.hotel_city()
        return [hotel for hotel in HOTELS if hotel[0] == hotel_city]

    @render.text
    def hotel_summary():
        hotels = available_hotels()
        req(hotels)
        nights_val = nights()
        return "\n".join(
            f"Hotel: {hotel_name}, {nights_val} nights, ${price * nights_val:.2f}"
            for city, hotel_name, price, _ in hotels
        )

    @render.download
    def book_hotel():
        hotels = available_hotels()
        req(hotels)
        return f"Booking {hotels[0][1]} in {hotels[0][0]} for {input.nights()} nights"

app = App(app_ui, server)