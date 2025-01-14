from shiny import reactive
from shiny.express import input, ui, render

# Sample data for different selectize examples
states = {
    "East Coast": {"NY": "New York", "NJ": "New Jersey", "CT": "Connecticut"},
    "West Coast": {"WA": "Washington", "OR": "Oregon", "CA": "California"},
    "Midwest": {"MN": "Minnesota", "WI": "Wisconsin", "IA": "Iowa"},
}

# Set page options
ui.page_opts(title="Selectize Input Demo")

# Layout with cards
with ui.layout_column_wrap(width=1 / 2):
    # Basic selectize with single selection
    with ui.card(height="200px"):
        ui.card_header("Basic Single Selection")
        ui.input_selectize(id="select1", label="Choose a state:", choices=states)

        @render.text
        def value1():
            return f"Selected: {input.select1()}"

    # Multiple selection with remove button
    with ui.card(height="200px"):
        ui.card_header("Multiple Selection")
        ui.input_selectize(
            id="select2",
            label="Choose multiple states:",
            choices=states,
            multiple=True,
            options={"plugins": ["remove_button"]},
        )

        @render.text
        def value2():
            return f"Selected: {input.select2()}"

    # Selectize with custom options
    with ui.card(height="200px"):
        ui.card_header("Custom Options")
        ui.input_selectize(
            id="select3",
            label="With placeholder:",
            choices=states,
            multiple=True,
            options={"placeholder": "Select states...", "plugins": ["remove_button"]},
        )

        @render.text
        def value3():
            return f"Selected: {input.select3()}"

    # Dynamic updates example
    with ui.card(height="200px"):
        ui.card_header("Dynamic Updates")
        ui.input_action_button("update_btn", "Update Choices", class_="mb-3")
        ui.input_selectize(
            id="select4",
            label="Dynamically updated choices:",
            choices=[],
            multiple=True,
        )

        @reactive.effect
        @reactive.event(input.update_btn)
        def _():
            new_choices = {f"Option {i}": f"Value {i}" for i in range(1, 6)}
            ui.update_selectize("select4", choices=new_choices, selected=["Option 1"])

        @render.text
        def value4():
            return f"Selected: {input.select4()}"

    # Server-side selectize example
    with ui.card(height="200px"):
        ui.card_header("Server-side Processing")
        ui.input_selectize(
            id="select5", label="Server-side search:", choices=[], multiple=True
        )

        @reactive.effect
        def _():
            # Generate large dataset
            large_choices = {f"Item {i}": f"Description {i}" for i in range(1, 1001)}
            ui.update_selectize(
                "select5", choices=large_choices, server=True, options={"maxItems": 5}
            )

        @render.text
        def value5():
            return f"Selected: {input.select5()}"

    # Width specification example
    with ui.card(height="200px"):
        ui.card_header("Custom Width")
        ui.input_selectize(
            id="select6", label="Fixed width selectize:", choices=states, width="200px"
        )

        @render.text
        def value6():
            return f"Selected: {input.select6()}"
