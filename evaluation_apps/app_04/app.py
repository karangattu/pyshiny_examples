from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.input_checkbox("show_message", "Show message", False),
    ui.output_ui("message_ui"),
)


def server(input, output, session):
    @output
    @render.ui
    def message_ui():
        if input.show_message():
            return ui.p("This is a dynamically generated message.")
        else:
            return None


app = App(app_ui, server)
