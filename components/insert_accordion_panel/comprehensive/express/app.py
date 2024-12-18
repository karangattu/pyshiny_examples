from shiny import reactive
from shiny.express import input, ui, render

# Page options for better layout
ui.page_opts(title="Accordion Panel Demo", fillable=True)

# Main accordion to insert panels into
with ui.accordion(id="main_acc", open=True):
    with ui.nav_panel("Initial Panel"):
        "This is the initial panel. Use the buttons below to add more panels."

# Control buttons in a card
with ui.card():
    ui.card_header("Control Panel")

    # Buttons to demonstrate different insertion positions
    with ui.layout_column_wrap(width=1 / 2):
        ui.input_action_button("add_after", "Add Panel After")
        ui.input_action_button("add_before", "Add Panel Before")
        ui.input_action_button("add_end", "Add Panel at End")
        ui.input_action_button("add_start", "Add Panel at Start")

# Counter for unique panel names
panel_counter = reactive.value(1)


@reactive.effect
@reactive.event(input.add_after)
def add_panel_after():
    count = panel_counter.get()
    # Create new panel with content
    new_panel = ui.accordion_panel(
        f"Panel {count}",
        ui.markdown(
            f"""
        ### Dynamic Panel {count}
        This panel was inserted **after** the target panel.
        - Created at position: after
        - Panel number: {count}
        """
        ),
        value=f"panel_{count}",
    )

    # Insert the panel after the first panel
    ui.insert_accordion_panel(
        "main_acc", new_panel, target="Initial Panel", position="after"
    )
    panel_counter.set(count + 1)


@reactive.effect
@reactive.event(input.add_before)
def add_panel_before():
    count = panel_counter.get()
    # Create new panel with content
    new_panel = ui.accordion_panel(
        f"Panel {count}",
        ui.markdown(
            f"""
        ### Dynamic Panel {count}
        This panel was inserted **before** the target panel.
        - Created at position: before
        - Panel number: {count}
        """
        ),
        value=f"panel_{count}",
    )

    # Insert the panel before the first panel
    ui.insert_accordion_panel(
        "main_acc", new_panel, target="Initial Panel", position="before"
    )
    panel_counter.set(count + 1)


@reactive.effect
@reactive.event(input.add_end)
def add_panel_end():
    count = panel_counter.get()
    # Create new panel with content
    new_panel = ui.accordion_panel(
        f"Panel {count}",
        ui.markdown(
            f"""
        ### Dynamic Panel {count}
        This panel was inserted at the **end**.
        - Created at position: end
        - Panel number: {count}
        """
        ),
        value=f"panel_{count}",
    )

    # Insert the panel at the end (target=None, position="after")
    ui.insert_accordion_panel("main_acc", new_panel, target=None, position="after")
    panel_counter.set(count + 1)


@reactive.effect
@reactive.event(input.add_start)
def add_panel_start():
    count = panel_counter.get()
    # Create new panel with content
    new_panel = ui.accordion_panel(
        f"Panel {count}",
        ui.markdown(
            f"""
        ### Dynamic Panel {count}
        This panel was inserted at the **start**.
        - Created at position: start
        - Panel number: {count}
        """
        ),
        value=f"panel_{count}",
    )

    # Insert the panel at the start (target=None, position="before")
    ui.insert_accordion_panel("main_acc", new_panel, target=None, position="before")
    panel_counter.set(count + 1)


# Display current accordion state
@render.text
def show_state():
    return f"Total panels created: {panel_counter.get() - 1}"
