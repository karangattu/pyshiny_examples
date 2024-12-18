from shiny import reactive
from shiny.express import input, ui, render

ui.page_opts(title="Accordion Panel Update Demo", fillable=True)

# Create a switch to control updates
ui.input_switch("update_panel", "Update (and open) Sections", value=False)

# Create an accordion with multiple sections
with ui.accordion(id="acc", multiple=True):
    # Create multiple panels with initial content
    for letter in "ABCDE":
        with ui.accordion_panel(f"Section {letter}", value=f"sec_{letter}"):
            f"Initial narrative for section {letter}"


# Effect to update panels when switch is toggled
@reactive.effect
@reactive.event(input.update_panel)
def _():
    # Add text to indicate updated content
    txt = " (updated)" if input.update_panel() else ""
    # Show panels when switch is on, hide when off
    show = bool(input.update_panel())

    # Update each panel's content and title
    for letter in "ABCDE":
        ui.update_accordion_panel(
            "acc",
            f"sec_{letter}",
            f"Updated narrative for section {letter}{txt}",
            title=f"Section {letter}{txt}",
            # Open/close accordion panel based on switch state
            show=show,
        )

    # Update switch label to indicate next action
    next_show_txt = "close" if show else "open"
    ui.update_switch("update_panel", label=f"Update (and {next_show_txt}) Sections")
