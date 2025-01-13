from shiny import reactive
from shiny.express import input, ui, render

ui.page_opts(title="remove_ui() Demo", fillable=True)

# Add some initial content with identifiable selectors
with ui.layout_column_wrap(width=1 / 2):
    with ui.card():
        ui.card_header("Controls")
        ui.input_action_button("remove_first", "Remove First Item", class_="me-2")
        ui.input_action_button("remove_all", "Remove All Items", class_="me-2")
        ui.input_action_button("remove_immediate", "Remove Immediately", class_="me-2")
        ui.input_action_button("add_items", "Add Items Back")

    with ui.card():
        ui.card_header("Dynamic Content")
        # Container for dynamic content
        with ui.div(id="content_container"):
            # Add multiple items with different selectors
            with ui.div(id="item1", class_="dynamic-item"):
                ui.h4("Item 1")
                ui.input_text("text1", "Enter text", "Sample text 1")

            with ui.div(id="item2", class_="dynamic-item"):
                ui.h4("Item 2")
                ui.input_text("text2", "Enter text", "Sample text 2")

            with ui.div(id="item3", class_="dynamic-item"):
                ui.h4("Item 3")
                ui.input_text("text3", "Enter text", "Sample text 3")

# Counter to track number of items
item_count = reactive.value(3)


@reactive.effect
@reactive.event(input.remove_first)
def remove_first_item():
    """Remove the first item using a specific selector"""
    if item_count.get() > 0:
        ui.remove_ui(
            selector="#item1",  # Specific selector for first item
            multiple=False,  # Only remove the first match
            immediate=False,  # Wait for all outputs to update
        )
        item_count.set(item_count.get() - 1)
        ui.notification_show("Removed first item", type="message")


@reactive.effect
@reactive.event(input.remove_all)
def remove_all_items():
    """Remove all items using a class selector"""
    if item_count.get() > 0:
        ui.remove_ui(
            selector=".dynamic-item",  # Class selector to match all items
            multiple=True,  # Remove all matches
            immediate=False,  # Wait for all outputs to update
        )
        item_count.set(0)
        ui.notification_show("Removed all items", type="warning")


@reactive.effect
@reactive.event(input.remove_immediate)
def remove_immediate():
    """Remove items immediately without waiting for outputs"""
    if item_count.get() > 0:
        ui.remove_ui(
            selector="div:has(> .dynamic-item)",  # Complex selector
            multiple=True,  # Remove all matches
            immediate=True,  # Remove immediately
        )
        item_count.set(0)
        ui.notification_show("Removed items immediately", type="error")


@reactive.effect
@reactive.event(input.add_items)
def add_items_back():
    """Add items back to demonstrate the effect"""
    if item_count.get() == 0:
        # Add items back using insert_ui
        for i in range(1, 4):
            ui.insert_ui(
                ui.div(
                    ui.h4(f"Item {i}"),
                    ui.input_text(f"text{i}", "Enter text", f"Sample text {i}"),
                    id=f"item{i}",
                    class_="dynamic-item",
                ),
                selector="#content_container",
                where="beforeEnd",
            )
        item_count.set(3)
        ui.notification_show("Added items back", type="message")


@render.ui
def item_status():
    """Display current status of items"""
    return ui.p(f"Current number of items: {item_count.get()}", class_="mt-3")
