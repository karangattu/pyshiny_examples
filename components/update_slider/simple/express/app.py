from shiny import reactive
from shiny.express import input, render, ui

# Page title and layout options
ui.page_opts(title="Slider Update Demo", fillable=True)

with ui.layout_sidebar():
    with ui.sidebar():
        # Control slider for min/max updates
        ui.input_slider("min_val", "Minimum Value", min=0, max=50, value=0)
        ui.input_slider("max_val", "Maximum Value", min=50, max=100, value=100)

        # Main slider that will be updated
        ui.input_slider("main_slider", "Main Slider", min=0, max=100, value=50)

    # Display current slider values
    @render.ui
    def show_values():
        return ui.tags.div(
            ui.tags.h4("Current Values:"),
            ui.tags.p(f"Min Value: {input.min_val()}"),
            ui.tags.p(f"Max Value: {input.max_val()}"),
            ui.tags.p(f"Main Slider Value: {input.main_slider()}"),
        )


# Effect to update the main slider when min/max controls change
@reactive.effect
def _():
    ui.update_slider(
        "main_slider",
        min=input.min_val(),
        max=input.max_val(),
        # Keep current value if within new range, otherwise clamp to min/max
        value=max(min(input.main_slider(), input.max_val()), input.min_val()),
    )
