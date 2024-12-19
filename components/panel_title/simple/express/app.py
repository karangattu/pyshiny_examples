from shiny.express import input, render, ui

# Set page options
ui.page_opts(title="Panel Title Demo", fillable=True)

# Add a panel title with different titles for the page and browser window
ui.panel_title("Main Dashboard View", window_title="Analytics Dashboard")

# Create some sample data display
with ui.layout_column_wrap(width=1 / 2):
    with ui.card():
        ui.card_header("Daily Statistics")

        @render.text
        def stats():
            return "Active Users: 1,234\nTotal Sessions: 5,678\nAvg. Time: 15.3 min"

    with ui.card():
        ui.card_header("System Status")

        @render.text
        def status():
            return "All Systems Operational\nServer Load: 42%\nResponse Time: 0.3s"


# Add some interactive elements
with ui.layout_column_wrap(width=1 / 3):
    with ui.card():
        ui.input_select(
            "view_option", "Select View", choices=["Overview", "Details", "Analytics"]
        )

        @render.text
        def selected_view():
            return f"Currently viewing: {input.view_option()}"
