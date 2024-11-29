from shiny import App, Inputs, Outputs, Session, render, ui

# Sample data for the dropdown
choices = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]

app_ui = ui.page_fluid(
    ui.input_select("dropdown", "Select an option", choices),
    ui.output_text("selected_choice"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.text
    def selected_choice():
        return f"You selected: {input.dropdown()}"


app = App(app_ui, server)
