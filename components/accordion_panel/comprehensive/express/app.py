from shiny import reactive
from shiny.express import input, ui, render

ui.page_opts(title="Accordion Panel Demo", fillable=True)

# Create a demo icon using HTML
demo_icon = ui.HTML('<i class="fa-solid fa-shield-halved" style="color: #005eff;"></i>')

# Add Font Awesome for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
    )
)

with ui.layout_columns(width=1 / 2):
    with ui.accordion(id="acc1", open=True):
        # Basic panel with just title
        with ui.accordion_panel("Basic Panel"):
            "This is a basic panel with just a title"

        # Panel with title and value
        with ui.accordion_panel("Panel with Value", value="panel2"):
            "This panel has a custom value that can be used for selection"

        # Panel with title, value, and icon
        with ui.accordion_panel("Panel with Icon", value="panel3", icon=demo_icon):
            "This panel includes an icon from Font Awesome"

    # Show the currently selected panel
    @render.text
    def selected_panel():
        return f"Selected Panel: {input.acc1()}"

    with ui.accordion(id="acc2", open=["panel4", "panel5"]):
        # Multiple panels open by default
        with ui.accordion_panel("Panel 4", value="panel4"):
            "This panel is open by default"

        with ui.accordion_panel("Panel 5", value="panel5"):
            "This panel is also open by default"

        with ui.accordion_panel("Panel 6", value="panel6"):
            "This panel starts closed"

    @render.text
    def selected_panels():
        return f"Selected Panels: {input.acc2()}"


with ui.layout_columns(width=1):
    with ui.accordion(id="acc3", open=False):
        # Panel with dynamic content
        with ui.accordion_panel("Dynamic Content Panel", value="dynamic"):

            @render.data_frame
            def dynamic_data():
                import pandas as pd
                import numpy as np

                # Generate sample data
                np.random.seed(123)
                df = pd.DataFrame(
                    {
                        "Category": ["A", "B", "C", "D"],
                        "Value": np.random.randint(1, 100, 4),
                        "Score": np.random.uniform(0, 1, 4),
                    }
                )
                return df

        # Panel with interactive elements
        with ui.accordion_panel(
            "Interactive Panel",
            value="interactive",
            icon=ui.HTML('<i class="fa-solid fa-gear"></i>'),
        ):
            ui.input_slider("n", "Number", min=1, max=100, value=50)

            @render.text
            def slider_value():
                return f"Selected value: {input.n()}"

        # Panel with formatted content
        with ui.accordion_panel("Formatted Content", value="formatted"):
            ui.markdown(
                """
            ## Formatted Content Example
            
            This panel demonstrates:
            * Markdown formatting
            * Lists
            * **Bold text**
            * *Italic text*
            
            And a [link](https://shiny.posit.co/py/)
            """
            )

# Add controls to manipulate accordions
with ui.card():
    ui.card_header("Accordion Controls")

    ui.input_action_button("toggle_all", "Toggle All Panels")

    @reactive.effect
    @reactive.event(input.toggle_all)
    def _():
        # Update accordion states
        if input.toggle_all() % 2 == 0:
            ui.update_accordion("acc1", show=False)
            ui.update_accordion("acc2", show=False)
            ui.update_accordion("acc3", show=False)
        else:
            ui.update_accordion("acc1", show=True)
            ui.update_accordion("acc2", show=True)
            ui.update_accordion("acc3", show=True)
