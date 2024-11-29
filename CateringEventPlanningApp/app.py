import random
from datetime import datetime, timedelta
from typing import List, Tuple

from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui

# Sample data for catering and event planning
MENU_ITEMS = [
    ("Appetizers", ["Bruschetta", "Caprese Skewers", "Stuffed Mushrooms"]),
    ("Entrees", ["Grilled Salmon", "Chicken Parmesan", "Beef Tenderloin"]),
    ("Sides", ["Roasted Vegetables", "Mashed Potatoes", "Garlic Bread"]),
    ("Desserts", ["Tiramisu", "Cheesecake", "Chocolate Cake"]),
]

EVENT_TYPES = ["Wedding", "Corporate Event", "Birthday Party", "Graduation"]
EVENT_CAPACITIES = {
    "Wedding": 200,
    "Corporate Event": 150,
    "Birthday Party": 100,
    "Graduation": 300,
}


def get_available_dates(
    start_date: datetime, end_date: datetime
) -> List[Tuple[datetime, bool]]:
    available_dates = []
    current_date = start_date
    while current_date <= end_date:
        is_available = random.choice([True, False])
        available_dates.append((current_date, is_available))
        current_date += timedelta(days=1)
    return available_dates


app_ui = ui.page_fluid(
    ui.head_content(
        ui.HTML(
            '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">'
        )
    ),
    ui.panel_title("Catering and Event Planning"),
    ui.layout_column_wrap(
        ui.value_box(
            "Upcoming Events",
            "5",
            "Events Scheduled",
            showcase=ui.HTML('<i class="fa-solid fa-calendar-check"></i>'),
            theme="bg-gradient-primary",
        ),
        ui.value_box(
            "Total Revenue",
            "$50,000",
            "This Month",
            showcase=ui.HTML('<i class="fa-solid fa-dollar-sign"></i>'),
            theme="bg-gradient-success",
        ),
        ui.value_box(
            "Booked Capacity",
            "75%",
            "Of Total Capacity",
            showcase=ui.HTML('<i class="fa-solid fa-chart-pie"></i>'),
            theme="bg-gradient-warning",
        ),
    ),
    ui.hr(),
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Event Details"),
            ui.layout_column_wrap(
                ui.input_select("event_type", "Event Type", EVENT_TYPES),
                ui.input_date_range("event_date", "Event Date"),
                ui.input_numeric(
                    "num_guests", "Number of Guests", min=1, max=500, value=50
                ),
            ),
            width=6,
        ),
        ui.card(
            ui.card_header("Menu Selection"),
            ui.layout_column_wrap(
                *[
                    ui.input_checkbox_group(
                        f"menu_{category.lower().replace(' ', '_')}", category, items
                    )
                    for category, items in MENU_ITEMS
                ],
            ),
            width=6,
        ),
    ),
    ui.card(
        ui.card_header("Event Summary"),
        ui.output_text_verbatim("event_summary"),
        ui.download_button("download_invoice", "Download Invoice"),
        width=12,
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    @reactive.calc
    def get_dates():
        start_date = input.event_date()[0]
        end_date = input.event_date()[1]
        return get_available_dates(start_date, end_date)

    @render.text
    def event_summary():
        event_type = input.event_type()
        event_date = input.event_date()
        num_guests = input.num_guests()
        dates = get_dates()

        selected_date = None
        for date, is_available in dates:
            if date >= event_date[0] and date <= event_date[1]:
                if is_available:
                    selected_date = date
                    break

        if selected_date is None:
            return "Sorry, the selected date is not available. Please choose a different date."

        menu_items = []
        for category, items in MENU_ITEMS:
            selected_items = input[f"menu_{category.lower().replace(' ', '_')}"]()
            if selected_items:
                menu_items.append("{}: {}".format(category, ", ".join(selected_items)))

        event_capacity = EVENT_CAPACITIES[event_type]
        event_summary = """
        Event Type: {}
        Event Date: {}
        Number of Guests: {}
        Event Capacity: {}
        Menu Items:
        {}
        """.format(
            event_type,
            selected_date.strftime("%B %d, %Y"),
            num_guests,
            event_capacity,
            "\n".join(menu_items),
        )
        return event_summary

    @render.download
    def download_invoice():
        event_summary = event_summary()
        return event_summary


app = App(app_ui, server)
