from pathlib import Path
from shiny.express import input, ui, render

# Create a page title
ui.page_opts(title="CSS Include Demo")

# Add CSS styles using ui.head_content
ui.head_content(
    ui.tags.style(
        """
        .custom-text {
            color: blue;
            font-size: 24px;
            font-weight: bold;
        }
        
        .custom-box {
            background-color: #f0f0f0;
            padding: 20px;
            border-radius: 5px;
            margin: 10px 0;
        }
        
        .custom-border {
            border: 3px solid green;
            padding: 10px;
            margin-top: 10px;
        }
        """
    )
)

# Display examples of the CSS styles
ui.p("This text uses the 'custom-text' class", class_="custom-text")

with ui.div(class_="custom-box"):
    "This content is in a custom box"

with ui.div(class_="custom-border"):
    "This content has a custom border"
