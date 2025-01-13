from shiny import reactive
from shiny.express import input, ui, render

# Page options
ui.page_opts(title="Accordion Panel Demo", fillable=True)

# Create some initial buttons to control the accordion
with ui.layout_column_wrap(width=1 / 3):
    ui.input_action_button("remove_a", "Remove Section A", class_="btn-danger")
    ui.input_action_button("remove_b", "Remove Section B", class_="btn-warning")
    ui.input_action_button("remove_c", "Remove Section C", class_="btn-info")

# Create an accordion with multiple sections that can be removed
with ui.accordion(id="acc", multiple=True):
    with ui.accordion_panel("Section A", value="sec_a"):
        "This is section A content. It can be removed using the button above."
        ui.input_text("text_a", "Enter text for section A", "Sample A")

    with ui.accordion_panel("Section B", value="sec_b"):
        "This is section B content. It can be removed using the button above."
        ui.input_slider("slider_b", "Adjust value for section B", 0, 100, 50)

    with ui.accordion_panel("Section C", value="sec_c"):
        "This is section C content. It can be removed using the button above."
        ui.input_numeric("num_c", "Enter number for section C", 42)


# Status display
@render.ui
def status():
    return ui.p(f"Current accordion state: {input.acc()}", class_="mt-3")


# Effect to remove Section A
@reactive.effect
@reactive.event(input.remove_a)
def remove_section_a():
    ui.remove_accordion_panel(
        id="acc",  # The ID of the accordion container
        target="sec_a",  # The value of the panel to remove
    )
    ui.notification_show("Section A has been removed", type="warning")


# Effect to remove Section B
@reactive.effect
@reactive.event(input.remove_b)
def remove_section_b():
    ui.remove_accordion_panel(
        id="acc",  # The ID of the accordion container
        target="sec_b",  # The value of the panel to remove
    )
    ui.notification_show("Section B has been removed", type="warning")


# Effect to remove Section C
@reactive.effect
@reactive.event(input.remove_c)
def remove_section_c():
    ui.remove_accordion_panel(
        id="acc",  # The ID of the accordion container
        target="sec_c",  # The value of the panel to remove
    )
    ui.notification_show("Section C has been removed", type="warning")


# Add a reset button at the bottom
ui.hr()
ui.input_action_button("reset", "Reset Accordion", class_="btn-success")


# Effect to reset the accordion by re-adding all panels
@reactive.effect
@reactive.event(input.reset)
def reset_accordion():
    # Insert each panel back into the accordion
    ui.insert_accordion_panel(
        id="acc",
        panel=ui.accordion_panel(
            title="Section A",
            value="This is section A content. It can be removed using the button above.",
        ),
    )

    ui.insert_accordion_panel(
        id="acc",
        panel=ui.accordion_panel(
            title="Section B",
            value="This is section B content. It can be removed using the button above.",
        ),
    )

    ui.insert_accordion_panel(
        id="acc",
        panel=ui.accordion_panel(
            title="Section C",
            value="This is section C content. It can be removed using the button above.",
        ),
    )

    ui.notification_show("Accordion has been reset!", type="message")
