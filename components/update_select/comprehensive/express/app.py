from shiny import reactive
from shiny.express import input, ui, render

# Sample data for different scenarios
states = {
    "East Coast": {"NY": "New York", "NJ": "New Jersey", "CT": "Connecticut"},
    "West Coast": {"WA": "Washington", "OR": "Oregon", "CA": "California"},
    "Midwest": {"MN": "Minnesota", "WI": "Wisconsin", "IA": "Iowa"},
}

fruits = ["Apple", "Banana", "Orange", "Grape", "Mango"]

ui.page_opts(title="update_select Demo", fillable=True)

with ui.layout_sidebar():
    with ui.sidebar():
        ui.h4("Control Panel")
        ui.input_action_button("update_label", "Update Label")
        ui.input_action_button("update_choices", "Update Choices")
        ui.input_action_button("update_selected", "Update Selected")
        ui.input_action_button("clear_all", "Clear All Choices")
        ui.input_action_button("reset", "Reset to Default")
        ui.hr()
        ui.input_radio_buttons(
            "choice_type",
            "Choice Type",
            {
                "simple": "Simple List",
                "grouped": "Grouped Options",
                "empty": "Empty Choices",
            },
        )

    with ui.card():
        ui.card_header("Demo Select Input")
        # The select input we'll be updating
        ui.input_select(
            "demo_select",
            "Choose items:",
            choices=fruits,
            selected="Apple",
            multiple=True,
        )

        @render.ui
        def selection_info():
            current = input.demo_select()
            if not current:
                return ui.p("No items selected", class_="text-muted")
            if isinstance(current, list):
                return ui.p(f"Selected items: {', '.join(current)}")
            return ui.p(f"Selected item: {current}")


# Define reactive effects for each update operation
@reactive.effect
@reactive.event(input.update_label)
def _():
    counter = input.update_label()
    ui.update_select("demo_select", label=f"Choose items (Updated {counter} times):")


@reactive.effect
@reactive.event(input.update_choices)
def _():
    choice_type = input.choice_type()

    if choice_type == "simple":
        new_choices = ["Option " + str(i) for i in range(1, 6)]
        ui.update_select("demo_select", choices=new_choices, selected=new_choices[0])
    elif choice_type == "grouped":
        ui.update_select("demo_select", choices=states, selected="CA")
    else:  # empty
        ui.update_select("demo_select", choices=[], selected=None)


@reactive.effect
@reactive.event(input.update_selected)
def _():
    choice_type = input.choice_type()

    if choice_type == "simple":
        ui.update_select("demo_select", selected=["Option 2", "Option 4"])
    elif choice_type == "grouped":
        ui.update_select("demo_select", selected=["CA", "NY"])
    else:
        ui.update_select("demo_select", selected=None)


@reactive.effect
@reactive.event(input.clear_all)
def _():
    ui.update_select("demo_select", choices=[], selected=None)


@reactive.effect
@reactive.event(input.reset)
def _():
    ui.update_select(
        "demo_select", label="Choose items:", choices=fruits, selected="Apple"
    )
