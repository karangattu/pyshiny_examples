from shiny import reactive
from shiny.express import input, render, ui

# Set page options and include Font Awesome
ui.page_opts(title="Dynamic Accordion Demo", fillable=True)
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
    )
)

# Add a title
ui.h2("Dynamic Accordion Panel Demo")

# Add description
ui.markdown(
    """
Click the button below to add new panels to the accordion dynamically.
Each new panel will have a star icon and custom content.
"""
)

# Button to insert panels
ui.input_action_button("add_panel", "Add New Panel", class_="btn-primary mb-3")

# Initial accordion setup
with ui.accordion(id="accordion_demo", open=True):
    with ui.accordion_panel(
        "Initial Panel",
        value="panel1",
        icon=ui.HTML('<i class="fa-solid fa-home"></i>'),
    ):
        "This is the first panel with some initial content"

# Counter to keep track of added panels
panel_count = reactive.value(1)


@reactive.effect
@reactive.event(input.add_panel)
def add_new_panel():
    current_count = panel_count.get()
    panel_count.set(current_count + 1)

    # Create new panel content
    new_panel = ui.accordion_panel(
        f"Panel {current_count + 1}",
        value=f"panel{current_count + 1}",
        icon=ui.HTML('<i class="fa-solid fa-star"></i>'),
    )

    # Insert the new panel
    ui.insert_accordion_panel(
        id="accordion_demo",
        panel=new_panel,
        target="panel1" if current_count == 1 else f"panel{current_count}",
        position="after",
    )


# Display the current number of panels
@render.text
def panel_counter():
    return f"Current number of panels: {panel_count.get()}"
