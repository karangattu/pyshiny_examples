from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Include JS Demo", fillable=True)

# Custom JavaScript code as a string
custom_js = """
function showAlert() {
    alert('Custom JavaScript Alert!');
}

function updateCounter() {
    const counterElement = document.getElementById('counter');
    if (counterElement) {
        const currentValue = parseInt(counterElement.textContent) || 0;
        counterElement.textContent = currentValue + 1;
    }
}

function changeBackgroundColor() {
    document.body.style.backgroundColor = 
        document.body.style.backgroundColor === 'lightblue' ? 'white' : 'lightblue';
}
"""

# Include JavaScript using 'inline' method
ui.include_js(custom_js, method="inline")

# Include JavaScript using 'link' method with additional attributes
ui.include_js(
    "https://code.jquery.com/jquery-3.6.0.min.js",
    method="link",
    async_=True,
    defer=True,
    crossorigin="anonymous",
)

with ui.layout_columns(width=1 / 2):
    with ui.card():
        ui.card_header("Inline JavaScript Demo")
        ui.input_action_button(
            "show_alert", "Show Alert", class_="btn-primary", onclick="showAlert()"
        )

    with ui.card():
        ui.card_header("Counter Demo")
        ui.tags.div("0", id="counter")  # Corrected syntax
        ui.input_action_button(
            "increment",
            "Increment Counter",
            class_="btn-success",
            onclick="updateCounter()",
        )

    with ui.card():
        ui.card_header("Background Color Toggle")
        ui.input_action_button(
            "toggle_bg",
            "Toggle Background",
            class_="btn-info",
            onclick="changeBackgroundColor()",
        )

    with ui.card():
        ui.card_header("jQuery Demo")

        @render.ui
        def jquery_status():
            return ui.tags.p(
                "jQuery is loaded and ready!",
                style="display: none;",
                id="jquery-status",
            )

        ui.tags.script(
            """
            $(document).ready(function() {
                $('#jquery-status').fadeIn('slow');
            });
        """
        )
