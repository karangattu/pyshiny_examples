from shiny import reactive
from shiny.express import input, ui, render  # Added render import
import random

# Add Font Awesome CSS for icons
ui.page_opts(title="Update Tooltip Demonstration", fillable=True)

ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">'
    )
)

# Synthetic data for demonstration
quotes = [
    "Creativity is intelligence having fun.",
    "Success is not final, failure is not fatal.",
    "Believe you can and you're halfway there.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Innovation distinguishes between a leader and a follower.",
]

# Action buttons to demonstrate different tooltip update scenarios
ui.input_action_button("btn_show", "Show Tooltip", class_="btn-primary me-2")
ui.input_action_button("btn_hide", "Hide Tooltip", class_="btn-secondary me-2")
ui.input_action_button("btn_update", "Update Tooltip Content", class_="btn-info me-2")
ui.input_action_button("btn_icon", "Change Tooltip Icon", class_="btn-warning")

# Icons to demonstrate icon changes
icons = [
    "fa-solid fa-lightbulb",
    "fa-solid fa-star",
    "fa-solid fa-rocket",
    "fa-solid fa-heart",
    "fa-solid fa-globe",
]

# Tooltip with an initial state
with ui.tooltip(id="demo_tooltip", placement="right"):
    ui.tags.span(
        ui.tags.i(class_="fa-solid fa-info-circle", style="font-size: 2rem;"),
        " Hover for info",
    )
    "Initial tooltip content"


# Effects to demonstrate different tooltip update scenarios
@reactive.effect
@reactive.event(input.btn_show)
def _():
    ui.update_tooltip("demo_tooltip", show=True)


@reactive.effect
@reactive.event(input.btn_hide)
def _():
    ui.update_tooltip("demo_tooltip", show=False)


@reactive.effect
@reactive.event(input.btn_update)
def _():
    # Randomly select a new quote
    new_quote = random.choice(quotes)

    # Update tooltip with new content and show it
    ui.update_tooltip("demo_tooltip", new_quote, show=True)


current_icon_index = reactive.value(0)


@reactive.effect
@reactive.event(input.btn_icon)
def _():
    # Cycle through icons
    current_index = current_icon_index.get()
    next_index = (current_index + 1) % len(icons)
    current_icon_index.set(next_index)

    # Create a new tooltip content with the new icon
    new_content = [
        ui.tags.i(class_=icons[next_index], style="font-size: 2rem;"),
        " Tooltip with new icon",
    ]

    # Update tooltip with new content and icon
    ui.update_tooltip("demo_tooltip", new_content, show=True)


# Optional: Display current tooltip state
@reactive.calc
def tooltip_state():
    # This is a placeholder to show how you might track tooltip state
    return "Tooltip is interactive. Use buttons to modify its behavior."


# Render the tooltip state
@render.text
def show_tooltip_state():
    return tooltip_state()
