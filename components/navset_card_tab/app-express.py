from shiny import reactive
from shiny.express import input, render, ui

# Set page options
ui.page_opts(title="Navset Card Tab Demo", fillable=True)

# Create main layout
with ui.layout_sidebar():
    with ui.sidebar():
        "This is the sidebar content"
        ui.input_slider("n", "N", min=0, max=100, value=20)

    # Create a navset_card_tab
    with ui.navset_card_tab(
        id="tabset",  # Optional ID for tracking selected tab
        selected="tab2",  # Initially selected tab
    ):
        # First tab panel
        with ui.nav_panel("Tab 1", value="tab1"):
            "This is content for Tab 1"
            with ui.card():
                ui.card_header("Tab 1 Card")
                "Some content in Tab 1"

        # Second tab panel
        with ui.nav_panel("Tab 2", value="tab2"):
            "This is content for Tab 2"
            with ui.card():
                ui.card_header("Tab 2 Card")
                "Some content in Tab 2"

        # Third tab panel
        with ui.nav_panel("Tab 3", value="tab3"):
            "This is content for Tab 3"
            with ui.card():
                ui.card_header("Tab 3 Card")
                "Some content in Tab 3"

    # Display which tab is currently selected
    @render.text
    def selected_tab():
        return f"Currently selected tab: {input.tabset()}"

    # Add a plot that updates based on the slider
    @render.plot
    def plot():
        import matplotlib.pyplot as plt
        import numpy as np

        np.random.seed(19680801)
        data = np.random.randn(input.n())

        fig, ax = plt.subplots()
        ax.hist(data, bins=20)
        ax.set_title("Histogram of Random Data")
        return fig
