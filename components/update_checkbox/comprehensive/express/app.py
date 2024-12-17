from shiny import reactive
from shiny.express import input, ui, render

# Synthetic data for demonstration
pet_types = ["Dog", "Cat", "Bird", "Hamster", "Fish"]
pet_statuses = ["Vaccinated", "Needs Checkup", "Healthy", "Recovering"]

ui.page_opts(title="Checkbox Update Demo")

with ui.layout_sidebar():
    with ui.sidebar():
        # Primary checkbox to control updates
        ui.input_checkbox("enable_updates", "Enable Checkbox Updates", value=True)

        # Slider to dynamically change checkbox label
        ui.input_slider("label_length", "Label Length", min=5, max=20, value=10, step=1)

        # Dropdown to select checkbox value manipulation
        ui.input_select(
            "value_type",
            "Value Manipulation",
            choices=["Set True", "Set False", "Toggle"],
        )

        # Button to trigger update
        ui.input_action_button("update_btn", "Update Checkbox")

    # Main panel with multiple checkboxes to demonstrate updates
    with ui.layout_column_wrap(width=1 / 2):
        # Checkbox for pet ownership
        ui.input_checkbox("pet_owned", "I own a pet", value=False)

        # Checkbox for pet type selection
        ui.input_checkbox("exotic_pet", "Exotic Pet Owner", value=False)

        # Display current checkbox states
        @render.text
        def checkbox_states():
            return f"""
            Pet Owned: {input.pet_owned()}
            Exotic Pet: {input.exotic_pet()}
            Updates Enabled: {input.enable_updates()}
            """

    # Reactive effect to update checkboxes
    @reactive.effect
    @reactive.event(input.update_btn)
    def update_checkboxes():
        # Only update if updates are enabled
        if not input.enable_updates():
            ui.notification_show("Updates are disabled!", type="warning")
            return

        # Dynamic label generation based on slider
        label_length = input.label_length()
        truncated_label = "Pet Owner" + "." * (label_length - 9)

        # Value manipulation based on dropdown
        if input.value_type() == "Set True":
            new_value = True
        elif input.value_type() == "Set False":
            new_value = False
        else:  # Toggle
            new_value = not input.pet_owned()

        # Update checkboxes with various parameters
        ui.update_checkbox(
            "pet_owned",
            label=truncated_label,  # Dynamic label
            value=new_value,  # Dynamic value
        )

        # Conditional exotic pet checkbox update
        if new_value:  # Only update exotic pet if pet owned is true
            ui.update_checkbox(
                "exotic_pet",
                label="Exotic Pet" if new_value else "No Exotic Pet",
                value=False,  # Reset exotic pet when main pet checkbox changes
            )

        # Show a notification about the update
        ui.notification_show(
            f"Updated pet owned checkbox to {new_value}", duration=3, type="message"
        )
