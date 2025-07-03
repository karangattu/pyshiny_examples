from shiny import App, reactive, render, ui

app_ui = ui.page_fluid(
    ui.input_action_button("increment", "Increment"),
    ui.output_text("count"),
)

def server(input, output, session):
    counter = reactive.Value(0)

    @reactive.Effect
    @reactive.event(input.increment)
    def _():
        counter.set(counter() + 1)

    @output
    @render.text
    def count():
        return f"Button clicked {counter()} times"

app = App(app_ui, server)
