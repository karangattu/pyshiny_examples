from shiny import App, reactive, render, ui

# Create a list of sections that will be removed one by one
sections = ["A", "B", "C", "D", "E"]

app_ui = ui.page_fillable(
    ui.input_action_button(
        id="remove_panel", label=f"Remove Section {sections[0]}", class_="mt-3 mb-3"
    ),
    ui.accordion(
        *[
            ui.accordion_panel(
                f"Section {letter}",
                f"This is content for section {letter}",
                value=f"section_{letter}",
            )
            for letter in sections
        ],
        id="acc",
        multiple=True,
        open=True,
    ),
    ui.output_text("remaining_count"),
    fillable_mobile=True,
)


def server(input, output, session):
    # Keep track of which sections have been removed
    remaining_sections = reactive.value(sections.copy())

    @output
    @render.text
    def remaining_count():
        count = len(remaining_sections())
        return f"Remaining sections: {count}"

    @reactive.effect
    @reactive.event(input.remove_panel)
    def handle_remove():
        current_sections = remaining_sections()
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


app = App(app_ui, server)
