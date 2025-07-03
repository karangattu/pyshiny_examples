from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.input_slider("n", "N", 1, 100, 20),
    ui.output_text_verbatim("txt"),
)


def server(input, output, session):
    @render.text
    def txt():
        return f"The value of n is {input.n()}"


app = App(app_ui, server)
