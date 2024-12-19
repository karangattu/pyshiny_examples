from shiny import reactive
from shiny.express import input, ui, render

# Create some sample data
sample_data = {
    "title": "Sample Report",
    "sections": ["Introduction", "Methods", "Results", "Discussion"],
    "authors": ["John Doe", "Jane Smith", "Bob Wilson"],
}

# Create a TagList for the header section
header = ui.TagList(
    ui.h1(sample_data["title"]),
    ui.p("Authors: " + ", ".join(sample_data["authors"])),
    ui.hr(),
)

# Display the header TagList
header

# Create an interactive section using TagList
with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_selectize("section", "Select Section", choices=sample_data["sections"])
        ui.input_text("new_content", "Add Content", "")
        ui.input_action_button("add", "Add Content")

    @render.ui
    def dynamic_content():
        # Create a TagList for the main content
        content = ui.TagList(
            ui.h3(f"Selected Section: {input.section()}"),
            ui.p("Current content for this section:"),
            ui.div(
                style="padding: 10px; background-color: #f0f0f0; border-radius: 5px;",
                children=f"This is sample content for the {input.section()} section.",
            ),
        )
        return content

    # Show added content when button is clicked
    @render.ui
    @reactive.event(input.add)
    def added_content():
        if not input.new_content():
            return ui.TagList()

        return ui.TagList(
            ui.div(
                style="margin-top: 20px; padding: 10px; background-color: #e6ffe6; border-radius: 5px;",
                children=[ui.strong("Added Content:"), ui.p(input.new_content())],
            )
        )
