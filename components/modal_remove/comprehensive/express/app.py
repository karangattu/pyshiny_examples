from shiny import reactive, ui
from shiny.express import input, render, ui as express_ui

# Synthetic data for demonstration
user_data = {
    "names": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "roles": ["Developer", "Manager", "Designer", "Analyst", "Tester"],
    "departments": ["Engineering", "HR", "Design", "Analytics", "QA"],
}

# Use express_ui.page_opts instead of ui.page_opts
express_ui.page_opts(title="Modal Remove Demonstration", fillable=True)

with ui.sidebar():
    ui.input_action_button("show_modal", "Show Modal")
    ui.input_action_button("remove_modal", "Remove Modal")
    ui.input_action_button("remove_specific_modal", "Remove Specific Modal")


# Modals with different configurations
def create_basic_modal():
    return ui.modal(
        "This is a basic modal that can be removed.",
        title="Basic Modal",
        easy_close=True,
    )


def create_complex_modal():
    return ui.modal(
        ui.p("This is a more complex modal with multiple elements."),
        ui.input_text("user_name", "Enter your name"),
        ui.input_select("user_role", "Select your role", choices=user_data["roles"]),
        title="Complex Modal",
        footer=ui.modal_button("Close"),
        size="l",
    )


@reactive.effect
@reactive.event(input.show_modal)
def _():
    # Show different modals based on button clicks
    if input.show_modal() % 2 == 0:
        m = create_basic_modal()
    else:
        m = create_complex_modal()

    ui.modal_show(m)


@reactive.effect
@reactive.event(input.remove_modal)
def _():
    # Demonstrate modal removal
    ui.modal_remove()
    ui.notification_show("Modal removed!", duration=2)


@reactive.effect
@reactive.event(input.remove_specific_modal)
def _():
    # Simulate removing a specific modal (though in this simple example, it's the same)
    ui.modal_remove()
    ui.notification_show("Specific modal removed!", duration=2)


# Optional: Display current modal state
@render.text
def modal_state():
    return f"Modal show count: {input.show_modal()}"
