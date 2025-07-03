from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.input_select("select", "Select an option", {"A": "Option A", "B": "Option B"}),
    ui.output_text("selected_option"),
)

def server(input, output, session):
    @output
    @render.text
    def selected_option():
        return f"You selected: {input.select()}"

app = App(app_ui, server)
