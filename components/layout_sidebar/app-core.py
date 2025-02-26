from shiny import App, reactive, render, ui
import numpy as np
import matplotlib.pyplot as plt

# Define the UI
app_ui = ui.page_fillable(
    # Main layout using layout_sidebar
    ui.layout_sidebar(
        # Sidebar content
        ui.sidebar(
            ui.markdown("This is sidebar content demonstrating the layout"),
            ui.br(),
            ui.br(),
            ui.input_slider("n", "Number of bins", min=1, max=50, value=30),
            ui.input_checkbox_group(
                "options",
                "Choose options:",
                choices=["Option A", "Option B", "Option C"],
                selected=["Option A"],
            ),
            ui.markdown("The sidebar can be toggled on desktop and mobile"),
            id="demo_sidebar",
            open="desktop",
            title="Sidebar Title",
            position="left",
            width="300px",
            bg="#f8f9fa",
            fg="#212529",
            border=True,
            padding="1rem",
        ),
        # Main content area
        ui.card(
            ui.card_header("Main Content Area"),
            ui.markdown("This demonstrates the main content area of the layout"),
            ui.br(),
            ui.markdown("Notice the following features:"),
            ui.tags.ul(
                ui.tags.li("Responsive sidebar that can be toggled"),
                ui.tags.li("Custom styling in sidebar"),
                ui.tags.li("Interactive inputs in sidebar"),
                ui.tags.li("Card-based main content"),
                ui.tags.li("Organized layout structure"),
            ),
            ui.output_plot("histogram"),
        ),
    )
)


# Define the server
def server(input, output, session):
    @output
    @render.plot
    def histogram():
        # Generate sample data
        data = np.random.normal(100, 20, 200)

        # Create the histogram
        fig, ax = plt.subplots()
        ax.hist(data, bins=input.n())
        ax.set_title("Sample Histogram")
        ax.set_xlabel("Value")
        ax.set_ylabel("Frequency")

        return fig


# Create the app
app = App(app_ui, server)
