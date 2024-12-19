from shiny import reactive
from shiny.express import input, render, ui

# Page options and styling
ui.page_opts(title="Action Link Demo", fillable=True)

with ui.layout_column_wrap():
    with ui.card():
        ui.card_header("Basic Action Link")
        ui.input_action_link(
            id="basic_link",
            label="Basic Link",
        )

        @render.text
        def basic_result():
            return f"Basic link clicked {input.basic_link()} times"

    with ui.card():
        ui.card_header("Action Link with Icon")
        ui.input_action_link(
            id="icon_link",
            label="Link with Icon",
            icon=ui.tags.i(class_="fa-solid fa-star", style="color: gold;"),
        )

        @render.text
        def icon_result():
            return f"Icon link clicked {input.icon_link()} times"

    with ui.card():
        ui.card_header("Action Link with Custom Style")
        ui.input_action_link(
            id="styled_link",
            label="Styled Link",
            class_="text-danger",
            style="text-decoration: underline; font-weight: bold;",
        )

        @render.text
        def styled_result():
            return f"Styled link clicked {input.styled_link()} times"

    with ui.card():
        ui.card_header("Action Link with HTML")
        ui.input_action_link(
            id="html_link",
            label=ui.HTML("<span style='color: purple;'>HTML Label</span>"),
        )

        @render.text
        def html_result():
            return f"HTML link clicked {input.html_link()} times"


# Add Font Awesome for icons
ui.head_content(
    ui.tags.link(
        rel="stylesheet",
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css",
    )
)

# Counter for total clicks
total_clicks = reactive.Value(0)


@reactive.effect
def count_clicks():
    total = sum(
        [
            input.basic_link() or 0,
            input.icon_link() or 0,
            input.styled_link() or 0,
            input.html_link() or 0,
        ]
    )
    total_clicks.set(total)


# Display total clicks
with ui.card():
    ui.card_header("Total Clicks")

    @render.text
    def total_result():
        return f"Total clicks across all links: {total_clicks.get()}"
