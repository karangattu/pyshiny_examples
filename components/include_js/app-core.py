from shiny import App, render, ui
from pathlib import Path

# First, let's create a directory and file for our JavaScript
js_dir = Path(__file__).parent / "js"
js_dir.mkdir(exist_ok=True)

# Create the JavaScript file
js_file = js_dir / "app.js"
with open(js_file, "w") as f:
    f.write(
        """
alert("If you're seeing this, the javascript file was included successfully.");
"""
    )

app_ui = ui.page_fluid(
    # Include the JavaScript file
    ui.tags.head(ui.tags.script(src=js_file.name)),
    # Simple text to show the page loaded
    ui.output_text_verbatim("txt"),
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        return "The JavaScript should have executed and shown an alert."


app = App(app_ui, server)
