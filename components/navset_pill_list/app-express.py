from shiny import reactive
from shiny.express import input, render, ui

# Set page options for a clean layout
ui.page_opts(title="Navset Pill List Demo", fillable=True)

with ui.layout_column_wrap(width=1):
    with ui.navset_pill_list(
        id="selected_pill_list", selected="Panel A", well=True, widths=(3, 9)
    ):
        # First nav panel
        with ui.nav_panel("Panel A"):
            with ui.card():
                ui.card_header("Panel A Content")
                "This is the content for Panel A"
                ui.input_text("text_a", "Enter text for Panel A", "")

        # Second nav panel
        with ui.nav_panel("Panel B"):
            with ui.card():
                ui.card_header("Panel B Content")
                "This is the content for Panel B"
                ui.input_slider("slider_b", "Slider for Panel B", 0, 100, 50)

        # Nav menu with additional panels
        with ui.nav_menu("More Options"):
            with ui.nav_panel("Panel C"):
                with ui.card():
                    ui.card_header("Panel C Content")
                    "This is the content for Panel C"
                    ui.input_numeric("num_c", "Number input for Panel C", 0)

            with ui.nav_panel("Panel D"):
                with ui.card():
                    ui.card_header("Panel D Content")
                    "This is the content for Panel D"
                    ui.input_checkbox("check_d", "Checkbox for Panel D", False)

    # Display the currently selected panel
    with ui.card():
        ui.card_header("Selection Status")

        @render.text
        def selected_panel():
            return f"Currently selected panel: {input.selected_pill_list()}"
