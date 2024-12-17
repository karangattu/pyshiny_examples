from shiny import reactive
from shiny.express import input, ui

# Create some synthetic data
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
ages = [25, 30, 35, 40, 45]
cities = ["New York", "San Francisco", "Chicago", "Boston", "Seattle"]

ui.page_opts(title="Insert UI Demo")

with ui.sidebar():
    ui.input_action_button("add_person", "Add Person")
    ui.input_action_button("clear_people", "Clear All")

# Container for dynamically added people
ui.div(id="people_container")


@reactive.effect
@reactive.event(input.add_person)
def _():
    # Generate a unique ID for the new person
    person_id = f"person_{input.add_person()}"

    # Select a random person from our synthetic data
    index = (input.add_person() - 1) % len(names)
    name = names[index]
    age = ages[index]
    city = cities[index]

    # Create a card for the new person
    new_person_card = ui.card(
        ui.h4(name), ui.p(f"Age: {age}"), ui.p(f"City: {city}"), id=person_id
    )

    # Insert the new person card into the container
    ui.insert_ui(new_person_card, selector="#people_container", where="beforeEnd")


@reactive.effect
@reactive.event(input.clear_people)
def _():
    # Remove all previously inserted people
    ui.remove_ui(selector="#people_container > *")
