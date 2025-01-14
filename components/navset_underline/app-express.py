from shiny import reactive
from shiny.express import input, render, ui

# Set page options
ui.page_opts(title="Navset Underline Demo", fillable=True)

# Create navset with underlined navigation
with ui.navset_underline(id="nav_id"):
    # Panel A
    with ui.nav_panel("Panel A"):
        with ui.card():
            ui.card_header("Panel A Content")
            "This is the content for Panel A"
            ui.input_text("text_a", "Enter text for Panel A", "Sample text")

    # Panel B
    with ui.nav_panel("Panel B", value="panel_b"):
        with ui.card():
            ui.card_header("Panel B Content")
            "This is the content for Panel B"
            ui.input_numeric("num_b", "Enter number for Panel B", 42)

    # Panel C
    with ui.nav_panel("Panel C"):
        with ui.card():
            ui.card_header("Panel C Content")
            "This is the content for Panel C"
            ui.input_slider("slider_c", "Slide in Panel C", 0, 100, 50)

    # Dropdown menu for additional panels
    with ui.nav_menu("More Options"):
        with ui.nav_panel("Panel D"):
            with ui.card():
                ui.card_header("Panel D Content")
                "This is the content for Panel D"
                ui.input_checkbox("check_d", "Check this in Panel D")

        with ui.nav_panel("Panel E"):
            with ui.card():
                ui.card_header("Panel E Content")
                "This is the content for Panel E"
                ui.input_radio_buttons(
                    "radio_e",
                    "Choose in Panel E",
                    choices=["Option 1", "Option 2", "Option 3"],
                )

# Show which panel is currently selected
with ui.card():
    ui.card_header("Navigation Status")

    @render.text
    def selected_panel():
        return f"Currently selected panel: {input.nav_id()}"


# Show inputs from various panels
with ui.card():
    ui.card_header("Input Values")

    @render.text
    def panel_values():
        return (
            f"Text from Panel A: {input.text_a()}\n"
            f"Number from Panel B: {input.num_b()}\n"
            f"Slider value from Panel C: {input.slider_c()}\n"
            f"Checkbox state from Panel D: {input.check_d()}\n"
            f"Radio selection from Panel E: {input.radio_e()}"
        )
