from shiny import reactive
from shiny.express import input, render, ui

# Set page options
ui.page_opts(title="Update Sidebar Demo", fillable=True)

# Create a sidebar with an id (required for update_sidebar)
with ui.sidebar(id="demo_sidebar", open="always"):
    ui.h4("Sidebar Content")
    ui.markdown("This sidebar can be controlled using the buttons below.")

# Main content area
with ui.layout_column_wrap(width="100%"):
    with ui.card():
        ui.card_header("Sidebar Controls")
        with ui.layout_column_wrap(width=1 / 2):
            ui.input_action_button(
                "show_sidebar", "Show Sidebar", class_="btn-success w-100"
            )
            ui.input_action_button(
                "hide_sidebar", "Hide Sidebar", class_="btn-danger w-100"
            )

        ui.hr()

        @render.text
        def sidebar_state():
            return f"Current sidebar state: {input.demo_sidebar()}"


# Effect to show the sidebar
@reactive.effect
@reactive.event(input.show_sidebar)
def show_sidebar():
    ui.update_sidebar("demo_sidebar", show=True)


# Effect to hide the sidebar
@reactive.effect
@reactive.event(input.hide_sidebar)
def hide_sidebar():
    ui.update_sidebar("demo_sidebar", show=False)
