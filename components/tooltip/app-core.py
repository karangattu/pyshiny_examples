from shiny import App, reactive, ui

# Define the UI
app_ui = ui.page_fluid(
    # Add Font Awesome to the app
    ui.head_content(
        ui.HTML(
            '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">'
        )
    ),
    # Create a card to contain the tooltips
    ui.card(
        ui.card_header("Tooltip Examples"),
        ui.layout_column_wrap(
            # Basic tooltip with default placement
            ui.tooltip(
                ui.input_action_button(
                    "btn1", "Default Tooltip", class_="btn-primary m-2"
                ),
                "This is a basic tooltip",
                id="tooltip1",
            ),
            # Tooltip with right placement
            ui.tooltip(
                ui.input_action_button(
                    "btn2", "Right Tooltip", class_="btn-success m-2"
                ),
                "This tooltip appears on the right",
                id="tooltip2",
                placement="right",
            ),
            # Tooltip with bottom placement
            ui.tooltip(
                ui.input_action_button("btn3", "Bottom Tooltip", class_="btn-info m-2"),
                "This tooltip appears at the bottom",
                id="tooltip3",
                placement="bottom",
            ),
            # Tooltip with left placement
            ui.tooltip(
                ui.input_action_button(
                    "btn4", "Left Tooltip", class_="btn-warning m-2"
                ),
                "This tooltip appears on the left",
                id="tooltip4",
                placement="left",
            ),
            # Tooltip with custom options
            ui.tooltip(
                ui.input_action_button(
                    "btn5", "Custom Options", class_="btn-danger m-2"
                ),
                "This tooltip has custom animation and delay",
                id="tooltip5",
                placement="auto",
                options={
                    "animation": True,
                    "delay": {"show": 500, "hide": 10000},
                    "trigger": "hover focus",
                },
            ),
            width=1 / 2,
        ),
        ui.hr(),
        # Control buttons in their own row
        ui.layout_column_wrap(
            # Button to show/hide tooltips dynamically
            ui.input_action_button(
                "toggle_tooltips",
                "Toggle All Tooltips",
                class_="btn-secondary mt-2",
            ),
            # Button to update tooltip content
            ui.input_action_button(
                "update_content",
                "Update Tooltip Content",
                class_="btn-secondary mt-2",
            ),
            width=1 / 2,
        ),
    ),
)


# Define the server
def server(input, output, session):
    # Effect to toggle tooltips
    @reactive.effect
    @reactive.event(input.toggle_tooltips)
    def toggle_tooltips():
        show_state = input.toggle_tooltips() % 2 == 1
        for i in range(1, 6):
            ui.update_tooltip(f"tooltip{i}", show=show_state)

    # Effect to update tooltip content
    @reactive.effect
    @reactive.event(input.update_content)
    def update_tooltip_content():
        count = input.update_content()
        for i in range(1, 6):
            ui.update_tooltip(
                f"tooltip{i}",
                f"Updated content {count} times! <i class='fa-solid fa-sync'></i>",
                show=True,
            )


# Create and return the app
app = App(app_ui, server)
