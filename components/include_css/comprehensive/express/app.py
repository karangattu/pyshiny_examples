from pathlib import Path
from shiny import reactive
from shiny.express import input, ui, render
import os

# Page options for title and styling
ui.page_opts(title="CSS Include Demo", fillable=True)

# Create a directory for CSS files if it doesn't exist
css_dir = Path("css")
css_dir.mkdir(exist_ok=True)

# Define CSS content as a string
css_content = """
/* Custom CSS rules */
.custom-card {
    border: 2px solid #447099;
    border-radius: 10px;
    padding: 15px;
    margin: 10px;
    background-color: #f8f9fa;
}

.custom-text {
    color: #447099;
    font-size: 1.2em;
    font-weight: bold;
}

.custom-button {
    background-color: #447099;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}

.custom-button:hover {
    background-color: #2c4a6d;
}

/* Additional styles that might be imported */
.highlight {
    background-color: yellow;
    padding: 5px;
}
"""

# Create CSS file in the css directory
css_file = css_dir / "style.css"
with open(css_file, "w") as f:
    f.write(css_content)

# Include CSS using inline method (most reliable for this example)
ui.include_css(css_file, method="inline")

# Create layout to demonstrate the CSS
with ui.layout_column_wrap(width=1 / 2):

    # Card demonstrating styles
    with ui.card(class_="custom-card"):
        ui.card_header("Style Demo 1")
        ui.p("This card demonstrates custom CSS styling", class_="custom-text")
        ui.input_action_button("btn1", "Click Me!", class_="custom-button")

        @render.text
        def link_clicks():
            return f"Button clicked {input.btn1()} times"

    # Card demonstrating more styles
    with ui.card(class_="custom-card"):
        ui.card_header("Style Demo 2")
        ui.p("Another example of custom styling", class_="custom-text")
        ui.input_action_button("btn2", "Click Me!", class_="custom-button")

        @render.text
        def link_files_clicks():
            return f"Button clicked {input.btn2()} times"

    # Card demonstrating combined styles
    with ui.card(class_="custom-card"):
        ui.card_header("Combined Styles Demo")
        ui.p("This text has multiple styles", class_="custom-text highlight")
        ui.input_action_button("btn3", "Click Me!", class_="custom-button")

        @render.text
        def combined_clicks():
            return f"Button clicked {input.btn3()} times"


# Cleanup function
@reactive.effect
def cleanup():
    import shutil

    if css_dir.exists():
        shutil.rmtree(css_dir)
