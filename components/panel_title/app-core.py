from shiny import App, ui

app_ui = ui.page_fillable(
    # Basic panel title with just text
    ui.panel_title("Basic Title"),
    # Panel title with HTML tag
    ui.panel_title(ui.tags.h1("Title with HTML tag", style="color: blue;")),
    # Layout with columns
    ui.layout_column_wrap(
        ui.card(
            # Panel title with both title and window_title
            ui.panel_title("Main Page Title", window_title="Browser Window Title"),
            "Some content for this card",
        ),
        ui.card(
            # Panel title with TagList for multiple elements
            ui.panel_title(
                ui.TagList(
                    ui.tags.h1("Main Title", style="color: purple;"),
                    ui.tags.h3("Subtitle", style="color: gray;"),
                ),
                window_title="Complex Title Example",
            ),
            "More content for this card",
        ),
    ),
)


def server(input, output, session):
    pass


app = App(app_ui, server)
