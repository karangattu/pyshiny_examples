from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Sidebar Update Demo", fillable=True)

# Create a sidebar with an ID for updating
with ui.sidebar(id="demo_sidebar", title="Interactive Sidebar"):
    ui.input_text("user_name", "Enter your name", "John Doe")
    ui.input_selectize(
        "dataset",
        "Select Dataset",
        choices=["Sales", "Marketing", "HR", "Finance"],
        selected="Sales",
    )

# Create buttons to control sidebar state
with ui.layout_column_wrap(width=1 / 4):
    ui.input_action_button("open_sidebar", "Open Sidebar", class_="btn-primary")
    ui.input_action_button("close_sidebar", "Close Sidebar", class_="btn-danger")
    ui.input_action_button("toggle_sidebar", "Toggle Sidebar", class_="btn-info")


# Display current sidebar state
@render.text
def sidebar_state():
    return f"Current Sidebar State: {'Open' if input.demo_sidebar() else 'Closed'}"


# Effect for opening sidebar
@reactive.effect
@reactive.event(input.open_sidebar)
def _():
    ui.update_sidebar(id="demo_sidebar", show=True)  # True to open the sidebar
    ui.notification_show("Sidebar Opened", type="message")


# Effect for closing sidebar
@reactive.effect
@reactive.event(input.close_sidebar)
def _():
    ui.update_sidebar(id="demo_sidebar", show=False)  # False to close the sidebar
    ui.notification_show("Sidebar Closed", type="warning")


# Effect for toggling sidebar
@reactive.effect
@reactive.event(input.toggle_sidebar)
def _():
    current_state = input.demo_sidebar()
    ui.update_sidebar(
        id="demo_sidebar", show=not current_state  # Toggle the current state
    )
    ui.notification_show(
        f"Sidebar {'Closed' if current_state else 'Opened'}", type="default"
    )


# Main content area
with ui.card():
    ui.card_header("Sidebar Control Demo")
    ui.markdown(
        """
    ### Instructions
    - Use the buttons above to control the sidebar
    - The sidebar state is tracked and displayed
    - Different notifications appear based on the action
    """
    )

    @render.ui
    def dynamic_content():
        return ui.markdown(
            f"""
        **Current Settings:**
        - User: {input.user_name()}
        - Selected Dataset: {input.dataset()}
        - Sidebar Status: {"Open" if input.demo_sidebar() else "Closed"}
        """
        )
