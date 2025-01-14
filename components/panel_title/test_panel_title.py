# Example of how you could modify the cards to make them testable
with ui.card(id="card1"):
    ui.panel_title("Main Page Title", window_title="Browser Window Title")
    "Some content for this card"

with ui.card(id="card2"):
    ui.panel_title(...)
    "More content for this card"
