from shiny import App, reactive, render, ui

# Define the UI
app_ui = ui.page_fillable(
    # Add Font Awesome CSS to the app
    ui.head_content(
        ui.HTML(
            '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
        )
    ),
    # Create a card to contain the popovers
    ui.card(
        ui.h3("Popover Examples"),
        ui.p("Click or hover over the buttons to see different popover behaviors"),
        ui.layout_column_wrap(
            # Basic popover with default parameters
            ui.popover(
                ui.input_action_button(
                    "btn1", "Basic Popover", class_="btn btn-primary w-100 mb-2"
                ),
                "This is a basic popover with default parameters",
                id="basic_popover",
            ),
            # Popover with custom placement (right)
            ui.popover(
                ui.input_action_button(
                    "btn2", "Right Placement", class_="btn btn-secondary w-100 mb-2"
                ),
                "This popover appears on the right",
                id="right_popover",
                placement="right",
            ),
            # Popover with custom placement (top)
            ui.popover(
                ui.input_action_button(
                    "btn3", "Top Placement", class_="btn btn-success w-100 mb-2"
                ),
                "This popover appears on top",
                id="top_popover",
                placement="top",
            ),
            # Popover with custom placement (bottom)
            ui.popover(
                ui.input_action_button(
                    "btn4", "Bottom Placement", class_="btn btn-info w-100 mb-2"
                ),
                "This popover appears at the bottom",
                id="bottom_popover",
                placement="bottom",
            ),
            # Popover with custom options
            ui.popover(
                ui.input_action_button(
                    "btn5",
                    ui.HTML('<i class="fa-solid fa-gear"></i> Custom Options'),
                    class_="btn btn-warning w-100 mb-2",
                ),
                "This popover has custom animation, delay, and trigger options",
                id="custom_popover",
                placement="auto",
                options={
                    "animation": True,
                    "delay": {"show": 500, "hide": 100},
                    "trigger": "hover focus",
                },
            ),
            width="200px",
        ),
        ui.hr(),
        ui.h4("Popover States"),
        ui.output_text("popover_states"),
        class_="p-4",
    ),
)


# Define the server
def server(input, output, session):
    @output
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


# Create the app
app = App(app_ui, server)
