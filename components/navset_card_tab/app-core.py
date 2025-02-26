from shiny import App, reactive, render, ui
import matplotlib.pyplot as plt
import numpy as np

# Define the UI
app_ui = ui.page_fillable(
    ui.layout_sidebar(
        ui.sidebar(
            "This is the sidebar content",
            ui.input_slider("n", "N", min=0, max=100, value=20),
        ),
        # Create a navset_card_tab
        ui.navset_card_tab(
            # First tab panel
            ui.nav_panel(
                "Tab 1",
                "This is content for Tab 1",
                ui.card(ui.card_header("Tab 1 Card"), "Some content in Tab 1"),
                value="tab1",
            ),
            # Second tab panel
            ui.nav_panel(
                "Tab 2",
                "This is content for Tab 2",
                ui.card(ui.card_header("Tab 2 Card"), "Some content in Tab 2"),
                value="tab2",
            ),
            # Third tab panel
            ui.nav_panel(
                "Tab 3",
                "This is content for Tab 3",
                ui.card(ui.card_header("Tab 3 Card"), "Some content in Tab 3"),
                value="tab3",
            ),
            id="tabset",
            selected="tab2",
        ),
        # Add text output for selected tab
        ui.output_text("selected_tab"),
        # Add plot output
        ui.output_plot("plot"),
    )
)


# Define the server
def server(input, output, session):
    @output
    @render.text
    def selected_tab():
        return f"Currently selected tab: {input.tabset()}"

    @output
    @render.plot
    def plot():
        np.random.seed(19680801)
        data = np.random.randn(input.n())

        fig, ax = plt.subplots()
        ax.hist(data, bins=20)
        ax.set_title("Histogram of Random Data")
        return fig


# Create and return the app
app = App(app_ui, server)
