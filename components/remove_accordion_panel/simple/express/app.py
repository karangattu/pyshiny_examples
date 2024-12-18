import random
from shiny import reactive
from shiny.express import input, ui

# Set page options
ui.page_opts(title="Remove Accordion Panel Demo", fillable=True)

# Create a list of sections to start with
choices = ["A", "B", "C", "D", "E"]
random.shuffle(choices)

# Create action button to remove panels
ui.input_action_button(
    "remove_panel",
    f"Remove Section {choices[-1]}",
    class_="mt-3 mb-3",
)

# Add explanatory text
ui.markdown("(Sections are randomly ordered at server start)")

# Create accordion with multiple panels
with ui.accordion(id="acc", multiple=True):
    for letter in "ABCDE":
        with ui.accordion_panel(f"Section {letter}"):
            f"Some narrative content for section {letter}"

# Keep track of available choices
user_choices = [choice for choice in choices]


@reactive.effect
@reactive.event(input.remove_panel)
def _():
    if len(user_choices) == 0:
        ui.notification_show("No more panels to remove!")
        return

    # Remove the last panel in our list
    ui.remove_accordion_panel("acc", f"Section {user_choices.pop()}")

    # Update the button label
    label = "No more panels to remove!"
    if len(user_choices) > 0:
        label = f"Remove Section {user_choices[-1]}"
    ui.update_action_button("remove_panel", label=label)
