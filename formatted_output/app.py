from shiny import App, Inputs, Outputs, Session, render, ui

app_ui = ui.page_fluid(
    ui.input_text("text_input", "Enter some text:"),
    ui.output_ui("text_output"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.text
    def text_output():
        # Make up some data for the output
        return ui.markdown(
            f"You entered: <strong>{input.text_input()}</strong>",
        )


app = App(app_ui, server)
