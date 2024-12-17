from shiny import reactive
from shiny.express import input, ui

# Synthetic data for the accordion panels
panel_data = {
    "Section A": "This is the initial content for Section A. It describes some interesting information.",
    "Section B": "Section B contains details about a specific topic. Learn more about its background.",
    "Section C": "Explore the contents of Section C, which provides insights into various aspects.",
    "Section D": "Section D offers a comprehensive overview of the subject matter.",
    "Section E": "The final section, Section E, wraps up our exploration with key takeaways.",
}

# Page setup
ui.page_opts(title="Accordion Panel Update Demo")

# Create the accordion with multiple panels
with ui.accordion(id="acc", multiple=True):
    for letter, content in panel_data.items():
        with ui.accordion_panel(f"Section {letter}", value=f"sec_{letter}"):
            content

# Sidebar with update controls
with ui.sidebar():
    ui.input_switch("update_panel", "Update Panels")
    ui.input_selectize(
        "select_panel", "Select Panel to Update", list(panel_data.keys())
    )


# Reactive effect to update accordion panels
@reactive.effect
@reactive.event(input.update_panel)
def _():
    # Determine if panels should be updated and shown
    txt = " (updated)" if input.update_panel() else ""
    show = bool(input.update_panel() % 2 == 1)

    # Update the selected panel
    selected_panel = input.select_panel()
    ui.update_accordion_panel(
        "acc",
        f"sec_{selected_panel.split()[-1]}",
        f"Updated content for {selected_panel}{txt}. This content has been dynamically modified.",
        title=f"{selected_panel}{txt}",
        # Open/close the panel based on the switch
        show=show,
    )

    # Update the switch label to indicate next action
    next_show_txt = "close" if show else "open"
    ui.update_switch("update_panel", label=f"Update (and {next_show_txt}) Sections")
