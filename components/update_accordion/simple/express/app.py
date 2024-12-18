from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Accordion Update Demo", fillable=True)

# Add some controls
with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_switch("update_panel", "Update (and open) Sections")
        ui.input_switch("show_details", "Show Extra Details")

# Create accordion with multiple panels
with ui.accordion(id="acc", multiple=True):
    for section in ["Sales", "Marketing", "Operations"]:
        with ui.accordion_panel(f"{section} Report", value=f"sec_{section}"):
            f"Basic {section} metrics and KPIs"


# Update accordion panels based on user input
@reactive.effect
@reactive.event(input.update_panel)
def _():
    txt = " (Updated)" if input.update_panel() else ""
    show = bool(input.update_panel())

    # Update each section with new content and title
    for section in ["Sales", "Marketing", "Operations"]:
        details = ""
        if input.show_details():
            details = (
                f"\n\nDetailed {section} Analysis:\n"
                + f"- Year-to-date {section} performance\n"
                + f"- Quarter-over-quarter growth\n"
                + f"- Regional breakdown"
            )

        content = f"Basic {section} metrics and KPIs{details}"

        ui.update_accordion_panel(
            "acc",
            f"sec_{section}",
            content,
            title=f"{section} Report{txt}",
            show=show,  # Open accordion panel to see updated contents
        )

    next_show_txt = "close" if show else "open"
    ui.update_switch("update_panel", label=f"Update (and {next_show_txt}) Sections")
