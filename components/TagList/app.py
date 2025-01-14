from datetime import datetime
from shiny import reactive
from shiny.express import input, ui, render

ui.page_opts(title="TagList Demo", fillable=True)


# Basic TagList with string and div
@render.ui
def basic_taglist():
    return ui.TagList(
        "Hello World", ui.div("This is a div inside TagList", class_="custom-div")
    )


# TagList with HTML elements and attributes
@render.ui
def html_taglist():
    return ui.TagList(
        ui.h3("Header in TagList"),
        ui.p("Paragraph 1", style="color: blue;"),
        ui.p("Paragraph 2", style="color: red;"),
    )


# TagList with dynamic content
@render.ui
def dynamic_taglist():
    reactive.invalidate_later(1)
    return ui.TagList(
        ui.h4("Dynamic Content"),
        ui.p(f"Current time: {datetime.now().strftime('%H:%M:%S')}"),
        ui.div("This content updates every second"),
    )


# Display the TagLists
with ui.layout_column_wrap(width=1 / 2):
    with ui.card(full_screen=True, height="200px"):
        ui.card_header("Basic TagList")
        basic_taglist()

    with ui.card(full_screen=True, height="200px"):
        ui.card_header("TagList with HTML Elements")
        html_taglist()

    with ui.card(full_screen=True, height="200px"):
        ui.card_header("Dynamic TagList")
        dynamic_taglist()

    with ui.card(full_screen=True, height="200px"):
        ui.card_header("TagList Methods Demo")

        @render.ui
        def taglist_methods():
            # Create a new TagList each time
            demo_taglist = ui.TagList("Initial content")

            # Append method
            demo_taglist.append(ui.p("Appended content"))

            # Extend method
            demo_taglist.extend(
                [ui.p("Extended content 1"), ui.p("Extended content 2")]
            )

            # Get dependencies
            deps = demo_taglist.get_dependencies()

            return ui.TagList(demo_taglist, ui.p(f"Dependencies count: {len(deps)}"))

        taglist_methods()
