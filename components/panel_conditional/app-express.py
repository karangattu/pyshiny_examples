from shiny import reactive
from shiny.express import input, ui, render

# Page options
ui.page_opts(title="Panel Conditional Demo", fillable=True)

with ui.layout_sidebar():
    with ui.sidebar():
        # Basic checkbox to control visibility
        ui.input_checkbox("show", "Show panels", True)

        # Add a slider to demonstrate numeric conditions
        ui.input_slider("value", "Slider value", min=0, max=100, value=75)

        # Display current state information
        @render.text
        def state():
            return (
                f"Current State:\n"
                f"Checkbox: {input.show()}\n"
                f"Slider: {input.value()}"
            )

    # Main content area
    with ui.card():
        ui.card_header("Panel Conditional Examples")

        # Basic panel that depends on checkbox
        with ui.panel_conditional("input.show"):
            ui.h4("Basic panel - visible when checkbox is checked")
            ui.markdown("This panel appears when the checkbox above is checked")
            ui.hr()

        # Panel that depends on multiple conditions combined
        with ui.panel_conditional("input.show && input.value > 50"):
            ui.h4("Panel with multiple conditions")
            ui.markdown(
                "This panel appears when checkbox is checked AND slider value > 50"
            )
            ui.hr()

        # Panel with a more complex JavaScript condition
        with ui.panel_conditional(
            "input.show && (input.value > 75 || input.value < 25)",
            id="complex_panel",
            class_="p-3 bg-light border rounded",
        ):
            ui.h4("Panel with complex conditions")
            ui.markdown(
                "This panel appears when checkbox is checked AND slider value is > 75 OR < 25"
            )
