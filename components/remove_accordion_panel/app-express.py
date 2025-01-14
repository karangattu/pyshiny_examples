from shiny import reactive
from shiny.express import input, render, ui

ui.page_opts(title="Remove Accordion Panels Demo", fillable=True)

# Create a list of sections that will be removed one by one
sections = ["A", "B", "C", "D", "E"]

# Keep track of which sections have been removed
remaining_sections = reactive.value(sections.copy())

ui.input_action_button(
    id="remove_panel", label=f"Remove Section {sections[0]}", class_="mt-3 mb-3"
)

with ui.accordion(id="acc", multiple=True, open=True):
    for letter in sections:
        with ui.accordion_panel(f"Section {letter}", value=f"section_{letter}"):
            f"This is content for section {letter}"


@render.text
def remaining_count():
    count = len(remaining_sections.get())
    return f"Remaining sections: {count}"


@reactive.effect
@reactive.event(input.remove_panel)
def handle_remove():
    current_sections = remaining_sections.get()
    if len(current_sections) > 0:
        # Get the next section to remove
        section_to_remove = current_sections[0]
        # Remove from our tracking list
        current_sections.pop(0)
        remaining_sections.set(current_sections)

        # Remove the accordion panel
        ui.remove_accordion_panel(
            "acc",  # The id of the accordion
            f"section_{section_to_remove}",  # The value of the panel to remove
        )

        # Update button text
        if len(current_sections) == 0:
            ui.update_action_button("remove_panel", label="All panels removed!")
        else:
            ui.update_action_button(
                "remove_panel", label=f"Remove Section {current_sections[0]}"
            )
