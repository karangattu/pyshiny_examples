from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Panel Title Demo", fillable=True)

# Basic panel title with just text
ui.panel_title("Basic Title")

# Panel title with HTML tag
ui.panel_title(ui.tags.h1("Title with HTML tag", style="color: blue;"))

with ui.layout_column_wrap():
    with ui.card():
        # Panel title with both title and window_title
        ui.panel_title("Main Page Title", window_title="Browser Window Title")
        "Some content for this card"

    with ui.card():
        # Panel title with TagList for multiple elements
        ui.panel_title(
            ui.TagList(
                ui.tags.h1("Main Title", style="color: purple;"),
                ui.tags.h3("Subtitle", style="color: gray;"),
            ),
            window_title="Complex Title Example",
        )
        "More content for this card"
