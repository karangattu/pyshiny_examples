from shiny import reactive
from shiny.express import input, ui

# Create a simple list of motivational quotes
quotes = [
    "Believe you can and you're halfway there.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "The only way to do great work is to love what you do.",
    "Don't watch the clock; do what it does. Keep going.",
    "Strive not to be a success, but rather to be of value.",
]

ui.page_opts(title="Popover Update Demo")

# Create a card with a button that has a popover
with ui.card():
    ui.card_header("Motivational Quote Generator")

    # Create a popover with an initial quote
    with ui.popover(id="quote_popover", placement="right"):
        ui.input_action_button("quote_btn", "Get Motivation", class_="btn-primary")
        quotes[0]  # Initial quote

# Buttons to update the popover
ui.input_action_button("update_quote", "Update Quote", class_="mt-3 btn-success")
ui.input_action_button("close_quote", "Close Popover", class_="mt-3 btn-danger")


# Reactive effect to update the popover quote
@reactive.effect
@reactive.event(input.update_quote)
def _():
    # Cycle through quotes, using the button click count to select
    quote_index = input.update_quote() % len(quotes)
    ui.update_popover("quote_popover", quotes[quote_index])


# Reactive effect to close the popover
@reactive.effect
@reactive.event(input.close_quote)
def _():
    ui.update_popover("quote_popover", show=False)
