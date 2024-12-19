from shiny import reactive
from shiny.express import input, ui, render

ui.page_opts(title="Action Button Update Demo", fillable=True)

# Create a layout with a sidebar
with ui.layout_sidebar():
    with ui.sidebar():
        ui.h4("Control Panel")
        ui.input_text("new_label", "New Button Label", value="Click me!")
        ui.input_switch("disable_button", "Disable Button", value=False)
        ui.input_action_button(
            "update_btn", "Update Button Settings", class_="btn-primary"
        )
        ui.hr()
        ui.markdown(
            """
        ### Parameters Demonstrated:
        - **label**: Change button text
        - **icon**: Add/remove icon
        - **disabled**: Enable/disable button
        """
        )

    # Main content area
    with ui.card():
        ui.card_header("Demo Area")

        # Target button that will be updated
        ui.input_action_button(
            "target_btn",
            "Original Button",
            icon=ui.tags.i(class_="fa-solid fa-star"),
            class_="btn-success",
        )

        # Display area for click count
        @render.text
        def click_count():
            return f"Button has been clicked {input.target_btn()} times"


# Effect to handle updates
@reactive.effect
@reactive.event(input.update_btn)
def _():
    # Update the button with new settings
    ui.update_action_button(
        "target_btn",
        label=input.new_label(),  # Update label from text input
        icon=(
            None
            if input.target_btn() % 2 == 0
            else ui.tags.i(class_="fa-solid fa-heart")
        ),  # Toggle icon
        disabled=input.disable_button(),  # Update disabled state
    )

    # Show notification
    ui.notification_show("Button settings updated!", type="message", duration=3)


# Add Font Awesome for icons
ui.head_content(
    ui.tags.link(
        rel="stylesheet",
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css",
    )
)
