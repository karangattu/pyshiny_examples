from shiny import reactive
from shiny.express import input, ui, render

# Page options for better layout
ui.page_opts(title="Input Switch Demo", fillable=True)

with ui.layout_column_wrap(width=1 / 2):
    # Basic switch with default parameters
    with ui.card(full_screen=True):
        ui.card_header("Basic Switch")
        ui.input_switch(id="switch_basic", label="Basic switch", value=False)

        @render.text
        def basic_value():
            return f"Basic switch value: {input.switch_basic()}"

    # Switch with width parameter
    with ui.card(full_screen=True):
        ui.card_header("Switch with Custom Width")
        ui.input_switch(
            id="switch_width",
            label="Width customized switch",
            value=True,
            width="200px",
        )

        @render.text
        def width_value():
            return f"Width switch value: {input.switch_width()}"


# Effect demonstration
switch_count = reactive.value(0)


@reactive.effect
def count_switches():
    if input.switch_basic():
        switch_count.set(switch_count.get() + 1)


# Display switch count
with ui.card():
    ui.card_header("Switch Counter")

    @render.text
    def show_count():
        return f"Number of times basic switch turned on: {switch_count.get()}"


# Switch states affecting UI
with ui.layout_column_wrap(width=1 / 2):
    with ui.card(full_screen=True):
        ui.card_header("Conditional Content")
        ui.input_switch(id="show_content", label="Show/Hide Content", value=False)

        @render.ui
        def conditional_content():
            if input.show_content():
                return ui.markdown(
                    """
                ### Hidden Content
                This content is only visible when the switch is ON!
                """
                )
            return ""

    # Switch controlling theme
    with ui.card(full_screen=True):
        ui.card_header("Theme Control")
        ui.input_switch(id="theme_switch", label="Toggle Card Theme", value=False)

        @render.ui
        def theme_content():
            theme_class = (
                "bg-light" if not input.theme_switch() else "bg-dark text-light"
            )
            return ui.div(
                "This card's theme changes based on the switch!",
                class_=theme_class,
                style="padding: 1rem; border-radius: 4px;",
            )


# Switch affecting other inputs
with ui.card():
    ui.card_header("Input Control")
    ui.input_switch(id="enable_inputs", label="Enable/Disable Other Inputs", value=True)

    @render.ui
    def dynamic_inputs():
        disabled = not input.enable_inputs()
        return ui.div(
            ui.input_text("text_input", "Text Input", disabled=disabled),
            ui.input_numeric(
                "numeric_input", "Numeric Input", value=0, disabled=disabled
            ),
            style="margin-top: 1rem;",
        )


# Technical details about the switches
with ui.card():
    ui.card_header("Technical Information")

    @render.data_frame
    def switch_info():
        import pandas as pd

        data = {
            "Switch ID": [
                "switch_basic",
                "switch_width",
                "show_content",
                "theme_switch",
                "enable_inputs",
            ],
            "Current Value": [
                input.switch_basic(),
                input.switch_width(),
                input.show_content(),
                input.theme_switch(),
                input.enable_inputs(),
            ],
            "Purpose": [
                "Basic demonstration",
                "Width customization",
                "Content visibility control",
                "Theme toggling",
                "Input state management",
            ],
        }
        return pd.DataFrame(data)
