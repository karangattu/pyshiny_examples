from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Accordion Demo", fillable=True)

# Sample data for demonstration
data = {
    "Section A": "This is content for section A. It demonstrates a basic accordion panel.",
    "Section B": "This is content for section B with some numbers: 123, 456, 789",
    "Section C": "This is content for section C showing some text formatting.",
    "Section D": "This demonstrates a panel with custom styling.",
}

# Add Font Awesome for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">'
    )
)

# Create an accordion with all possible parameters
with ui.accordion(
    id="main_accordion",  # Unique identifier for the accordion
    open=["Section A"],  # Initially open panels
    multiple=True,  # Allow multiple panels to be open
):
    # Panel A - Basic panel
    with ui.accordion_panel(
        "Section A", value="section_a", icon=ui.tags.i(class_="fa-solid fa-house")
    ):
        ui.markdown(data["Section A"])
        ui.input_numeric("num_a", "Enter a number", value=10)

        @render.text
        def show_num_a():
            return f"You entered: {input.num_a()}"

    # Panel B - Panel with data display
    with ui.accordion_panel(
        "Section B",
        value="section_b",
        icon=ui.tags.i(class_="fa-solid fa-chart-simple"),
    ):
        ui.markdown(data["Section B"])
        ui.input_slider("slider_b", "Select a value", min=0, max=100, value=50)

        @render.text
        def show_slider_b():
            return f"Selected value: {input.slider_b()}"

    # Panel C - Panel with text input
    with ui.accordion_panel(
        "Section C", value="section_c", icon=ui.tags.i(class_="fa-solid fa-pen")
    ):
        ui.markdown(data["Section C"])
        ui.input_text("text_c", "Enter some text", "Sample text")

        @render.text
        def show_text_c():
            return f"You typed: {input.text_c()}"

    # Panel D - Panel with custom styling
    with ui.accordion_panel(
        "Section D", value="section_d", icon=ui.tags.i(class_="fa-solid fa-gear")
    ):
        ui.markdown(data["Section D"])
        ui.input_checkbox("check_d", "Enable feature", value=False)

        @render.text
        def show_check_d():
            return f"Feature is: {'enabled' if input.check_d() else 'disabled'}"


# Controls for accordion manipulation
with ui.card(id="control_card"):
    ui.card_header("Accordion Controls")

    with ui.layout_column_wrap(width=1 / 2):
        # Button to open all sections
        ui.input_action_button("open_all", "Open All Sections", class_="btn-primary")

        # Button to close all sections
        ui.input_action_button(
            "close_all", "Close All Sections", class_="btn-secondary"
        )


# Reactive effects for accordion control
@reactive.effect
@reactive.event(input.open_all)
def _():
    ui.update_accordion("main_accordion", show=True)


@reactive.effect
@reactive.event(input.close_all)
def _():
    ui.update_accordion("main_accordion", show=False)


# Display current accordion state
@render.text
def show_accordion_state():
    return f"Currently open sections: {input.main_accordion()}"
