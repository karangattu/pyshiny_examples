from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.input_text("name", "Name", "World"),
    ui.output_text("greeting"),
)

def server(input, output, session):
    @output
    @render.text
    def greeting():
        return f"Hello, {input.name()}!"

app = App(app_ui, server)
