from shiny import reactive
from shiny.express import input, ui, render

# Add Font Awesome CSS to use icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">'
    )
)

ui.page_opts(title="Popover Demo", fillable=True)

with ui.layout_columns(col_widths=[6, 6]):
    # Example 1: Basic Popover with default placement
    with ui.card():
        ui.card_header("Basic Popover (Default Placement)")
        with ui.popover(id="basic_popover"):
            ui.input_action_button("btn_basic", "Click me!", class_="btn-primary")
            "This is a basic popover with default placement"

    # Example 2: Popover with custom placement
    with ui.card():
        ui.card_header("Popover with Right Placement")
        with ui.popover(id="right_popover", placement="right"):
            ui.input_action_button("btn_right", "Right Popover", class_="btn-info")
            "This popover appears on the right"

    # Example 3: Popover with title and custom options
    with ui.card():
        ui.card_header("Popover with Title and Custom Options")
        with ui.popover(
            id="custom_popover",
            title="Custom Title",
            placement="top",
            options={"trigger": "hover"},
        ):
            ui.input_action_button("btn_custom", "Hover me!", class_="btn-warning")
            "This popover appears on hover instead of click"

    # Example 4: Popover with dynamic content
    with ui.card():
        ui.card_header("Dynamic Popover Content")
        with ui.popover(id="dynamic_popover", placement="bottom"):
            ui.input_action_button(
                "btn_dynamic",
                ui.HTML('<i class="fa-solid fa-gear"></i> Settings'),
                class_="btn-secondary",
            )
            ui.input_select(
                "setting_option",
                "Choose setting:",
                choices=["Option A", "Option B", "Option C"],
            )
            ui.input_numeric("setting_value", "Value:", value=10)

# Add a section to demonstrate popover updates
ui.hr()
with ui.layout_columns(col_widths=[4, 4, 4]):
    # Example 5: Updatable Popover
    with ui.card():
        ui.card_header("Updatable Popover")
        with ui.popover(id="update_popover", placement="left"):
            ui.input_action_button(
                "btn_update", "Click to Update", class_="btn-success"
            )
            "Initial content"
        ui.input_action_button("trigger_update", "Update Popover Content")

    # Example 6: Popover with show/hide controls
    with ui.card():
        ui.card_header("Control Popover Visibility")
        with ui.popover(id="control_popover"):
            ui.input_action_button(
                "btn_control", "Controlled Popover", class_="btn-danger"
            )
            "This popover can be controlled programmatically"
        ui.input_action_button("show_popover", "Show Popover", class_="me-2")
        ui.input_action_button("hide_popover", "Hide Popover")

    # Example 7: Popover with HTML content
    with ui.card():
        ui.card_header("HTML Content Popover")
        with ui.popover(id="html_popover", placement="auto"):
            ui.input_action_button(
                "btn_html",
                ui.HTML('<i class="fa-solid fa-code"></i> HTML Demo'),
                class_="btn-dark",
            )
            ui.HTML(
                """
                <div style='color: blue;'>
                    <h5>Formatted Content</h5>
                    <ul>
                        <li>Item 1</li>
                        <li>Item 2</li>
                    </ul>
                </div>
            """
            )


# Add reactive effects to handle popover updates and controls
@reactive.effect
@reactive.event(input.trigger_update)
def _():
    update_count = input.trigger_update()
    ui.update_popover(
        "update_popover", f"Content updated {update_count} times!", show=True
    )


@reactive.effect
@reactive.event(input.show_popover)
def _():
    ui.update_popover("control_popover", show=True)


@reactive.effect
@reactive.event(input.hide_popover)
def _():
    ui.update_popover("control_popover", show=False)


# Add a display to show which popover was last clicked
@render.text
def last_clicked():
    ctx = reactive.get_current_context()
    for input_id in [
        "btn_basic",
        "btn_right",
        "btn_custom",
        "btn_dynamic",
        "btn_update",
        "btn_control",
        "btn_html",
    ]:
        if hasattr(input, input_id) and getattr(input, input_id)():
            return f"Last clicked: {input_id}"
    return "No button clicked yet"
