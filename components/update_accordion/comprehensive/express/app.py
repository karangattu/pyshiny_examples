from shiny import reactive
from shiny.express import input, ui

# Synthetic data for accordion panels
accordion_data = [
    {
        "title": "Section Alpha",
        "value": "alpha",
        "content": "Details about Alpha section",
    },
    {"title": "Section Beta", "value": "beta", "content": "Insights into Beta section"},
    {
        "title": "Section Gamma",
        "value": "gamma",
        "content": "Exploration of Gamma section",
    },
    {
        "title": "Section Delta",
        "value": "delta",
        "content": "Deep dive into Delta section",
    },
    {
        "title": "Section Epsilon",
        "value": "epsilon",
        "content": "Understanding Epsilon section",
    },
]

# Page setup
ui.page_opts(title="Accordion Update Playground", fillable=True)

# Sidebar with control inputs
with ui.sidebar():
    ui.input_radio_buttons(
        "update_type",
        "Update Type",
        [
            "Update Title",
            "Update Content",
            "Update Value",
            "Show/Hide Panel",
            "Reset Panels",
        ],
    )

    ui.input_selectize(
        "target_panel", "Target Panel", [panel["value"] for panel in accordion_data]
    )

    ui.input_text(
        "new_title", "New Title (if applicable)", placeholder="Enter new title"
    )
    ui.input_text(
        "new_content", "New Content (if applicable)", placeholder="Enter new content"
    )
    ui.input_checkbox("show_panel", "Show Panel", value=True)

# Main accordion
with ui.accordion(id="demo_accordion", multiple=True):
    for panel in accordion_data:
        with ui.accordion_panel(panel["title"], value=panel["value"]):
            panel["content"]


# Reactive effect to handle accordion updates
@reactive.effect
@reactive.event(input.update_type)
def update_accordion():
    update_type = input.update_type()
    target_panel = input.target_panel()

    if update_type == "Update Title":
        new_title = input.new_title() or f"Updated {target_panel.capitalize()} Title"
        ui.update_accordion_panel("demo_accordion", target_panel, title=new_title)

    elif update_type == "Update Content":
        new_content = (
            input.new_content()
            or f"New content for {target_panel.capitalize()} section"
        )
        ui.update_accordion_panel("demo_accordion", target_panel, new_content)

    elif update_type == "Update Value":
        new_value = f"new_{target_panel}"
        ui.update_accordion_panel("demo_accordion", target_panel, value=new_value)

    elif update_type == "Show/Hide Panel":
        show_state = input.show_panel()
        ui.update_accordion_panel("demo_accordion", target_panel, show=show_state)

    elif update_type == "Reset Panels":
        # Reset all panels to their original state
        for panel in accordion_data:
            ui.update_accordion_panel(
                "demo_accordion",
                panel["value"],
                title=panel["title"],
                value=panel["value"],
                *[panel["content"]],  # Use *[] to pass content as a positional argument
            )


# Render current accordion state
@reactive.calc
def get_accordion_state():
    return f"Current Accordion State: {input.demo_accordion()}"


# Display accordion state
with ui.card():
    ui.card_header("Accordion State")
    get_accordion_state()
