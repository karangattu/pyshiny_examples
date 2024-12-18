from shiny import reactive
from shiny.express import input, ui, render

# Page options for the app
ui.page_opts(title="Dark Mode Demo", fillable=True, sidebar=True)

# Add Font Awesome CSS to use icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
    )
)

# Create a dark mode switch with all possible parameters
ui.input_dark_mode(
    id="mode",  # Optional ID to track dark mode state
    mode=None,  # Initial mode (None uses system settings)
    class_="mb-3",  # Additional CSS classes
    style="font-size: 1.2rem;",  # Custom styling
)

with ui.layout_sidebar():
    with ui.sidebar():
        ui.h4("Dark Mode Settings")
        ui.input_radio_buttons(
            "chart_type", "Select Chart Type", choices=["Line", "Bar", "Scatter"]
        )

    with ui.layout_columns():
        with ui.card():
            ui.card_header("Current Dark Mode Status")

            @render.text
            def dark_mode_status():
                status = "Dark" if input.mode() == "dark" else "Light"
                return f"Current mode: {status}"

        with ui.card():
            ui.card_header("Sample Chart")

            @render.plot
            def sample_plot():
                import matplotlib.pyplot as plt
                import numpy as np

                # Generate sample data
                x = np.linspace(0, 10, 100)
                y = np.sin(x)

                fig, ax = plt.subplots()

                # Set colors based on dark mode
                color_fg = "black" if input.mode() == "light" else "white"
                color_bg = "white" if input.mode() == "light" else "#333333"

                # Create plot based on selected type
                if input.chart_type() == "Line":
                    ax.plot(x, y, color=color_fg)
                elif input.chart_type() == "Bar":
                    ax.bar(x[::10], y[::10], color=color_fg)
                else:  # Scatter
                    ax.scatter(x, y, color=color_fg)

                # Style the plot based on dark mode
                ax.set_facecolor(color_bg)
                fig.patch.set_facecolor(color_bg)
                ax.tick_params(colors=color_fg)
                ax.spines["bottom"].set_color(color_fg)
                ax.spines["top"].set_color(color_fg)
                ax.spines["left"].set_color(color_fg)
                ax.spines["right"].set_color(color_fg)

                plt.title("Sample Visualization", color=color_fg)
                plt.xlabel("X axis", color=color_fg)
                plt.ylabel("Y axis", color=color_fg)

                return fig

        with ui.card():
            ui.card_header("Dark Mode Information")

            @render.ui
            def mode_info():
                current_mode = input.mode()
                if current_mode == "dark":
                    icon = ui.tags.i(class_="fa-solid fa-moon", style="color: #ffd700;")
                    text = "Dark mode is currently active. This helps reduce eye strain in low-light conditions."
                else:
                    icon = ui.tags.i(class_="fa-solid fa-sun", style="color: #ff8c00;")
                    text = "Light mode is currently active. This provides high contrast in well-lit environments."

                return ui.div(
                    ui.tags.h4(icon, " Mode Details"),
                    ui.p(text),
                    style="padding: 10px;",
                )
