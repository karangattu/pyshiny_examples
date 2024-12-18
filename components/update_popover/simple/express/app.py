from shiny import reactive
from shiny.express import input, render, ui

# Page title and options
ui.page_opts(title="Popover Update Demo", fillable=True)

# Add Font Awesome CSS for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
    )
)

# Create a card to hold our content
with ui.card():
    ui.card_header("Popover Update Demo")

    # Create a button with a popover
    with ui.popover(id="info_popover", placement="right"):
        ui.input_action_button(
            "btn_info",
            "Show Statistics",
            class_="mt-3",
        )
        "Click to see current statistics"

    # Add some controls
    ui.input_numeric("value", "Enter a value", value=100)
    ui.input_action_button("update_stats", "Update Statistics", class_="mt-3")

# Create a reactive value to store our statistics
stats = reactive.value({"mean": 100, "std": 15, "min": 70, "max": 130})


@reactive.effect
@reactive.event(input.update_stats)
def _():
    # Update our statistics based on the input value
    new_value = input.value()
    new_stats = {
        "mean": new_value,
        "std": new_value * 0.15,
        "min": new_value * 0.7,
        "max": new_value * 1.3,
    }
    stats.set(new_stats)

    # Update the popover with new content
    content = f"""
    <div>
        <p><i class="fa-solid fa-calculator"></i> Current Statistics:</p>
        <ul>
            <li>Mean: {new_stats['mean']:.1f}</li>
            <li>Std Dev: {new_stats['std']:.1f}</li>
            <li>Range: [{new_stats['min']:.1f}, {new_stats['max']:.1f}]</li>
        </ul>
    </div>
    """

    ui.update_popover("info_popover", ui.HTML(content), show=True)
