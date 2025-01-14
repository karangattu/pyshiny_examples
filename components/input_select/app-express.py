from shiny import reactive
from shiny.express import input, ui, render

# Sample data for different types of choices
simple_choices = ["A", "B", "C", "D"]
dict_choices = {"a": "Option A", "b": "Option B", "c": "Option C"}
grouped_choices = {
    "Group 1": {"g1a": "Group 1 - A", "g1b": "Group 1 - B"},
    "Group 2": {"g2a": "Group 2 - A", "g2b": "Group 2 - B"},
}

# Page options
ui.page_opts(title="input_select Demo", fillable=True)

with ui.layout_column_wrap(width="400px"):
    # Basic select with simple choices
    with ui.card():
        ui.card_header("Basic Select")
        ui.input_select(
            id="select1",
            label="Basic select (simple list)",
            choices=simple_choices,
            selected="A",
        )

    # Select with dictionary choices
    with ui.card():
        ui.card_header("Dictionary Choices")
        ui.input_select(
            id="select2",
            label="Select with dictionary choices",
            choices=dict_choices,
            selected="a",
        )

    # Select with grouped choices
    with ui.card():
        ui.card_header("Grouped Choices")
        ui.input_select(
            id="select3",
            label="Select with grouped choices",
            choices=grouped_choices,
            selected="g1a",
        )

    # Multiple select
    with ui.card():
        ui.card_header("Multiple Select")
        ui.input_select(
            id="select4",
            label="Multiple select",
            choices=simple_choices,
            selected=["A", "B"],
            multiple=True,
        )

    # Select with custom width
    with ui.card():
        ui.card_header("Custom Width")
        ui.input_select(
            id="select5",
            label="Select with custom width",
            choices=simple_choices,
            width="200px",
        )

    # Select with size parameter
    with ui.card():
        ui.card_header("Box Style")
        ui.input_select(
            id="select6",
            label="Select with size parameter",
            choices=simple_choices,
            size="4",  # Shows 4 items at once
        )

# Display selected values in a card
with ui.card():
    ui.card_header("Selected Values")

    @render.text
    def selected_values():
        return (
            f"Select 1: {input.select1()}\n"
            f"Select 2: {input.select2()}\n"
            f"Select 3: {input.select3()}\n"
            f"Select 4: {input.select4()}\n"
            f"Select 5: {input.select5()}\n"
            f"Select 6: {input.select6()}"
        )
