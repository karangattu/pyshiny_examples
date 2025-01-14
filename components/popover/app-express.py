from shiny import reactive
from shiny.express import input, render, ui

# Add Font Awesome CSS to the app
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
    )
)

# Page title
ui.page_opts(title="Popover Demo", fillable=True)

# Create a card to contain the popovers
with ui.card(class_="p-4"):
    ui.h3("Popover Examples")
    ui.p("Click or hover over the buttons to see different popover behaviors")

    with ui.layout_column_wrap(width="200px"):
        # Basic popover with default parameters
        with ui.popover(id="basic_popover"):
            ui.input_action_button(
                "btn1", "Basic Popover", class_="btn btn-primary w-100 mb-2"
            )
            "This is a basic popover with default parameters"

        # Popover with custom placement (right)
        with ui.popover(id="right_popover", placement="right"):
            ui.input_action_button(
                "btn2", "Right Placement", class_="btn btn-secondary w-100 mb-2"
            )
            "This popover appears on the right"

        # Popover with custom placement (top)
        with ui.popover(id="top_popover", placement="top"):
            ui.input_action_button(
                "btn3", "Top Placement", class_="btn btn-success w-100 mb-2"
            )
            "This popover appears on top"

        # Popover with custom placement (bottom)
        with ui.popover(id="bottom_popover", placement="bottom"):
            ui.input_action_button(
                "btn4", "Bottom Placement", class_="btn btn-info w-100 mb-2"
            )
            "This popover appears at the bottom"

        # Popover with custom options
        with ui.popover(
            id="custom_popover",
            placement="auto",
            options={
                "animation": True,
                "delay": {"show": 500, "hide": 100},
                "trigger": "hover focus",
            },
        ):
            ui.input_action_button(
                "btn5",
                ui.HTML('<i class="fa-solid fa-gear"></i> Custom Options'),
                class_="btn btn-warning w-100 mb-2",
            )
            "This popover has custom animation, delay, and trigger options"

    # Show popover states
    ui.hr()
    ui.h4("Popover States")

    @render.text
    def popover_states():
        states = {
            "basic": input.basic_popover(),
            "right": input.right_popover(),
            "top": input.top_popover(),
            "bottom": input.bottom_popover(),
            "custom": input.custom_popover(),
        }
        return f"Current States: {states}"
