from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Modal Remove Demo", fillable=True)

# Create buttons to show different types of modals
with ui.layout_column_wrap():
    ui.input_action_button("show_basic", "Show Basic Modal", class_="m-2")
    ui.input_action_button("show_complex", "Show Complex Modal", class_="m-2")
    ui.input_action_button("show_form", "Show Form Modal", class_="m-2")


# Create a display area for status messages
@render.ui
def status_display():
    ui.div(
        "Status messages will appear here",
        id="status_area",
        class_="p-3 m-2 border rounded",
    )


# Handler for basic modal
@reactive.effect
@reactive.event(input.show_basic)
def show_basic_modal():
    modal = ui.modal(
        "This is a basic modal that will be removed automatically",
        title="Basic Modal",
        easy_close=True,
    )
    ui.modal_show(modal)


# Handler for complex modal with manual removal
@reactive.effect
@reactive.event(input.show_complex)
def show_complex_modal():
    modal = ui.modal(
        ui.input_text("name", "Enter your name"),
        ui.input_numeric("age", "Enter your age", value=25),
        ui.layout_column_wrap(
            ui.input_action_button("modal_cancel", "Cancel", class_="btn-danger"),
            ui.input_action_button("modal_submit", "Submit", class_="btn-success"),
        ),
        title="Complex Modal",
        easy_close=False,
    )
    ui.modal_show(modal)


# Handler for form modal
@reactive.effect
@reactive.event(input.show_form)
def show_form_modal():
    modal = ui.modal(
        ui.input_select(
            "choice", "Select an option", choices=["Option A", "Option B", "Option C"]
        ),
        ui.input_text_area(
            "comments", "Additional Comments", value="Enter your comments here..."
        ),
        ui.layout_column_wrap(
            ui.input_action_button("form_cancel", "Cancel", class_="btn-secondary"),
            ui.input_action_button("form_submit", "Submit", class_="btn-primary"),
        ),
        title="Form Modal",
        easy_close=False,
    )
    ui.modal_show(modal)


# Handlers for modal actions
@reactive.effect
@reactive.event(input.modal_cancel)
def handle_modal_cancel():
    ui.modal_remove()
    ui.notification_show("Complex modal cancelled", type="warning")


@reactive.effect
@reactive.event(input.modal_submit)
def handle_modal_submit():
    ui.modal_remove()
    ui.notification_show(
        f"Submitted: Name={input.name()}, Age={input.age()}", type="message"
    )


@reactive.effect
@reactive.event(input.form_cancel)
def handle_form_cancel():
    ui.modal_remove()
    ui.notification_show("Form cancelled", type="warning")


@reactive.effect
@reactive.event(input.form_submit)
def handle_form_submit():
    ui.modal_remove()
    ui.notification_show(
        f"Form submitted: Choice={input.choice()}, Comments={input.comments()}",
        type="message",
    )
