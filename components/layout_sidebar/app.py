from shiny import reactive
from shiny.express import input, ui, render

# Page options for a more complete layout
ui.page_opts(title="Layout Sidebar Demo", fillable=True)

# Main layout using layout_sidebar with all possible parameters
with ui.layout_sidebar():
    # Sidebar content
    with ui.sidebar(
        id="demo_sidebar",
        open="desktop",
        title="Sidebar Title",
        position="left",
        width="300px",
        bg="#f8f9fa",
        fg="#212529",
        border=True,
        padding="1rem",
    ):
        ui.markdown("This is sidebar content demonstrating the layout")
        ui.br()
        ui.br()
        ui.input_slider("n", "Number of bins", min=1, max=50, value=30)
        ui.input_checkbox_group(
            "options",
            "Choose options:",
            choices=["Option A", "Option B", "Option C"],
            selected=["Option A"],
        )
        ui.markdown("The sidebar can be toggled on desktop and mobile")

    # Main content area
    with ui.card():
        ui.card_header("Main Content Area")
        ui.markdown("This demonstrates the main content area of the layout")
        ui.br()
        ui.markdown("Notice the following features:")
        with ui.tags.ul():
            ui.tags.li("Responsive sidebar that can be toggled")
            ui.tags.li("Custom styling in sidebar")
            ui.tags.li("Interactive inputs in sidebar")
            ui.tags.li("Card-based main content")
            ui.tags.li("Organized layout structure")

        @render.plot
        def histogram():
            import numpy as np
            import matplotlib.pyplot as plt

            # Generate sample data
            data = np.random.normal(100, 20, 200)

            # Create the histogram
            fig, ax = plt.subplots()
            ax.hist(data, bins=input.n())
            ax.set_title("Sample Histogram")
            ax.set_xlabel("Value")
            ax.set_ylabel("Frequency")

            return fig
