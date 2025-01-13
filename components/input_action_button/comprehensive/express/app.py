from shiny import reactive
from shiny.express import input, ui, render

# Page options and Font Awesome CSS
ui.page_opts(title="Action Button Demo", fillable=True)
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
    )
)

with ui.layout_sidebar():
    with ui.sidebar():
        ui.h4("Action Button Parameters Demo")
        ui.markdown(
            """
        This app demonstrates all parameters of `input_action_button`:
        - id
        - label
        - icon
        - width
        - disabled
        - **kwargs (class_, style)
        """
        )

    with ui.layout_column_wrap(width=1 / 2):
        # Basic button
        with ui.card(full_screen=True):
            ui.card_header("Basic Button")
            ui.input_action_button(id="basic_btn", label="Click Me!")

            @render.text
            def basic_clicks():
                return f"Basic button clicks: {input.basic_btn()}"

        # Button with icon
        with ui.card(full_screen=True):
            ui.card_header("Button with Icon")
            ui.input_action_button(
                id="icon_btn",
                label="Save",
                icon=ui.tags.i(class_="fa-solid fa-floppy-disk"),
            )

            @render.text
            def icon_clicks():
                return f"Icon button clicks: {input.icon_btn()}"

        # Button with custom width
        with ui.card(full_screen=True):
            ui.card_header("Button with Custom Width")
            ui.input_action_button(id="width_btn", label="Wide Button", width="100%")

            @render.text
            def width_clicks():
                return f"Wide button clicks: {input.width_btn()}"

        # Disabled button
        with ui.card(full_screen=True):
            ui.card_header("Disabled Button")
            ui.input_action_button(
                id="disabled_btn", label="Can't Click Me!", disabled=True
            )

            @render.text
            def disabled_clicks():
                return f"Disabled button clicks: {input.disabled_btn()}"

        # Button with custom class
        with ui.card(full_screen=True):
            ui.card_header("Button with Custom Class")
            ui.input_action_button(
                id="class_btn", label="Success Button", class_="btn-success"
            )

            @render.text
            def class_clicks():
                return f"Success button clicks: {input.class_btn()}"

        # Button with custom style
        with ui.card(full_screen=True):
            ui.card_header("Button with Custom Style")
            ui.input_action_button(
                id="style_btn",
                label="Styled Button",
                style="background-color: #ff69b4; color: white;",
            )

            @render.text
            def style_clicks():
                return f"Styled button clicks: {input.style_btn()}"

    # Dynamic button state control
    with ui.card():
        ui.card_header("Dynamic Button State Control")
        ui.input_switch("toggle_state", "Enable/Disable Button", value=True)
        ui.input_action_button(id="dynamic_btn", label="Dynamic State Button")

        @reactive.effect
        def _():
            ui.update_action_button("dynamic_btn", disabled=not input.toggle_state())

        @render.text
        def dynamic_clicks():
            return f"Dynamic button clicks: {input.dynamic_btn()}"

    # Button click counter with notification
    with ui.card():
        ui.card_header("Button with Notification")
        ui.input_action_button(
            id="notify_btn",
            label="Click for Notification",
            icon=ui.tags.i(class_="fa-solid fa-bell"),
        )

        @reactive.effect
        @reactive.event(input.notify_btn)
        def _():
            ui.notification_show(
                f"You've clicked the notification button {input.notify_btn()} times!",
                duration=3,
            )
