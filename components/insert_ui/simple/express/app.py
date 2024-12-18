from shiny import reactive
from shiny.express import input, ui, render

# Create a simple counter to track number of elements added
counter = reactive.value(0)

# Add action button to trigger UI insertion
ui.input_action_button("add", "Add UI Element")

# Add container div where elements will be inserted
ui.div(id="container")


@reactive.effect
@reactive.event(input.add)
def add_element():
    global counter
    count = counter.get() + 1
    counter.set(count)

    # Insert a new div with text and button
    ui.insert_ui(
        ui.div(
            f"Element {count}",
            ui.input_action_button(f"btn_{count}", "Click me!"),
            class_="mt-3 p-3 border rounded",
        ),
        selector="#container",
        where="beforeEnd",
    )
