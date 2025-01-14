from shiny import reactive
from shiny.express import input, ui, render

# Sample data - using HTML for some choices to demonstrate rich formatting
choices = {
    "red": ui.span("Red", style="color: #FF0000;"),
    "blue": ui.span("Blue", style="color: #0000FF;"),
    "green": ui.span("Green", style="color: #00AA00;"),
    "purple": ui.span("Purple", style="color: #800080;"),
}

# Set page options
ui.page_opts(title="Checkbox Group Demo", fillable=True)

# Create layout with columns
with ui.layout_column_wrap(width=1 / 3):
    # Basic checkbox group with default parameters
    with ui.card(full_screen=True, id="card1"):
        ui.card_header("Basic Checkbox Group")
        ui.input_checkbox_group(
            id="basic_group",
            label="Choose colors:",
            choices=choices,
            selected=["red", "blue"],
        )

        @render.text
        def basic_output():
            return f"You selected: {input.basic_group()}"

    # Inline checkbox group
    with ui.card(full_screen=True, id="card2"):
        ui.card_header("Inline Checkbox Group")
        ui.input_checkbox_group(
            id="inline_group",
            label="Choose colors (inline):",
            choices=choices,
            selected=["green"],
            inline=True,
        )

        @render.text
        def inline_output():
            return f"You selected: {input.inline_group()}"

    # Custom width checkbox group
    with ui.card(full_screen=True, id="card3"):
        ui.card_header("Custom Width Checkbox Group")
        ui.input_checkbox_group(
            id="width_group",
            label="Choose colors (wider):",
            choices=choices,
            width="400px",
        )

        @render.text
        def width_output():
            return f"You selected: {input.width_group()}"


# Add a summary card
with ui.card(id="summary_card"):
    ui.card_header("Summary of All Selections")

    @render.text
    def total_selections():
        basic = input.basic_group() if input.basic_group() else []
        inline = input.inline_group() if input.inline_group() else []
        width = input.width_group() if input.width_group() else []

        total = len(basic) + len(inline) + len(width)
        return f"Total number of selections across all groups: {total}"

    @render.ui
    def selection_details():
        selections = {
            "Basic Group": input.basic_group() if input.basic_group() else [],
            "Inline Group": input.inline_group() if input.inline_group() else [],
            "Width Group": input.width_group() if input.width_group() else [],
        }

        # Create a div containing paragraphs for each group's selections
        return ui.tags.div(
            [
                ui.tags.p(f"{group}: {', '.join(selected) if selected else 'None'}")
                for group, selected in selections.items()
            ],
            class_="mt-3",
        )
