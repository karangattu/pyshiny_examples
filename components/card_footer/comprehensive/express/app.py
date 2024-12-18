from shiny import reactive
from shiny.express import input, ui, render

# Page options for better layout
ui.page_opts(title="Card Footer Demo", fillable=True)

# Create a card with various footer configurations
with ui.card(full_screen=True):
    ui.card_header("Card with Different Footer Styles")

    @render.text
    def card_content():
        return "This is the main content of the card. The footer below demonstrates different styling options."

    # Basic footer with just text
    with ui.card_footer("Basic Footer"):
        "This is a simple footer with text"

    # Footer with class attributes
    with ui.card_footer(class_="bg-primary text-white p-3"):
        "Footer with custom background and text color"

    # Footer with HTML content using tags
    with ui.card_footer(
        ui.tags.div(
            ui.tags.span("Created by: ", class_="text-muted"),
            ui.tags.strong("John Doe"),
            style="display: flex; justify-content: space-between;",
        )
    ):
        ui.tags.div(ui.tags.small("Last updated: 2024-01-20"), class_="text-muted")

    # Footer with interactive elements
    with ui.card_footer(
        style="display: flex; justify-content: space-between; align-items: center;"
    ):
        ui.input_action_button("like_btn", "👍 Like", class_="btn-sm")
        ui.input_action_button("share_btn", "📤 Share", class_="btn-sm")

        @render.text
        def interaction_count():
            return f"Likes: {input.like_btn()} | Shares: {input.share_btn()}"

    # Footer with custom styling and data display
    with ui.card_footer(
        style="background-color: #f8f9fa; border-top: 2px solid #dee2e6;"
    ):
        with ui.tags.div(style="display: flex; justify-content: space-around;"):
            with ui.tags.div(class_="text-center"):
                ui.tags.strong("Views")
                ui.tags.div("1,234", class_="text-muted")
            with ui.tags.div(class_="text-center"):
                ui.tags.strong("Comments")
                ui.tags.div("56", class_="text-muted")
            with ui.tags.div(class_="text-center"):
                ui.tags.strong("Rating")
                ui.tags.div("4.5/5", class_="text-muted")

    # Footer with form elements
    with ui.card_footer(class_="p-3"):
        with ui.tags.div(style="display: flex; gap: 10px;"):
            ui.input_text("comment", "Add a comment", width="300px")
            ui.input_action_button("submit_comment", "Submit", class_="btn-primary")

        @render.text
        def comment_status():
            if input.submit_comment():
                return f"Latest comment: {input.comment()}"
            return ""
