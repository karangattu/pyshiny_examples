from shiny import reactive
from shiny.express import input, render, ui

# Page options
ui.page_opts(title="Popover Update Demo", fillable=True)

# Add Font Awesome CSS for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">'
    )
)

# Create a layout with two columns
with ui.layout_columns(col_widths=[6, 6]):
    # Left column - Controls
    with ui.card():
        ui.card_header("Popover Controls")

        # Input for new title
        ui.input_text("new_title", "New Popover Title", value="Updated Title")

        # Input for new content
        ui.input_text_area(
            "new_content",
            "New Popover Content",
            value="This is updated content for the popover.",
        )

        # Buttons to control popover visibility
        ui.input_action_button("show_popover", "Show Popover", class_="btn-success m-2")
        ui.input_action_button("hide_popover", "Hide Popover", class_="btn-danger m-2")
        ui.input_action_button(
            "update_content", "Update Content", class_="btn-primary m-2"
        )

    # Right column - Popover Demo
    with ui.card():
        ui.card_header("Popover Demo")

        # Create a popover with initial content
        with ui.popover(id="demo_popover"):
            ui.input_action_button(
                "demo_button", "Click me! (I have a popover)", class_="btn-info m-2"
            )
            "Initial popover content"


# Handle show popover button
@reactive.effect
@reactive.event(input.show_popover)
def _():
    ui.update_popover("demo_popover", show=True)


# Handle hide popover button
@reactive.effect
@reactive.event(input.hide_popover)
def _():
    ui.update_popover("demo_popover", show=False)


# Handle content update button
@reactive.effect
@reactive.event(input.update_content)
def _():
    # Update both title and content
    ui.update_popover(
        "demo_popover",
        ui.HTML(
            f"""
            <div>
                <p>{input.new_content()}</p>
                <i class="fa-solid fa-check text-success"></i>
                <small class="text-muted">Updated at: {reactive.now()}</small>
            </div>
        """
        ),
        title=input.new_title(),
        show=True,
    )


# Handle demo button clicks
@reactive.effect
@reactive.event(input.demo_button)
def _():
    ui.notification_show("Button clicked!", duration=3, type="message")
