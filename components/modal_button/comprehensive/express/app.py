from shiny import reactive
from shiny.express import input, ui

# Synthetic data for demonstration
departments = {
    "Engineering": ["Software Dev", "Hardware Eng", "QA", "DevOps"],
    "Marketing": ["Digital Marketing", "Brand Strategy", "Content", "Social Media"],
    "Sales": [
        "Inside Sales",
        "Outside Sales",
        "Account Management",
        "Business Development",
    ],
    "HR": ["Recruitment", "Training", "Employee Relations", "Compensation"],
}

ui.page_opts(title="Modal Button Showcase", fillable=True)

with ui.sidebar():
    ui.input_select("department", "Select Department", choices=list(departments.keys()))
    ui.input_action_button("show_modal", "Show Modal")


# Different modal configurations
@reactive.effect
@reactive.event(input.show_modal)
def _():
    # Modal with different configurations
    m = ui.modal(
        ui.input_select("team", "Select Team", choices=departments[input.department()]),
        title=f"{input.department()} Department Teams",
        footer=[
            ui.modal_button("Select", icon="check-circle"),  # Basic modal button
            ui.modal_button(
                "Cancel", icon="x-circle", class_="btn-secondary"  # Custom styling
            ),
        ],
        size="l",  # Large modal
        easy_close=True,
        fade=True,
    )
    ui.modal_show(m)


# Reactive output to show selected team
@reactive.effect
@reactive.event(input.team)
def _():
    if input.team():
        ui.notification_show(
            f"You selected {input.team()} team", duration=3, type="message"
        )


# Footer with different modal button configurations
with ui.card():
    ui.card_header("Modal Button Configurations")

    # Demonstration of various modal button styles and icons
    with ui.layout_column_wrap(width=1 / 2):
        ui.input_action_button("modal_primary", "Primary Modal", class_="btn-primary")
        ui.input_action_button(
            "modal_secondary", "Secondary Modal", class_="btn-secondary"
        )


# Different modal configurations
@reactive.effect
@reactive.event(input.modal_primary)
def show_primary_modal():
    m = ui.modal(
        "This is a primary modal with custom buttons.",
        title="Primary Modal",
        footer=[
            ui.modal_button(
                "Confirm",
                icon=ui.tags.i(class_="fa-solid fa-check"),  # Font Awesome icon
                class_="btn-primary",
            ),
            ui.modal_button(
                "Close",
                icon=ui.tags.i(class_="fa-solid fa-times"),  # Font Awesome icon
                class_="btn-secondary",
            ),
        ],
        size="m",
        easy_close=True,
    )
    ui.modal_show(m)


@reactive.effect
@reactive.event(input.modal_secondary)
def show_secondary_modal():
    m = ui.modal(
        "This is a secondary modal with alternative styling.",
        title="Secondary Modal",
        footer=[
            ui.modal_button(
                "Proceed",
                icon=ui.tags.i(class_="fa-solid fa-arrow-right"),
                class_="btn-warning",
            ),
            ui.modal_button(
                "Dismiss", icon=ui.tags.i(class_="fa-solid fa-ban"), class_="btn-danger"
            ),
        ],
        size="s",
        fade=False,
    )
    ui.modal_show(m)


# Add Font Awesome CSS
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.0/css/all.min.css">'
    )
)
