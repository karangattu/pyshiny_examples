from shiny import reactive
from shiny.express import input, ui, render

# Sample data
sample_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
"""

# Page options
ui.page_opts(title="Accordion Demo", fillable=True, padding=2)

# Add Font Awesome CSS for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
    )
)

with ui.layout_columns(col_widths=[6, 6]):
    # Basic accordion with all parameters
    with ui.accordion(
        id="acc1",
        open=["Panel 1"],  # Open first panel by default
        multiple=True,  # Allow multiple panels open
        class_="mt-3",  # Additional CSS classes
    ):
        with ui.accordion_panel(
            title="Panel 1",
            value="panel1",
            icon=ui.HTML('<i class="fa-solid fa-star"></i>'),
        ):
            ui.markdown("**Panel 1 Content**")
            ui.input_text("text1", "Enter text:", "Sample text")
            ui.markdown(sample_text)

        with ui.accordion_panel(
            title="Panel 2",
            value="panel2",
            icon=ui.HTML('<i class="fa-solid fa-heart"></i>'),
        ):
            ui.markdown("**Panel 2 Content**")
            ui.input_numeric("num1", "Enter number:", 42)
            ui.markdown(sample_text)

        with ui.accordion_panel(
            title="Panel 3",
            value="panel3",
            icon=ui.HTML('<i class="fa-solid fa-check"></i>'),
        ):
            ui.markdown("**Panel 3 Content**")
            ui.input_slider("slider1", "Select value:", 0, 100, 50)
            ui.markdown(sample_text)

    # Control panel to demonstrate dynamic updates
    with ui.card():
        ui.card_header("Accordion Controls")
        ui.input_action_button("add_panel", "Add New Panel", class_="me-2")
        ui.input_action_button("remove_panel", "Remove Last Panel", class_="me-2")
        ui.input_action_button("update_panel", "Update Panel 1", class_="me-2")

        @render.ui
        def accordion_state():
            return ui.markdown(f"Selected panels: {input.acc1()}")


# Second column with another accordion for comparison
with ui.accordion(
    id="acc2",
    open=True,  # Open all panels
    multiple=False,  # Only one panel can be open
    class_="mt-3",
):
    with ui.accordion_panel(
        title="Dynamic Panel",
        value="dynamic",
        icon=ui.HTML('<i class="fa-solid fa-gear"></i>'),
    ):

        @render.ui
        def dynamic_content():
            return ui.markdown(
                f"Last button clicked: {max(input.add_panel(), input.remove_panel(), input.update_panel())}"
            )


# Counter for new panels
panel_counter = reactive.Value(4)


@reactive.effect
@reactive.event(input.add_panel)
def _():
    from shiny.ui import accordion_panel

    current_count = panel_counter.get()
    new_panel = accordion_panel(
        title=f"Panel {str(current_count)}",
        value=f"panel{str(current_count)}",
        icon=ui.HTML('<i class="fa-solid fa-plus"></i>'),
    )

    ui.insert_accordion_panel("acc1", new_panel)
    panel_counter.set(current_count + 1)


@reactive.effect
@reactive.event(input.remove_panel)
def _():
    current_count = panel_counter.get()
    print(current_count)
    if current_count <= 4:
        ui.remove_accordion_panel("acc1", f"panel{current_count-1}")
        panel_counter.set(current_count - 1)


@reactive.effect
@reactive.event(input.update_panel)
def _():
    ui.update_accordion_panel(
        id="acc1",
        target="panel1",
        title="Panel 1 (Updated)",
        icon=ui.HTML('<i class="fa-solid fa-sync"></i>'),
    )
