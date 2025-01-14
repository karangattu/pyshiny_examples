from shiny import render
from shiny.express import input, ui
from pathlib import Path

# Create a minimal page title
ui.page_opts(title="Include JS Demo")

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

# Include the JavaScript file
ui.include_js(js_file)


# Simple text to show the page loaded
@render.text
def txt():
    return "The JavaScript should have executed and shown an alert."
