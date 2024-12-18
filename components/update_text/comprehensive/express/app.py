from shiny import reactive
from shiny.express import input, render, ui

# Page options and layout
ui.page_opts(title="Text Input Update Demo", fillable=True)

# Create a layout with cards to organize the demo
with ui.layout_columns(col_widths=[6, 6]):
    # First card - Controls
    with ui.card(full_screen=True):
        ui.card_header("Control Panel")

        # Original text input
        ui.input_text(
            "original_text",
            "Original Text Input",
            value="Initial value",
            placeholder="Type something here",
        )

        ui.hr()

        # Controls to update the text input
        ui.input_text("new_label", "New Label", value="Updated Label")

        ui.input_text("new_value", "New Value", value="Updated value")

        ui.input_text("new_placeholder", "New Placeholder", value="Updated placeholder")

        ui.input_action_button("update_all", "Update All", class_="btn-primary")

        ui.input_action_button(
            "update_label", "Update Label Only", class_="btn-secondary"
        )

        ui.input_action_button(
            "update_value", "Update Value Only", class_="btn-success"
        )

        ui.input_action_button(
            "update_placeholder", "Update Placeholder Only", class_="btn-info"
        )

        ui.input_action_button("reset", "Reset", class_="btn-warning")

    # Second card - Current State
    with ui.card(full_screen=True):
        ui.card_header("Current State")

        @render.ui
        def current_state():
            return ui.tags.div(
                ui.tags.p(f"Current Input Value: {input.original_text()}"),
                ui.tags.p(f"Current Label Value: {input.new_label()}"),
                ui.tags.p(f"Current Value to Set: {input.new_value()}"),
                ui.tags.p(f"Current Placeholder: {input.new_placeholder()}"),
            )


# Effect handlers for the buttons
@reactive.effect
@reactive.event(input.update_all)
def _():
    ui.update_text(
        "original_text",
        label=input.new_label(),
        value=input.new_value(),
        placeholder=input.new_placeholder(),
    )


@reactive.effect
@reactive.event(input.update_label)
def _():
    ui.update_text("original_text", label=input.new_label())


@reactive.effect
@reactive.event(input.update_value)
def _():
    ui.update_text("original_text", value=input.new_value())


@reactive.effect
@reactive.event(input.update_placeholder)
def _():
    ui.update_text("original_text", placeholder=input.new_placeholder())


@reactive.effect
@reactive.event(input.reset)
def _():
    ui.update_text(
        "original_text",
        label="Original Text Input",
        value="Initial value",
        placeholder="Type something here",
    )
    ui.update_text("new_label", value="Updated Label")
    ui.update_text("new_value", value="Updated value")
    ui.update_text("new_placeholder", value="Updated placeholder")
