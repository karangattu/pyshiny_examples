from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Panel Title Demo", fillable=True)

# Demonstrate panel_title with both parameters:
# 1. title - The title to display in the app's UI
# 2. window_title - The title to display on the browser tab

# Basic example with both parameters
ui.panel_title(
    ui.h2("Main Dashboard Title", class_="text-primary"),  # title parameter as Tag
    window_title="Dashboard | Analytics",  # window_title parameter as string
)

# Create a layout with different sections
with ui.layout_columns(col_widths=[6, 6]):
    # First card with dynamic title
    with ui.card():

        @render.ui
        def dynamic_title():
            return ui.panel_title(
                f"Active Users: {input.user_count()}",
                window_title=f"Users: {input.user_count()}",
            )

        ui.input_numeric("user_count", "Enter number of users:", value=100)

        @render.text
        def user_stats():
            return f"Currently tracking {input.user_count()} active users"

    # Second card with HTML in title
    with ui.card():
        ui.panel_title(
            ui.div(
                ui.h3("System Status", class_="text-success"),
                ui.span("🟢 Online", class_="badge bg-success"),
                class_="d-flex align-items-center gap-2",
            ),
            window_title="System Status",
        )

        @render.text
        def status():
            return "All systems operational"


# Bottom section with markdown title
with ui.card():
    ui.panel_title(
        ui.markdown("### Data Overview\n*Real-time metrics*"),
        window_title="Data Overview",
    )

    with ui.layout_columns(col_widths=[4, 4, 4]):
        # Column 1
        with ui.value_box(showcase=ui.h1("📊"), theme="bg-info"):
            "Metrics"
            "1,234"
            "Daily Average"

        # Column 2
        with ui.value_box(showcase=ui.h1("📈"), theme="bg-success"):
            "Growth"
            "+15%"
            "Month over Month"

        # Column 3
        with ui.value_box(showcase=ui.h1("🎯"), theme="bg-warning"):
            "Target"
            "95%"
            "Achievement Rate"
