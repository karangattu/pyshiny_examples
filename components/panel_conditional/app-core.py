from shiny import App, reactive, render, ui

app_ui = ui.page_fillable(
    ui.layout_sidebar(
        ui.sidebar(
            # Basic checkbox to control visibility
            ui.input_checkbox("show", "Show panels", True),
            # Add a slider to demonstrate numeric conditions
            ui.input_slider("value", "Slider value", min=0, max=100, value=75),
            # Display current state information
            ui.output_text_verbatim("state"),
        ),
        # Main content area
        ui.card(
            ui.card_header("Panel Conditional Examples"),
            # Basic panel that depends on checkbox
            ui.panel_conditional(
                "input.show",
                ui.h4("Basic panel - visible when checkbox is checked"),
                ui.markdown("This panel appears when the checkbox above is checked"),
                ui.hr(),
            ),
            # Panel that depends on multiple conditions combined
            ui.panel_conditional(
                "input.show && input.value > 50",
                ui.h4("Panel with multiple conditions"),
                ui.markdown(
                    "This panel appears when checkbox is checked AND slider value > 50"
                ),
                ui.hr(),
            ),
            # Panel with a more complex JavaScript condition
            ui.panel_conditional(
                "input.show && (input.value > 75 || input.value < 25)",
                ui.h4("Panel with complex conditions"),
                ui.markdown(
                    "This panel appears when checkbox is checked AND slider value is > 75 OR < 25"
                ),
                id="complex_panel",
                class_="p-3 bg-light border rounded",
            ),
        ),
    )
)


def server(input, output, session):
    @output
    @render.text
    def state():
        return (
            f"Current State:\n" f"Checkbox: {input.show()}\n" f"Slider: {input.value()}"
        )


app = App(app_ui, server)
