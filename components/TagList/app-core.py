from datetime import datetime
from shiny import App, reactive, render, ui

# Define the UI
app_ui = ui.page_fillable(
    ui.panel_title("TagList Demo"),
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Basic TagList"),
            ui.output_ui("basic_taglist"),
            full_screen=True,
            height="200px",
        ),
        ui.card(
            ui.card_header("TagList with HTML Elements"),
            ui.output_ui("html_taglist"),
            full_screen=True,
            height="200px",
        ),
        ui.card(
            ui.card_header("Dynamic TagList"),
            ui.output_ui("dynamic_taglist"),
            full_screen=True,
            height="200px",
        ),
        ui.card(
            ui.card_header("TagList Methods Demo"),
            ui.output_ui("taglist_methods"),
            full_screen=True,
            height="200px",
        ),
        width=1 / 2,
    ),
)


# Define the server
def server(input, output, session):
    @output
    @render.ui
    def basic_taglist():
        return ui.TagList(
            "Hello World", ui.div("This is a div inside TagList", class_="custom-div")
        )

    @output
    @render.ui
    def html_taglist():
        return ui.TagList(
            ui.h3("Header in TagList"),
            ui.p("Paragraph 1", style="color: blue;"),
            ui.p("Paragraph 2", style="color: red;"),
        )

    @output
    @render.ui
    def dynamic_taglist():
        reactive.invalidate_later(1)
        return ui.TagList(
            ui.h4("Dynamic Content"),
            ui.p(f"Current time: {datetime.now().strftime('%H:%M:%S')}"),
            ui.div("This content updates every second"),
        )

    @output
    @render.ui
    def taglist_methods():
        # Create a new TagList each time
        demo_taglist = ui.TagList("Initial content")

        # Append method
        demo_taglist.append(ui.p("Appended content"))

        # Extend method
        demo_taglist.extend([ui.p("Extended content 1"), ui.p("Extended content 2")])

        # Get dependencies
        deps = demo_taglist.get_dependencies()

        return ui.TagList(demo_taglist, ui.p(f"Dependencies count: {len(deps)}"))


# Create and return the app
app = App(app_ui, server)
