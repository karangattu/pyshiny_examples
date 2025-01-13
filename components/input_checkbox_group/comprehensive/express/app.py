from shiny import reactive
from shiny.express import input, ui, render

# Sample data - dictionary mapping values to HTML labels
choices_dict = {
    "red": ui.span("Red", style="color: #FF0000;"),
    "green": ui.span("Green", style="color: #00AA00;"),
    "blue": ui.span("Blue", style="color: #0000AA;"),
}

# Simple list of choices
choices_list = ["Option A", "Option B", "Option C", "Option D"]

ui.page_opts(title="Checkbox Group Demo", fillable=True)

with ui.layout_columns():
    # Example 1: Basic usage with a list and all parameters
    with ui.card():
        ui.card_header("Basic Checkbox Group")
        ui.input_checkbox_group(
            id="basic_group",
            label="Choose multiple options:",
            choices=choices_list,
            selected=["Option A", "Option B"],
            inline=False,
            width="300px",
        )

        @render.text
        def basic_result():
            if input.basic_group():
                return f"You selected: {', '.join(input.basic_group())}"
            return "Nothing selected"

    # Example 2: Using HTML labels with dictionary and inline layout
    with ui.card():
        ui.card_header("Styled Checkbox Group")
        ui.input_checkbox_group(
            id="styled_group",
            label="Choose colors:",
            choices=choices_dict,
            selected=["red"],
            inline=True,
            width="100%",
        )

        @render.text
        def styled_result():
            if input.styled_group():
                return f"Colors selected: {', '.join(input.styled_group())}"
            return "No colors selected"


# Dynamic update example
with ui.card():
    ui.card_header("Dynamic Control")

    # Controls for updating the checkbox group
    with ui.layout_columns():
        ui.input_switch("use_inline", "Use inline layout", value=False)
        ui.input_numeric("width_px", "Width (px)", value=300, min=100, max=800)

    @reactive.effect
    def _():
        ui.update_checkbox_group(
            "basic_group", inline=input.use_inline(), width=f"{input.width_px()}px"
        )


# Show current state of all inputs
with ui.card():
    ui.card_header("Current State")

    @render.ui
    def show_state():
        return ui.tags.div(
            ui.tags.p(f"Basic group value: {input.basic_group()}"),
            ui.tags.p(f"Styled group value: {input.styled_group()}"),
            ui.tags.p(f"Inline layout: {input.use_inline()}"),
            ui.tags.p(f"Width setting: {input.width_px()}px"),
        )
