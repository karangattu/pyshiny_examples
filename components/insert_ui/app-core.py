from shiny import App, reactive, ui

app_ui = ui.page_fluid(
    # A single button to trigger UI insertions
    ui.input_action_button("add", "Add UI Elements", class_="btn btn-primary mb-3"),
    # A container div to help with UI insertion positions
    ui.div(
        "Click the button above to add UI elements in different positions",
        id="demo_container",
        class_="p-3 border rounded",
    ),
)


def server(input, output, session):
    # Counter to make unique IDs for inserted elements
    counter = reactive.value(0)

    @reactive.effect
    @reactive.event(input.add)
    def _():
        count = counter.get()

        # beforeBegin - insert before the container
        ui.insert_ui(
            ui.div(
                f"Element {count}: beforeBegin",
                class_="alert alert-primary mt-2",
                id=f"before_begin_{count}",
            ),
            selector="#demo_container",
            where="beforeBegin",
        )

        # afterBegin - insert at the start inside the container
        ui.insert_ui(
            ui.div(
                f"Element {count}: afterBegin",
                class_="alert alert-success mt-2",
                id=f"after_begin_{count}",
            ),
            selector="#demo_container",
            where="afterBegin",
        )

        # beforeEnd - insert at the end inside the container
        ui.insert_ui(
            ui.div(
                f"Element {count}: beforeEnd",
                class_="alert alert-warning mt-2",
                id=f"before_end_{count}",
            ),
            selector="#demo_container",
            where="beforeEnd",
        )

        # afterEnd - insert after the container
        ui.insert_ui(
            ui.div(
                f"Element {count}: afterEnd",
                class_="alert alert-info mt-2",
                id=f"after_end_{count}",
            ),
            selector="#demo_container",
            where="afterEnd",
        )

        counter.set(count + 1)


app = App(app_ui, server)
