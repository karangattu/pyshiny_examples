import random
from datetime import datetime, timedelta
from typing import List, Tuple

from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Sample event data
events: List[Tuple[str, datetime, datetime]] = [
    ("Company Picnic", datetime(2024, 6, 1, 12, 0), datetime(2024, 6, 1, 16, 0)),
    ("Team Offsite", datetime(2024, 7, 15, 9, 0), datetime(2024, 7, 15, 17, 0)),
    ("Client Meeting", datetime(2024, 8, 10, 14, 0), datetime(2024, 8, 10, 15, 30)),
    ("Holiday Party", datetime(2024, 12, 20, 19, 0), datetime(2024, 12, 20, 23, 0)),
]

app_ui = ui.page_fluid(
    ui.panel_title("Event Management and Scheduling"),
    ui.markdown(
        """
    <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css'>
    """
    ),
    ui.layout_column_wrap(
        ui.value_box(
            "Upcoming Events",
            ui.output_text("upcoming_events_count"),
            theme="bg-gradient-orange-red",
            showcase=ui.tags.i(class_="fas fa-calendar-alt"),
        ),
        ui.value_box(
            "Past Events",
            ui.output_text("past_events_count"),
            theme="bg-gradient-blue-purple",
            showcase=ui.tags.i(class_="fas fa-history"),
        ),
        ui.card(
            ui.card_header(
                ui.h4(ui.tags.i(class_="fas fa-calendar-check me-2"), "Event Calendar")
            ),
            ui.output_ui("calendar"),
            full_screen=True,
        ),
        ui.card(
            ui.card_header(
                ui.h4(ui.tags.i(class_="fas fa-info-circle me-2"), "Event Details")
            ),
            ui.output_ui("event_details"),
            full_screen=True,
        ),
        width=1 / 2,
    ),
    ui.input_action_button(
        "add_event",
        "Add New Event",
        class_="btn-primary mt-3",
        icon=ui.tags.i(class_="fas fa-plus-circle me-2"),
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    # Reactive value to store events (mutable)
    event_list = reactive.Value(events)

    @output
    @render.text
    def upcoming_events_count():
        return str(len([e for e in event_list() if e[1] > datetime.now()]))

    @output
    @render.text
    def past_events_count():
        return str(len([e for e in event_list() if e[1] <= datetime.now()]))

    # Reactive value to track selected event
    selected_event = reactive.Value(None)

    @render.ui
    def calendar():
        return ui.input_date("event_calendar", "Select Date")

    @reactive.effect
    @reactive.event(input.event_calendar)
    def _():
        selected_date = input.event_calendar()
        if selected_date is not None:
            updated_events = [e for e in event_list() if e[1].date() == selected_date]
            if updated_events:
                selected_event.set(updated_events[0])

    @render.ui
    def event_details():
        event = selected_event()
        if event is None:
            return ui.p(
                ui.tags.i(class_="fas fa-info-circle me-2"),
                "Select an event to view details",
            )
        else:
            name, start, end = event
            return ui.layout_column_wrap(
                ui.h3(ui.tags.i(class_="fas fa-calendar-day me-2"), name),
                ui.p(
                    ui.tags.i(class_="fas fa-clock me-2"),
                    f"Start: {start.strftime('%Y-%m-%d %H:%M')}",
                ),
                ui.p(
                    ui.tags.i(class_="fas fa-clock me-2"),
                    f"End: {end.strftime('%Y-%m-%d %H:%M')}",
                ),
                ui.input_action_button(
                    "edit_event",
                    "Edit Event",
                    icon=ui.tags.i(class_="fas fa-edit me-2"),
                ),
                ui.input_action_button(
                    "delete_event",
                    "Delete Event",
                    icon=ui.tags.i(class_="fas fa-trash-alt me-2"),
                ),
                width=1,
            )

    @reactive.effect
    @reactive.event(input.delete_event)
    def _():
        event = selected_event()
        if event is not None:
            name, _, _ = event
            # Remove the event from the list
            updated_events = [e for e in event_list() if e[0] != name]
            event_list.set(updated_events)
            selected_event.set(None)
            ui.notification_show(
                f"Deleted event: {name}", title="Event Deleted", type="warning"
            )

    @reactive.effect
    @reactive.event(input.add_event)
    def _():
        # This could be expanded to show a modal for adding a new event
        ui.notification_show(
            "Add Event functionality to be implemented",
        )

    @reactive.effect
    @reactive.event(input.edit_event)
    def _():
        event = selected_event()
        if event is not None:
            name, _, _ = event
            # This could be expanded to show a modal for editing the event
            ui.notification_show(
                f"Edit Event functionality to be implemented for: {name}",
            )


app = App(app_ui, server)
