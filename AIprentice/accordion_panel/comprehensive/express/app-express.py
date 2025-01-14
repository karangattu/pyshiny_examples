from shiny import reactive
from shiny.express import input, ui, render

ui.page_opts(title="Accordion Panel Demo", fillable=True)

# Create a sample dataset for demonstration
data = {
    "Section A": "This is the content for Section A. It demonstrates basic accordion panel usage.",
    "Section B": "This is the content for Section B with some numbers: 123, 456, 789",
    "Section C": "This is the content for Section C with special characters: !@#$%",
}

# Add Font Awesome CSS
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">'
    )
)

# First Column: Basic Accordion
with ui.layout_column_wrap(width="400px"):
    with ui.card():
        ui.card_header("Basic Accordion with Icons")
        with ui.accordion(id="acc1"):
            with ui.accordion_panel("Basic Panel with Icon", value="panel1"):
                ui.tags.i(class_="fa-solid fa-star", style="margin-right: 10px;")
                "This panel demonstrates using an icon and a custom value."

            with ui.accordion_panel(
                ui.HTML("<span style='color: blue;'>HTML Title</span>"), value="panel2"
            ):
                "This panel demonstrates using HTML in the title."

# Second Column: Dynamic Accordion
with ui.layout_column_wrap(width="400px"):
    with ui.card():
        ui.card_header("Dynamic Content Accordion")
        with ui.accordion(id="acc2"):
            for section, content in data.items():
                with ui.accordion_panel(section, value=f"section_{section}"):
                    ui.tags.i(class_="fa-solid fa-book", style="margin-right: 10px;")
                    ui.markdown(content)

# Third Section: Interactive Accordion
with ui.card():
    ui.card_header("Interactive Accordion")
    with ui.accordion(id="acc3"):
        with ui.accordion_panel("Interactive Panel", value="interactive"):
            ui.tags.i(class_="fa-solid fa-gear", style="margin-right: 10px;")
            ui.input_text("panel_text", "Enter text:", "Sample text")
            ui.input_action_button("update_btn", "Update Panel", class_="mt-2")

        @render.ui
        @reactive.event(input.update_btn)
        def dynamic_panel():
            return ui.accordion_panel(
                f"Dynamic Panel - {input.panel_text()}", value="dynamic"
            )


# Display selected panels
ui.h3("Selected Panels:", class_="mt-4")


@render.text
def selected_panels():
    return (
        f"Accordion 1: {input.acc1() or 'None'}\n"
        f"Accordion 2: {input.acc2() or 'None'}\n"
        f"Accordion 3: {input.acc3() or 'None'}"
    )
