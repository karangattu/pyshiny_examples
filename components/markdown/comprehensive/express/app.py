from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Markdown Examples", fillable=True)

# Create a sidebar with markdown customization options
with ui.sidebar():
    ui.input_text("text", "Enter custom markdown text", "**Hello** _world_!")
    ui.input_text(
        "custom_func", "Custom render function (Python code)", "lambda x: x.upper()"
    )

# Main content area
with ui.layout_columns(width=1 / 2):
    # Basic markdown example
    with ui.card():
        ui.card_header("Basic Markdown")
        ui.markdown(
            """
        # Basic Markdown Example
        
        This is **bold** text and _italic_ text.
        
        * List item 1
        * List item 2
        
        1. Numbered item 1
        2. Numbered item 2
        
        [Link to Shiny](https://shiny.posit.co/py/)
        """
        )

    # Dynamic markdown example
    with ui.card():
        ui.card_header("Dynamic Markdown")

        @render.ui
        def dynamic_markdown():
            return ui.markdown(input.text())

    # Custom rendered markdown
    with ui.card():
        ui.card_header("Custom Rendered Markdown")

        @render.ui
        def custom_markdown():
            try:
                # Safely evaluate the custom function
                custom_func = eval(input.custom_func())
                text = custom_func(input.text())
                return ui.markdown(text)
            except Exception as e:
                return ui.markdown(f"Error: {str(e)}")
