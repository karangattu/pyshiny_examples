from shiny.express import ui
from htmltools import TagList, div

# Create a simple app demonstrating TagList functionality
ui.page_opts(title="TagList Demonstration")

# Create a TagList with mixed content types
my_taglist = ui.TagList(
    ui.h2("TagList Example"),
    ui.p("This is a paragraph inside a TagList."),
    ui.tags.div(id="custom-div", class_="bg-light p-3", "A div with custom attributes"),
    ui.tags.span("A span element"),
    ui.markdown("**Markdown** is also supported in TagList!")
)

# Display the TagList
my_taglist

# Additional demonstration of TagList methods
with ui.card():
    ui.card_header("TagList Methods Demonstration")
    
    # Demonstrate appending to a TagList
    demo_taglist = ui.TagList(ui.p("Initial content"))
    demo_taglist.append(ui.p("Appended content"))
    
    # Render the modified TagList
    demo_taglist

    # Demonstrate extending a TagList
    extend_taglist = ui.TagList(ui.h3("Original content"))
    extend_taglist.extend([
        ui.p("First extended item"),
        ui.p("Second extended item")
    ])
    
    # Render the extended TagList
    extend_taglist