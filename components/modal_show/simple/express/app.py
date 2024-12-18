from shiny import reactive
from shiny.express import input, ui, render

ui.page_opts(title="Modal Demo")

# Create sample data
sample_data = {"Item A": 100, "Item B": 200, "Item C": 300}

# Add a button to show modal
ui.input_action_button("show", "Show Details", class_="btn-primary")


# Display basic info
@render.text
def txt():
    return f"Total items: {len(sample_data)}"


# Modal handler
@reactive.effect
@reactive.event(input.show)
def _():
    # Create modal content
    content = ui.TagList(
        ui.h3("Item Details"),
        ui.tags.table(
            [
                ui.tags.tr([ui.tags.td(k), ui.tags.td(v)])
                for k, v in sample_data.items()
            ],
            class_="table table-striped",
        ),
        ui.modal_button("Close"),
    )

    # Create and show modal
    m = ui.modal(content, title="Sample Data", easy_close=True)
    ui.modal_show(m)
