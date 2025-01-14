from shiny import reactive
from shiny.express import input, render, ui

ui.page_opts(title="Accordion Demo", fillable=True)

# Add Font Awesome CSS for icons
ui.head_content(
    ui.HTML('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">')
)

with ui.layout_column_wrap(width=1/2):
    # Create buttons panel
    with ui.card():
        ui.card_header("Controls")
        ui.input_action_button("update_all", "Update All Sections", class_="m-1")
        ui.input_action_button("show_ac", "Show only A & C", class_="m-1")
        ui.input_action_button("show_b", "Show only B", class_="m-1")
        ui.input_action_button("show_none", "Collapse All", class_="m-1")
        ui.input_action_button("show_all", "Expand All", class_="m-1")

    # Create accordion panel
    with ui.card():
        ui.card_header("Accordion Demo")
        with ui.accordion(id="acc", multiple=True):
            with ui.accordion_panel("Section A", value="sec_a"):
                "Original content for Section A"
            
            with ui.accordion_panel("Section B", value="sec_b"):
                "Original content for Section B"
            
            with ui.accordion_panel("Section C", value="sec_c"):
                "Original content for Section C"

# Effect to demonstrate updating content, title, and icon
@reactive.effect
@reactive.event(input.update_all)
def _():
    # Update section A with new content, title and icon
    ui.update_accordion_panel(
        id="acc",
        target="sec_a",
        "Updated content for Section A",
        title="New Section A Title",
        icon=ui.tags.i(class_="fa-solid fa-star")
    )
    
    # Update section B with just new content
    ui.update_accordion_panel(
        id="acc",
        target="sec_b",
        "Updated content for Section B"
    )
    
    # Update section C with new content and value
    ui.update_accordion_panel(
        id="acc",
        target="sec_c", 
        "Updated content for Section C",
        value="sec_c_new"
    )

# Effect to show only sections A and C
@reactive.effect
@reactive.event(input.show_ac)
def _():
    ui.update_accordion("acc", show=["sec_a", "sec_c"])

# Effect to show only section B
@reactive.effect
@reactive.event(input.show_b)
def _():
    ui.update_accordion("acc", show="sec_b")

# Effect to collapse all sections
@reactive.effect
@reactive.event(input.show_none)
def _():
    ui.update_accordion("acc", show=False)

# Effect to expand all sections
@reactive.effect
@reactive.event(input.show_all)
def _():
    ui.update_accordion("acc", show=True)

# Add output to show current accordion state
@render.text
def acc_state():
    return f"Current accordion state: {input.acc()}"