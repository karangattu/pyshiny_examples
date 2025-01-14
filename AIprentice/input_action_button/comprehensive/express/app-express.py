from shiny import reactive
from shiny.express import input, ui, render
import time
import pandas as pd

# Set page options
ui.page_opts(title="Action Button Demo", fillable=True)

# Add Font Awesome CSS for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
    )
)

# Add custom button styling
ui.head_content(
    ui.HTML(
        """
        <style>
        .custom-button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
        }
        .custom-button:hover {
            background-color: #45a049;
        }
        </style>
        """
    )
)

with ui.layout_columns(col_widths=[6, 6]):
    with ui.card():
        ui.card_header("Basic Button")
        ui.input_action_button(id="basic_btn", label="Basic Button", width="200px")

        @render.text
        def basic_clicks():
            return f"Basic button clicks: {input.basic_btn()}"

    with ui.card():
        ui.card_header("Button with Icon")
        ui.input_action_button(
            id="icon_btn",
            label="Button with Icon",
            icon=ui.tags.i(class_="fa-solid fa-star"),
            width="200px",
        )

        @render.text
        def icon_clicks():
            return f"Icon button clicks: {input.icon_btn()}"

    with ui.card():
        ui.card_header("Disabled Button")
        ui.input_action_button(
            id="disabled_btn", label="Initially Disabled", disabled=True, width="200px"
        )
        ui.input_action_button(
            id="toggle_disabled", label="Toggle Disabled State", class_="mt-2"
        )

        @reactive.effect
        @reactive.event(input.toggle_disabled)
        def toggle_disabled():
            current_state = input.disabled_btn.disabled
            ui.update_action_button("disabled_btn", disabled=not current_state)

        @render.text
        def disabled_clicks():
            return f"Disabled button clicks: {input.disabled_btn()}"

    with ui.card():
        ui.card_header("Styled Button")
        ui.input_action_button(
            id="styled_btn",
            label="Custom Styled Button",
            width="200px",
            class_="custom-button",
        )

        @render.text
        def styled_clicks():
            return f"Styled button clicks: {input.styled_btn()}"

    with ui.card():
        ui.card_header("Button with Additional Attributes")
        ui.input_action_button(
            id="attr_btn",
            label="Button with Attributes",
            width="200px",
            title="Hover over me!",
            style="border-radius: 25px;",
        )

        @render.text
        def attr_clicks():
            return f"Attribute button clicks: {input.attr_btn()}"

    with ui.card():
        ui.card_header("Progress Button")
        ui.input_action_button(id="progress_btn", label="Start Progress", width="200px")

        @reactive.effect
        @reactive.event(input.progress_btn)
        def show_progress():
            with ui.Progress(min=1, max=10) as p:
                for i in range(1, 11):
                    p.set(value=i, message=f"Processing step {i}")
                    ui.update_action_button(
                        "progress_btn", label=f"Processing {i*10}%", disabled=True
                    )
                    time.sleep(0.5)  # Simulate work being done
                ui.update_action_button(
                    "progress_btn", label="Start Progress", disabled=False
                )


# Add click counter display for all buttons
with ui.card():
    ui.card_header("Total Click Statistics")

    @render.data_frame
    def click_stats():
        df = pd.DataFrame(
            {
                "Button": [
                    "Basic",
                    "Icon",
                    "Disabled",
                    "Styled",
                    "Attribute",
                    "Progress",
                ],
                "Clicks": [
                    input.basic_btn(),
                    input.icon_btn(),
                    input.disabled_btn(),
                    input.styled_btn(),
                    input.attr_btn(),
                    input.progress_btn(),
                ],
            }
        )
        return df
