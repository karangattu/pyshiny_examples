from shiny import reactive
from shiny.express import input, ui, render
from pathlib import Path
import os

# Create a directory to store the JavaScript file if it doesn't exist
js_dir = Path(__file__).parent / "js"
js_dir.mkdir(exist_ok=True)

# Path for the JavaScript file
js_path = js_dir / "color_changer.js"

# Write the JavaScript content to a file
js_content = """
// Custom JavaScript function to modify an element
function changeTextColor() {
    var element = document.getElementById('dynamic_text');
    element.style.color = getRandomColor();
}

// Function to generate a random color
function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
"""

# Write the JavaScript to a file
with open(js_path, "w") as f:
    f.write(js_content)

# Page title and description
ui.page_opts(title="Include JS Demo")

# Include the JavaScript file
ui.include_js(js_path)

# Create a card with interactive elements
with ui.card():
    ui.markdown("## JavaScript Interaction Demo")

    # Button to trigger JavaScript function
    ui.input_action_button(
        "color_btn", "Change Text Color", onclick="changeTextColor()"
    )

    # Text element that will be modified by JavaScript
    ui.tags.p("This text can change color dynamically!", id="dynamic_text")

    # Display click count using Shiny's reactive system
    @render.text
    def click_count():
        return f"Button clicked {input.color_btn()} times"
