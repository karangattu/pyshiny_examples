from shiny import reactive
from shiny.express import input, ui, render

# Create some synthetic data for demonstration
sidebar_states = [
    {"open": True, "position": "left", "width": 250},
    {"open": False, "position": "right", "width": 300},
    {"open": "always", "position": "left", "width": 200},
]

ui.page_opts(title="Sidebar Update Demonstration", fillable=True)

# Create a sidebar with an ID for updating
with ui.sidebar(id="demo_sidebar", width=250, open="desktop"):
    ui.input_select(
        "sidebar_state",
        "Sidebar State",
        choices=["Open (Desktop Default)", "Closed", "Always Open"],
    )

    ui.input_select("sidebar_position", "Sidebar Position", choices=["Left", "Right"])

    ui.input_slider(
        "sidebar_width", "Sidebar Width", min=100, max=500, value=250, step=10
    )

# Main content area
with ui.card():
    ui.card_header("Sidebar Update Controls")

    # Buttons to demonstrate different update scenarios
    with ui.layout_columns():
        ui.input_action_button("open_sidebar", "Open Sidebar")
        ui.input_action_button("close_sidebar", "Close Sidebar")

    # Display current sidebar state
    @render.text
    def sidebar_state_display():
        return f"""
        Current Sidebar State:
        - Open: {input.demo_sidebar()}
        - Position: {input.sidebar_position()}
        - Width: {input.sidebar_width()}px
        """


# Reactive effect to update sidebar based on state selection
@reactive.effect
@reactive.event(input.sidebar_state)
def update_sidebar_state():
    state = input.sidebar_state()
    if state == "Open (Desktop Default)":
        ui.update_sidebar("demo_sidebar", show=True)
    elif state == "Closed":
        ui.update_sidebar("demo_sidebar", show=False)
    else:  # Always Open
        ui.update_sidebar("demo_sidebar", show="always")


# Reactive effect to update sidebar position
@reactive.effect
@reactive.event(input.sidebar_position)
def update_sidebar_position():
    position = input.sidebar_position().lower()
    # Note: This demonstrates how position can be dynamically changed
    with ui.sidebar(id="demo_sidebar", position=position):
        pass  # Redefine sidebar with new position


# Reactive effect to update sidebar width
@reactive.effect
@reactive.event(input.sidebar_width)
def update_sidebar_width():
    width = input.sidebar_width()
    # Note: Width is set during sidebar creation
    with ui.sidebar(id="demo_sidebar", width=width):
        pass  # Redefine sidebar with new width


# Additional buttons for direct sidebar manipulation
@reactive.effect
@reactive.event(input.open_sidebar)
def _():
    ui.update_sidebar("demo_sidebar", show=True)


@reactive.effect
@reactive.event(input.close_sidebar)
def _():
    ui.update_sidebar("demo_sidebar", show=False)
