from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui

# Make up some data
data = [
    {"name": "John Doe", "age": 35, "city": "New York"},
    {"name": "Jane Smith", "age": 28, "city": "Los Angeles"},
    {"name": "Bob Johnson", "age": 42, "city": "Chicago"},
    {"name": "Sarah Lee", "age": 31, "city": "Miami"},
]

app_ui = ui.page_fluid(
    ui.input_text("name", "Name"),
    ui.input_numeric("age", "Age", min=0, max=100, value=0),  # Added 'value' argument
    ui.input_text("city", "City"),
    ui.input_action_button("submit", "Submit"),
    ui.output_ui("result"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @reactive.effect
    @reactive.event(input.submit)
    def _():
        req(input.name(), input.age(), input.city())

        # Find the matching person in the data
        person = next(
            (
                p
                for p in data
                if p["name"] == input.name()
                and p["age"] == input.age()
                and p["city"] == input.city()
            ),
            None,
        )

        if person:
            ui.notification_show(
                f"Found {person['name']}, age {person['age']} from {person['city']}",
                duration=5,
                type="message",
            )
        else:
            ui.notification_show("No matching person found", duration=5, type="error")

    @render.ui
    def result():
        return ui.tags.div()


app = App(app_ui, server)
