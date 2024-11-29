from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Fake data for the app
data = [
    {"title": "Section A", "content": "This is the content for Section A."},
    {"title": "Section B", "content": "This is the content for Section B."},
    {"title": "Section C", "content": "This is the content for Section C."},
]

app_ui = ui.page_fluid(
    ui.accordion(
        *[ui.accordion_panel(item["title"], item["content"]) for item in data],
        id="accordion",
        multiple=True,
    )
)


def server(input: Inputs, output: Outputs, session: Session):
    pass


app = App(app_ui, server)
