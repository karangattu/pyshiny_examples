from shiny import reactive
from shiny.express import input, render, ui

# Page title and description
ui.page_opts(title="remove_ui() demo", fillable=True)

ui.markdown(
    """
    # UI Removal Demo
    This app demonstrates how to dynamically remove UI elements.
    Click the button below to add text inputs, then use the remove button to remove them.
    """
)

# Add buttons for adding/removing UI elements
with ui.layout_column_wrap(width=1 / 2):
    ui.input_action_button("add", "Add Text Input", class_="btn-primary")
    ui.input_action_button("remove", "Remove Last Input", class_="btn-warning")

# Create a container for dynamic UI elements
ui.div(id="dynamic_inputs")

# Counter for unique IDs
input_counter = reactive.value(0)


@reactive.effect
@reactive.event(input.add)
def add_input():
    current_count = input_counter.get()
    input_counter.set(current_count + 1)

    ui.insert_ui(
        ui.input_text(
            f"txt_{current_count}",
            f"Input #{current_count + 1}",
            value="Type something here",
        ),
        selector="#dynamic_inputs",
        where="beforeEnd",
    )


@reactive.effect
@reactive.event(input.remove)
def remove_input():
    current_count = input_counter.get()
    if current_count > 0:
        # Remove the last added input
        ui.remove_ui(selector=f"div:has(> #txt_{current_count - 1})", multiple=False)
        input_counter.set(current_count - 1)


# Display current values
@render.ui
def show_values():
    values = []
    for i in range(input_counter.get()):
        input_id = f"txt_{i}"
        try:
            value = getattr(input, input_id)()
            if value:
                values.append(f"Input #{i + 1}: {value}")
        except:
            continue

    if not values:
        return "No inputs available"

    return ui.tags.div(
        ui.h4("Current Values:"), ui.tags.ul([ui.tags.li(v) for v in values])
    )
