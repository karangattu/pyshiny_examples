from pathlib import Path
from shiny import App, ui

# Define the UI
app_ui = ui.page_fluid(
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
    ),
    # Display examples of the CSS styles
    ui.p("This text uses the 'custom-text' class", class_="custom-text"),
    ui.div("This content is in a custom box", class_="custom-box"),
    ui.div("This content has a custom border", class_="custom-border"),
)


# Define the server
def server(input, output, session):
    pass


# Create the Shiny app
app = App(app_ui, server)
