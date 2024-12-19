from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Sidebar Update Demo", fillable=True)

# Create sidebar with controls
with ui.sidebar(id="sidebar", open="closed"):
    ui.h4("Settings")
    ui.input_numeric("num_points", "Number of points", value=50, min=10, max=100)
    ui.input_selectize(
        "chart_type", "Chart Type", choices=["Line", "Bar", "Scatter"], selected="Line"
    )

# Create main content
with ui.layout_columns(col_widths=[8, 4]):
    # Left column with buttons to control sidebar
    with ui.card():
        ui.card_header("Sidebar Controls")
        ui.input_action_button("open_sidebar", "Open Sidebar", class_="me-2")
        ui.input_action_button("close_sidebar", "Close Sidebar", class_="me-2")

        @render.text
        def sidebar_state():
            return f"Current sidebar state: {'Open' if input.sidebar() else 'Closed'}"

    # Right column showing selected values
    with ui.card():
        ui.card_header("Selected Values")

        @render.text
        def selected_values():
            return (
                f"Number of points: {input.num_points()}\n"
                f"Chart type: {input.chart_type()}"
            )


# Handle sidebar open button click
@reactive.effect
@reactive.event(input.open_sidebar)
def _():
    ui.update_sidebar("sidebar", show=True)


# Handle sidebar close button click
@reactive.effect
@reactive.event(input.close_sidebar)
def _():
    ui.update_sidebar("sidebar", show=False)
