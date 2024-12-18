from pathlib import Path
from shiny import reactive
from shiny.express import input, ui, render

# Create a synthetic JavaScript content
js_content = """
// Sample JavaScript function
function showAlert() {
    alert('Hello from included JavaScript!');
}

function changeBackgroundColor() {
    document.body.style.backgroundColor = 
        '#' + Math.floor(Math.random()*16777215).toString(16);
}

console.log('JavaScript file loaded successfully!');
"""

ui.page_opts(title="Include JS Demonstration")

# Create a temporary file to demonstrate file inclusion
temp_js_file = Path(__file__).parent / "temp_demo.js"
temp_js_file.write_text(js_content)

with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_radio_buttons(
            "method", "Include JS Method", ["link", "link_files", "inline"]
        )

        ui.input_checkbox("use_kwargs", "Use Additional Kwargs")

        # Conditional input for additional attributes
        with ui.panel_conditional("input.use_kwargs"):
            ui.input_text("js_id", "Script ID", placeholder="Optional script ID")
            ui.input_text(
                "js_class", "Script Class", placeholder="Optional script class"
            )

    # Main panel to demonstrate JS inclusion and interaction
    with ui.card():
        ui.card_header("JavaScript Inclusion Demonstration")

        # Button to trigger JavaScript functions
        ui.input_action_button("show_alert", "Show Alert")
        ui.input_action_button("change_color", "Change Background Color")

        # Area to show JS inclusion details
        @render.text
        def js_method_details():
            method = input.method()
            details = f"Method: {method}\n"

            # Prepare kwargs if checkbox is checked
            kwargs = {}
            if input.use_kwargs():
                if input.js_id():
                    kwargs["id"] = input.js_id()
                if input.js_class():
                    kwargs["class_"] = input.js_class()

            # Demonstrate different inclusion methods
            if method == "link":
                ui.include_js(temp_js_file, method="link", **kwargs)
                details += "Linked external JavaScript file"
            elif method == "link_files":
                ui.include_js(temp_js_file, method="link_files", **kwargs)
                details += "Linked files with potential additional imports"
            else:  # inline
                ui.include_js(js_content, method="inline", **kwargs)
                details += "Inlined JavaScript content directly"

            return details


# Reactive effects to trigger JavaScript functions
@reactive.effect
@reactive.event(input.show_alert)
def _():
    # This would typically trigger the showAlert() function in the included JS
    pass


@reactive.effect
@reactive.event(input.change_color)
def _():
    # This would typically trigger the changeBackgroundColor() function in the included JS
    pass
