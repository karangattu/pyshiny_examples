from shiny import reactive
from shiny.express import input, ui, render

# Sample data with nested structure for optgroups
states = {
    "East Coast": {"NY": "New York", "NJ": "New Jersey", "CT": "Connecticut"},
    "West Coast": {"WA": "Washington", "OR": "Oregon", "CA": "California"},
    "Midwest": {"MN": "Minnesota", "WI": "Wisconsin", "IA": "Iowa"},
}

# Set page options
ui.page_opts(title="input_select Demo", fillable=True)

with ui.layout_sidebar():
    with ui.sidebar():
        ui.h4("Control Panel")
        ui.input_checkbox("multiple", "Enable multiple selection", value=False)
        ui.input_checkbox("selectize", "Use selectize.js", value=False)
        ui.input_numeric("size", "Size (height in items)", value=5)

    with ui.card():
        ui.card_header("Basic Select")

        # Basic select with all parameters
        @render.ui
        def select_input():
            return ui.input_select(
                id="state",
                label="Choose state(s):",
                choices=states,
                selected="NY" if not input.multiple() else ["NY", "CA"],
                multiple=input.multiple(),
                selectize=input.selectize(),
                size=str(input.size()) if not input.selectize() else None,
                width="100%",
            )

    with ui.card():
        ui.card_header("Selected Value(s)")

        @render.text
        def selected_value():
            return f"You selected: {input.state()}"

    with ui.card():
        ui.card_header("Current Settings")

        @render.ui
        def current_settings():
            settings = {
                "Multiple Selection": str(input.multiple()),
                "Selectize Mode": str(input.selectize()),
                "Size (if not selectize)": str(input.size()),
                "Width": "100%",
            }

            return ui.tags.div(
                ui.tags.pre("\n".join([f"{k}: {v}" for k, v in settings.items()]))
            )

    with ui.card():
        ui.card_header("Documentation")
        ui.markdown(
            """
        ### Parameters Demonstrated:
        
        * **id**: The input identifier ("state")
        * **label**: The label shown above the input
        * **choices**: A dictionary of choices (with nested structure for optgroups)
        * **selected**: The initially selected value(s)
        * **multiple**: Whether multiple selections are allowed
        * **selectize**: Whether to use selectize.js
        * **width**: The width of the input ("100%")
        * **size**: Number of items to show (when not in selectize mode)
        """
        )
