from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Checkbox Group Demo", fillable=True)

# Create some sample data
choices = {
    "red": ui.span("Red", style="color: #FF0000;"),
    "green": ui.span("Green", style="color: #00AA00;"),
    "blue": ui.span("Blue", style="color: #0000AA;"),
}

# Layout the UI elements
with ui.layout_columns(col_widths=[6, 6]):
    # Left column - Controls
    with ui.card():
        ui.card_header("Controls")

        # Label control
        ui.input_text("new_label", "New Label", value="Choose colors:")

        # Choices control
        ui.input_checkbox_group(
            "choice_selector",
            "Select choices to include:",
            choices=list(choices.keys()),
            selected=list(choices.keys()),
            inline=True,
        )

        # Selected control
        ui.input_checkbox_group(
            "selected_selector",
            "Pre-select colors:",
            choices=list(choices.keys()),
            inline=True,
        )

        # Inline control
        ui.input_radio_buttons(
            "inline_control",
            "Display inline?",
            choices={"true": "Yes", "false": "No"},
            selected="false",
        )

        # Update button
        ui.input_action_button(
            "update_btn", "Update Checkbox Group", class_="btn-primary"
        )

    # Right column - Demo checkbox group
    with ui.card():
        ui.card_header("Demo Checkbox Group")

        # The checkbox group we'll be updating
        ui.input_checkbox_group(
            "demo_group", "Choose colors:", choices=choices, selected=["red"]
        )

        # Show current state
        @render.text
        def current_selection():
            selected = input.demo_group()
            if not selected:
                return "No colors selected"
            return f"Selected colors: {', '.join(selected)}"


# Handle updates when button is clicked
@reactive.effect
@reactive.event(input.update_btn)
def _():
    # Get the current state of controls
    new_label = input.new_label()
    selected_choices = input.choice_selector()
    pre_selected = input.selected_selector()
    is_inline = input.inline_control() == "true"

    # Filter choices based on selection
    filtered_choices = {k: choices[k] for k in selected_choices}

    # Update the checkbox group with all parameters
    ui.update_checkbox_group(
        "demo_group",
        label=new_label,
        choices=filtered_choices,
        selected=pre_selected,
        inline=is_inline,
    )

    # Show notification
    ui.notification_show("Checkbox group updated!", type="message")
