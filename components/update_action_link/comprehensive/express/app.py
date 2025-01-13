from shiny import reactive
from shiny.express import input, render, ui

ui.page_opts(title="Action Link Update Demo", fillable=True)

# Create a layout with controls in sidebar
with ui.sidebar():
    ui.h4("Control Panel")
    ui.input_text("new_label", "New Label", value="Updated Link")
    ui.input_action_button("update_link", "Update Link")
    ui.hr()
    ui.markdown(
        """
    ### Current Parameters:
    * id: 'action_link'
    * label: customizable
    * icon: customizable
    """
    )

# Main content area
with ui.layout_columns():
    with ui.card():
        ui.card_header("Original Action Link")
        ui.input_action_link(
            "action_link",
            "Original Link",
            icon=ui.HTML('<i class="fa-solid fa-star"></i>'),
        )

        @render.text
        def action_count():
            return f"Link clicked {input.action_link()} times"


# Add Font Awesome for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">'
    )
)

# Define icons that can be cycled through
icons = [
    '<i class="fa-solid fa-star"></i>',
    '<i class="fa-solid fa-heart"></i>',
    '<i class="fa-solid fa-circle-check"></i>',
    '<i class="fa-solid fa-thumbs-up"></i>',
]
icon_index = reactive.value(0)


@reactive.effect
@reactive.event(input.update_link)
def _():
    # Update icon index cyclically
    current_index = icon_index.get()
    icon_index.set((current_index + 1) % len(icons))

    # Update the action link with new label and icon
    ui.update_action_link(
        id="action_link", label=input.new_label(), icon=ui.HTML(icons[icon_index.get()])
    )
