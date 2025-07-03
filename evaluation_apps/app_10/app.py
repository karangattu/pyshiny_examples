from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.input_password("password", "Password"),
    ui.output_text("password_length"),
)

def server(input, output, session):
    @output
    @render.text
    def password_length():
        return f"Password length: {len(input.password())}"

app = App(app_ui, server)
