from shiny import reactive
from shiny.express import input, ui

# Create some sample data
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

ui.page_opts(title="Remove UI Demo")

with ui.sidebar():
    ui.input_select("name_select", "Select a name to add", names)
    ui.input_action_button("add_name", "Add Name")
    ui.input_action_button("remove_last", "Remove Last Name")

# Container to hold dynamically added names
ui.div(id="name_container")


@reactive.effect
@reactive.event(input.add_name)
def _():
    # Get the selected name
    selected_name = input.name_select()

    # Insert a new paragraph with the selected name
    ui.insert_ui(
        ui.p(selected_name, id=f"name_{selected_name}"),
        selector="#name_container",
        where="beforeEnd",
    )


@reactive.effect
@reactive.event(input.remove_last)
def _():
    # Find the last added name paragraph and remove it
    ui.remove_ui(selector="#name_container > p:last-child")
