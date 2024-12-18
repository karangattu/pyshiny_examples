from shiny import reactive
from shiny.express import input, render, ui

# Page options and title
ui.page_opts(title="Markdown Demo", fillable=True)

# Add some markdown content using ui.markdown()
ui.markdown(
    """
    # Welcome to Markdown Demo! 
    
    This is a demonstration of **Markdown** capabilities in Shiny for Python.
    
    ## Features shown:
    * Headers (like above)
    * **Bold text**
    * *Italic text*
    * Lists (like this one)
    * [Links](https://shiny.posit.co/py/)
    * Code blocks
    
    ### Here's a sample code block:
    ```python
    print("Hello, world!")    
    ```
        """
)
