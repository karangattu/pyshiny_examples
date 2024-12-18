from shiny import reactive
from shiny.express import input, ui, render

# Synthetic data for demonstration
button_click_counts = {"primary_btn": 0, "secondary_btn": 0, "custom_btn": 0}

# Emoji list for dynamic icon changes
emojis = ["🚀", "🌟", "🎉", "🔥", "🌈", "💡", "🤖", "🚦"]

ui.page_opts(title="Action Button Update Showcase", fillable=True)

with ui.layout_sidebar():
    with ui.sidebar():
        # Control inputs for button updates
        ui.input_select(
            "label_select",
            "Change Button Label",
            ["Original", "New Label 1", "New Label 2", "Custom Label"],
        )

        ui.input_checkbox_group(
            "icon_select",
            "Select Icon Options",
            ["Add Icon", "Change Icon", "Remove Icon"],
            selected=[],
        )

        ui.input_checkbox("disable_toggle", "Toggle Button Disabled State")

    with ui.layout_columns():
        # Primary Button
        ui.input_action_button("primary_btn", "Primary Button", class_="btn-primary")

        # Secondary Button
        ui.input_action_button(
            "secondary_btn", "Secondary Button", class_="btn-secondary"
        )

        # Custom Button
        ui.input_action_button("custom_btn", "Custom Button", class_="btn-info")

    # Display button click counts
    @render.text
    def button_stats():
        return "\n".join(
            [
                f"Primary Button Clicks: {button_click_counts['primary_btn']}",
                f"Secondary Button Clicks: {button_click_counts['secondary_btn']}",
                f"Custom Button Clicks: {button_click_counts['custom_btn']}",
            ]
        )


# Reactive effects to update buttons
@reactive.effect
@reactive.event(input.primary_btn)
def _primary_btn_click():
    button_click_counts["primary_btn"] += 1


@reactive.effect
@reactive.event(input.secondary_btn)
def _secondary_btn_click():
    button_click_counts["secondary_btn"] += 1


@reactive.effect
@reactive.event(input.custom_btn)
def _custom_btn_click():
    button_click_counts["custom_btn"] += 1


# Button Update Logic
@reactive.effect
def update_buttons():
    # Label Update
    label_map = {
        "Original": "Original Button",
        "New Label 1": "Updated Button",
        "New Label 2": "Transformed Button",
        "Custom Label": f"Custom Label {button_click_counts['primary_btn']}",
    }

    # Icon Update
    icon_options = input.icon_select()
    current_icon = None

    if "Add Icon" in icon_options:
        current_icon = "🚀"
    elif "Change Icon" in icon_options:
        current_icon = emojis[button_click_counts["primary_btn"] % len(emojis)]
    elif "Remove Icon" in icon_options:
        current_icon = []  # Remove icon

    # Update Primary Button
    ui.update_action_button(
        "primary_btn",
        label=label_map[input.label_select()],
        icon=current_icon,
        disabled=input.disable_toggle(),
    )

    # Update Secondary Button
    ui.update_action_button(
        "secondary_btn",
        label=f"Secondary: {button_click_counts['secondary_btn']}",
        icon="🌈" if button_click_counts["secondary_btn"] % 2 == 0 else "🌟",
    )

    # Update Custom Button
    ui.update_action_button(
        "custom_btn",
        label=f"Custom: {button_click_counts['custom_btn']}",
        disabled=button_click_counts["custom_btn"] > 5,
    )
