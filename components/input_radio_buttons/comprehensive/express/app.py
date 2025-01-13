from shiny import reactive
from shiny.express import input, ui, render

# Sample data - dictionary with HTML content as values
choices_dict = {
    "red": ui.span("Red", style="color: red;"),
    "blue": ui.span("Blue", style="color: blue;"),
    "green": ui.span("Green", style="color: green;"),
}

# Simple list of choices
choices_list = ["Option A", "Option B", "Option C"]

ui.page_opts(title="Radio Buttons Demo", fillable=True)

with ui.layout_columns():
    # Basic radio buttons with a list
    with ui.card():
        ui.card_header("Basic Radio Buttons (List)")
        ui.input_radio_buttons(
            id="rb1",
            label="Choose an option:",
            choices=choices_list,
            selected="Option A",
        )

        @render.text
        def show_rb1():
            return f"Selected: {input.rb1()}"

    # Radio buttons with HTML choices and inline display
    with ui.card():
        ui.card_header("HTML Choices & Inline Display")
        ui.input_radio_buttons(
            id="rb2",
            label="Choose a color:",
            choices=choices_dict,
            selected="red",
            inline=True,
        )

        @render.text
        def show_rb2():
            return f"Selected color: {input.rb2()}"

    # Radio buttons with custom width
    with ui.card():
        ui.card_header("Custom Width")
        ui.input_radio_buttons(
            id="rb3",
            label="Fixed width radio buttons:",
            choices=choices_list,
            selected="Option B",
            width="200px",
        )

        @render.text
        def show_rb3():
            return f"Selected: {input.rb3()}"


# Dynamic update example
with ui.card():
    ui.card_header("Dynamic Updates")

    # Control buttons
    with ui.layout_columns(col_widths=[2, 2, 8]):
        ui.input_action_button("update_label", "Update Label")
        ui.input_action_button("update_choices", "Update Choices")

    ui.input_radio_buttons(
        id="rb4",
        label="Dynamic radio buttons:",
        choices=choices_list,
        selected="Option A",
    )

    @render.text
    def show_rb4():
        return f"Selected: {input.rb4()}"

    @reactive.effect
    @reactive.event(input.update_label)
    def _():
        ui.update_radio_buttons(
            "rb4", label=f"Updated Label (clicked: {input.update_label()})"
        )

    @reactive.effect
    @reactive.event(input.update_choices)
    def _():
        # Generate new choices when update button is clicked
        new_choices = [f"New Option {i}" for i in range(1, 4)]
        ui.update_radio_buttons("rb4", choices=new_choices, selected=new_choices[0])


# Show all parameters and their current values
with ui.card():
    ui.card_header("Current Parameter Values")

    @render.ui
    def show_params():
        params = {
            "id": "Various IDs (rb1, rb2, rb3, rb4)",
            "label": "Various labels shown above",
            "choices": "Both list and dictionary examples shown",
            "selected": "Different for each example",
            "inline": f"True for color selection, False for others",
            "width": "200px for third example, default for others",
        }

        return ui.tags.div(
            ui.tags.h4("Parameters Demonstrated:"),
            ui.tags.ul(
                [ui.tags.li(f"{key}: {value}") for key, value in params.items()]
            ),
        )
