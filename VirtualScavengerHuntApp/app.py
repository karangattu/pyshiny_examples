import random

from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Sample data for the scavenger hunt
items = [
    {"name": "Rubber duck", "description": "A classic bath toy"},
    {"name": "Paperclip", "description": "A small metal fastener"},
    {"name": "Sticky note", "description": "A small square of adhesive paper"},
    {"name": "Stapler", "description": "A device for binding papers together"},
    {"name": "Highlighter", "description": "A marker that makes text stand out"},
    {"name": "Pencil sharpener", "description": "A tool for sharpening pencils"},
    {"name": "Tape measure", "description": "A flexible ruler for measuring distances"},
    {"name": "Calculator", "description": "An electronic device for calculations"},
    {"name": "Ruler", "description": "A straightedge for measuring lengths"},
    {"name": "Eraser", "description": "A tool for removing pencil marks"},
    {"name": "Binder clip", "description": "A metal clip for holding papers"},
    {"name": "Scissors", "description": "A tool for cutting various materials"},
    {"name": "Glue stick", "description": "A tool for bonding papers"},
    {"name": "Pushpin", "description": "A small pin for holding papers"},
    {"name": "Whiteboard marker", "description": "A marker for writing on whiteboards"},
    {"name": "Folder", "description": "A container for organizing papers"},
    {"name": "Sticky tab", "description": "A small adhesive label"},
    {"name": "Desk calendar", "description": "A calendar for keeping track of dates"},
    {"name": "Pencil case", "description": "A container for storing writing utensils"},
    {"name": "Index card", "description": "A small card for note-taking"},
    {"name": "Hole punch", "description": "A tool for creating holes in papers"},
    {"name": "Page flag", "description": "A small marker for marking pages"},
    {"name": "Correction tape", "description": "A tool for correcting mistakes"},
    {"name": "Desk lamp", "description": "A lamp for providing light"},
    {"name": "USB flash drive", "description": "A device for storing digital files"},
]

app_ui = ui.page_fluid(
    ui.panel_title("Virtual Scavenger Hunt"),
    ui.layout_column_wrap(
        ui.value_box(
            "Items Found",
            ui.output_text_verbatim("items_found_box"),
            id="items_found_box",
            theme="bg-gradient-success",
            showcase=ui.HTML(
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" fill="#ffd700" stroke="#ffd700" stroke-width="2" style="color: #ffd700;"><!--!Font Awesome Free 6.7.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path d="M400 0L176 0c-26.5 0-48.1 21.8-47.1 48.2c.2 5.3 .4 10.6 .7 15.8L24 64C10.7 64 0 74.7 0 88c0 92.6 33.5 157 78.5 200.7c44.3 43.1 98.3 64.8 138.1 75.8c23.4 6.5 39.4 26 39.4 45.6c0 20.9-17 37.9-37.9 37.9L192 448c-17.7 0-32 14.3-32 32s14.3 32 32 32l192 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l-26.1 0C337 448 320 431 320 410.1c0-19.6 15.9-39.2 39.4-45.6c39.9-11 93.9-32.7 138.2-75.8C542.5 245 576 180.6 576 88c0-13.3-10.7-24-24-24L446.4 64c.3-5.2 .5-10.4 .7-15.8C448.1 21.8 426.5 0 400 0zM48.9 112l84.4 0c9.1 90.1 29.2 150.3 51.9 190.6c-24.9-11-50.8-26.5-73.2-48.3c-32-31.1-58-76-63-142.3zM464.1 254.3c-22.4 21.8-48.3 37.3-73.2 48.3c22.7-40.3 42.8-100.5 51.9-190.6l84.4 0c-5.1 66.3-31.1 111.2-63 142.3z"/></svg>'
            ),
            showcase_layout="left center",
        ),
        ui.card(
            ui.card_header("Scavenger Hunt"),
            ui.output_text_verbatim("item_description"),
            ui.input_action_button("found_item", "I found it!"),
            ui.output_text_verbatim("status_message"),
            height="300px",
        ),
        width=1 / 2,
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    items_found = reactive.Value(0)
    current_item_index = reactive.Value(0)

    @render.text
    def item_description():
        item = items[current_item_index.get()]
        return f"Find: {item['name']}\n\n{item['description']}"

    @render.text
    @reactive.event(input.found_item)
    def status_message():
        items_found.set(items_found.get() + 1)
        next_index = current_item_index.get() + 1
        if next_index < len(items):
            current_item_index.set(next_index)
        else:
            current_item_index.set(0)  # Loop back to first item
        return "Great job! You found the item."

    @render.text
    def items_found_box():
        return str(items_found.get())


app = App(app_ui, server)
