from shiny import App, ui

app_ui = ui.page_fillable(
    # Basic markdown content
    ui.markdown(
        """
        # Markdown Demo
        
        This demonstrates various markdown features:
        
        ## Text Formatting
        **Bold text** and *italic text* and `inline code`
        
        ## Lists
        * Unordered list item 1
        * Unordered list item 2
          * Nested item
        
        1. Ordered list item 1
        2. Ordered list item 2
        
        ## Code Blocks
        """
    )
)


def server(input, output, session):
    pass


app = App(app_ui, server)
