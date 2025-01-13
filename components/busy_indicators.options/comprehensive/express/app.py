import time
import numpy as np
import pandas as pd
from shiny import reactive
from shiny.express import input, ui, render
from matplotlib import pyplot as plt

# Set page options
ui.page_opts(title="Busy Indicators Demo", fillable=True)

# Configure busy indicators with all possible parameters
ui.busy_indicators.options(
    spinner_type="bars2",  # Type of spinner
    spinner_color="#FF5733",  # Custom color
    spinner_size="3rem",  # Size of spinner
    spinner_delay="1s",  # Delay before showing spinner
    fade_opacity=0.5,  # Opacity for recalculating output
    fade_selector=".fade-target",  # CSS selector for fade
    pulse_background="linear-gradient(45deg, #FF5733, #33FF57, #3357FF)",  # Custom pulse background
    pulse_height="4px",  # Height of pulse banner
    pulse_speed="2s",  # Speed of pulse animation
)

# Add Font Awesome for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">'
    )
)


# Create sidebar with controls
with ui.sidebar():
    ui.h3("Controls")
    ui.input_slider("rows", "Number of Rows", 1000, 100000, 5000)
    ui.input_slider("delay", "Processing Delay (s)", 0, 5, 2, step=0.5)
    ui.input_action_button("generate", "Generate Data", class_="btn-primary")
    ui.input_action_button("compute", "Run Computation", class_="btn-success")
    ui.hr()
    ui.markdown(
        """
    ### Busy Indicators Demo
    This app demonstrates all possible parameters of `busy_indicators.options`:
    - Custom spinner type and color
    - Delayed spinner appearance
    - Fade effects
    - Pulse animation
    """
    )

# Create main content area
with ui.layout_columns(col_widths=[6, 6]):
    # First column
    with ui.card():
        ui.card_header("Generated Data")

        @render.data_frame
        @reactive.event(input.generate)
        def show_data():
            time.sleep(input.delay())
            # Generate sample data
            n = input.rows()
            data = pd.DataFrame(
                {
                    "ID": range(n),
                    "Value": np.random.normal(100, 15, n),
                    "Category": np.random.choice(["A", "B", "C"], n),
                    "Score": np.random.uniform(0, 100, n),
                }
            )
            return data.head(10)

    # Second column
    with ui.card():
        ui.card_header("Computation Results")

        @render.plot
        @reactive.event(input.compute)
        def show_plot():
            time.sleep(input.delay())
            # Generate and plot some data
            x = np.random.normal(0, 1, 1000)
            y = np.random.normal(0, 1, 1000)
            fig, ax = plt.subplots()
            ax.scatter(x, y, alpha=0.5)
            ax.set_title("Random Scatter Plot")
            return fig


# Add some explanatory text at the bottom
with ui.card():
    ui.card_header("About Busy Indicators")
    ui.markdown(
        """
    The busy indicators in this app have been configured with custom settings:
    
    * A custom spinner type (`bars3`) with orange color
    * 1-second delay before showing the spinner
    * 50% opacity for fading effects
    * Custom gradient background for the pulse animation
    * 4px height for the pulse banner
    * 2-second animation speed for the pulse
    
    Try clicking the buttons above and observe the different loading indicators!
    """
    )
