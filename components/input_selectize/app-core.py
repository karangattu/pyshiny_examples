from shiny import App, reactive, render, ui

# Sample data for states
states = {
    "East Coast": {"NY": "New York", "NJ": "New Jersey", "CT": "Connecticut"},
    "West Coast": {"WA": "Washington", "OR": "Oregon", "CA": "California"},
    "Midwest": {"MN": "Minnesota", "WI": "Wisconsin", "IA": "Iowa"},
}

app_ui = ui.page_fluid(
    # Create layout with sidebar and main panel
    ui.input_selectize(
        id="state",
        label="Choose state(s):",
        choices=states,
        selected=["NY", "CA"],
        multiple=True,
        options={
            "placeholder": "Select states...",
            "plugins": ["clear_button"],
            "render": ui.js_eval(
                '{option: function(item, escape) {return "<div><strong>" + escape(item.label) + "</strong></div>";}}'
            ),
        },
    ),
    # Main panel
    ui.card(
        ui.card_header("Selection Results"),
        ui.output_text("selection"),
    ),
)


def server(input, output, session):
    @output
    @render.text
    def selection():
        if not input.state():
            return "No states selected"
        return f"You selected: {', '.join(input.state())}"


app = App(app_ui, server)
