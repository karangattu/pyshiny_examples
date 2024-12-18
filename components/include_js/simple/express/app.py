from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Include JS Demo")

# Include custom JavaScript code directly
js_code = """
function showAlert() {
    alert('Hello from custom JavaScript!');
}

function updateCounter() {
    const counterElement = document.getElementById('click-counter');
    if (counterElement) {
        const currentCount = parseInt(counterElement.textContent) || 0;
        counterElement.textContent = currentCount + 1;
    }
}
"""

# Include the JavaScript code
ui.tags.script(js_code)

# Create a card with buttons that use the JavaScript functions
with ui.card():
    ui.card_header("JavaScript Demo")

    # Button that triggers JavaScript alert
    ui.input_action_button(
        "show_alert", "Show Alert", onclick="showAlert()", class_="btn-primary me-2"
    )

    # Button that updates counter using JavaScript
    ui.input_action_button(
        "increment",
        "Increment Counter",
        onclick="updateCounter()",
        class_="btn-success",
    )

    # Display area for counter
    ui.div(
        ui.p(
            "Click count: ",
            ui.span("0", id="click-counter", style="font-weight: bold;"),
        ),
        class_="mt-3",
    )

# Display current time using JavaScript
with ui.card(class_="mt-3"):
    ui.card_header("Current Time")

    @render.ui
    def show_time():
        return ui.tags.div(id="current-time", class_="p-3", _add_ws=True)


# JavaScript to update time every second
time_update_js = """
function updateTime() {
    const timeElement = document.getElementById('current-time');
    if (timeElement) {
        const now = new Date();
        timeElement.textContent = now.toLocaleTimeString();
    }
}

// Update time immediately and then every second
updateTime();
setInterval(updateTime, 1000);
"""

ui.tags.script(time_update_js)
