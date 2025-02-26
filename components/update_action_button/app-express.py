from shiny import reactive
from shiny.express import input, ui, render

# Page title
ui.page_opts(title="Update Action Button Demo", fillable=True)

with ui.layout_sidebar():
    with ui.sidebar():
        # Controls to demonstrate each parameter of update_action_button
        ui.input_text(id="new_label", label="Enter new label", value="Updated Label")

        ui.input_checkbox(id="toggle_disabled", label="Disable button", value=False)

        # Button to trigger the update
        ui.input_action_button(id="update_btn", label="Update Button", class_="mt-3")

    # Main panel content
    with ui.card():
        ui.card_header("Demo Area")

        # Create a base action button that we'll update
        ui.input_action_button(
            id="target_btn",
            label="Original Button",
        )

        # Display the current state
        @render.text
        def button_state():
            return f"""
            Button clicks: {input.target_btn()}
            Current label: {input.new_label()}
            Is disabled: {input.toggle_disabled()}
            """


@reactive.effect
@reactive.event(input.update_btn)
def update_button():
    # Update the button using all available parameters
    ui.update_action_button(
        id="target_btn",
        label=input.new_label(),
        icon="🔄",  # Using an emoji as a simple icon
        disabled=input.toggle_disabled(),
    )
