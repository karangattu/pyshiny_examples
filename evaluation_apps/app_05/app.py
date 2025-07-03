from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.input_radio_buttons(
        "choice", "Choose one:", ["A", "B", "C"]
    ),
    ui.output_text("result"),
)

def server(input, output, session):
    @output
    @render.text
    def result():
        return f"You chose: {input.choice()}"

app = App(app_ui, server)
