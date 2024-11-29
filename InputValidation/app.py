from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui
import random

# Made-up data
data = {
    "name": ["John", "Jane", "Bob", "Alice"],
    "age": [25, 32, 45, 28],
    "city": ["New York", "Los Angeles", "Chicago", "Miami"],
}

app_ui = ui.page_fluid(
    ui.input_text("name", "Name", placeholder="Enter a name"),
    ui.input_numeric("age", "Age", min=0, max=120, value=30),
    ui.input_text("city", "City", placeholder="Enter a city"),
    ui.output_text_verbatim("output"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.text
    def output():
        req(input.name(), input.age(), input.city())
        index = data["name"].index(input.name())
        return f"Name: {data['name'][index]}, Age: {data['age'][index]}, City: {data['city'][index]}"


app = App(app_ui, server)
