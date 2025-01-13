from shiny import reactive
from shiny.express import input, ui, render

# Page setup
ui.page_opts(title="Accordion Demo", fillable=True)

# Create a sidebar with controls
with ui.sidebar():
    ui.h4("Accordion Controls")
    ui.input_radio_buttons(
        "show_sections",
        "Show Sections",
        choices={
            "all": "Show All",
            "odd": "Show Odd Sections",
            "even": "Show Even Sections",
            "none": "Hide All"
        },
        selected="all"
    )

# Create main accordion
with ui.accordion(id="acc", open=True, multiple=True):
    # Section 1
    with ui.accordion_panel("Section 1", value="sec1"):
        ui.markdown("""
        This is section 1 content. 
        * Bullet point 1
        * Bullet point 2
        """)

    # Section 2
    with ui.accordion_panel("Section 2", value="sec2"):
        ui.markdown("""
        This is section 2 content.
        1. Numbered item 1
        2. Numbered item 2
        """)

    # Section 3
    with ui.accordion_panel("Section 3", value="sec3"):
        ui.markdown("""
        This is section 3 content.
        > This is a blockquote
        """)

    # Section 4
    with ui.accordion_panel("Section 4", value="sec4"):
        ui.markdown("""
        This is section 4 content.