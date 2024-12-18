from shiny import reactive
from shiny.express import input, ui, render

# Page options and styling
ui.page_opts(title="Tooltip Demo", fillable=True)

# Add Font Awesome for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
    )
)

with ui.layout_columns(width=1 / 2):
    # Example 1: Basic tooltip with default placement
    with ui.tooltip(id="tooltip_basic"):
        ui.input_action_button("btn_basic", "Basic Tooltip", class_="btn-primary mt-3")
        "This is a basic tooltip"

    # Example 2: Tooltip with top placement
    with ui.tooltip(id="tooltip_top", placement="top"):
        ui.input_action_button("btn_top", "Top Tooltip", class_="btn-success mt-3")
        "This tooltip appears on top"

    # Example 3: Tooltip with right placement
    with ui.tooltip(id="tooltip_right", placement="right"):
        ui.input_action_button("btn_right", "Right Tooltip", class_="btn-info mt-3")
        "This tooltip appears on the right"

    # Example 4: Tooltip with bottom placement
    with ui.tooltip(id="tooltip_bottom", placement="bottom"):
        ui.input_action_button(
            "btn_bottom", "Bottom Tooltip", class_="btn-warning mt-3"
        )
        "This tooltip appears at the bottom"

    # Example 5: Tooltip with left placement
    with ui.tooltip(id="tooltip_left", placement="left"):
        ui.input_action_button("btn_left", "Left Tooltip", class_="btn-danger mt-3")
        "This tooltip appears on the left"

    # Example 6: Tooltip with custom options
    with ui.tooltip(
        id="tooltip_custom",
        placement="auto",
        options={
            "animation": True,
            "delay": {"show": 500, "hide": 100},
            "trigger": "hover focus",
        },
    ):
        ui.input_action_button(
            "btn_custom", "Custom Options", class_="btn-secondary mt-3"
        )
        "This tooltip has custom animation and delay"

# Interactive tooltip content update section
ui.hr()
with ui.card():
    ui.card_header("Interactive Tooltip Demo")

    with ui.layout_columns(width=1 / 2):
        # Button to show tooltip
        ui.input_action_button(
            "show_tooltip", "Show Dynamic Tooltip", class_="btn-primary mt-3"
        )

        # Button to hide tooltip
        ui.input_action_button(
            "hide_tooltip", "Hide Dynamic Tooltip", class_="btn-danger mt-3"
        )

    # Dynamic tooltip example
    with ui.tooltip(id="tooltip_dynamic", placement="right"):
        ui.input_action_button(
            "btn_dynamic",
            ui.HTML('<i class="fa-solid fa-gear"></i> Dynamic Tooltip'),
            class_="btn-info mt-3",
        )
        "Click the buttons above to control this tooltip"

# Counter for dynamic content
tooltip_counter = reactive.value(0)


@reactive.effect
@reactive.event(input.btn_dynamic)
def _():
    tooltip_counter.set(tooltip_counter.get() + 1)
    content = f"Tooltip content updated {tooltip_counter.get()} times"
    ui.update_tooltip("tooltip_dynamic", content, show=True)


@reactive.effect
@reactive.event(input.show_tooltip)
def _():
    ui.update_tooltip("tooltip_dynamic", show=True)


@reactive.effect
@reactive.event(input.hide_tooltip)
def _():
    ui.update_tooltip("tooltip_dynamic", show=False)


# Add description of the demo
ui.hr()
with ui.card():
    ui.card_header("About This Demo")
    ui.markdown(
        """
    This demo showcases various tooltip features in Shiny for Python:
    
    * Basic tooltip with default settings
    * Tooltips with different placements (top, right, bottom, left)
    * Custom tooltip with animation and delay
    * Dynamic tooltip with updateable content
    * Tooltip visibility control
    
    Hover over or click the buttons to see the tooltips in action!
    """
    )
