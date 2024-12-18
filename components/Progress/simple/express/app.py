import time
import numpy as np
import pandas as pd
from shiny import reactive
from shiny.express import input, ui, render

# Page title
ui.page_opts(title="Progress Demo", fillable=True)

# Input controls
with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_slider(
            "n_samples", "Number of samples", 1000, 100000, 10000, step=1000
        )
        ui.input_action_button("compute", "Compute Statistics", class_="btn-primary")
        ui.hr()
        ui.input_numeric(
            "sleep", "Simulation delay (seconds)", 0.1, min=0, max=2, step=0.1
        )

    # Main panel content
    @render.data_frame
    @reactive.event(input.compute)
    def results():
        # Create a progress object
        p = ui.Progress(min=0, max=1)
        p.set(message="Initializing computation...")

        # Generate random data
        n = input.n_samples()
        delay = input.sleep()

        data = []
        steps = 5

        for i in range(steps):
            # Update progress
            p.set(
                value=(i / steps),
                message=f"Computing batch {i+1} of {steps}",
                detail=f"Processing {n//steps} samples...",
            )

            # Simulate computation time
            time.sleep(delay)

            # Generate batch of random data and compute statistics
            batch = np.random.normal(loc=100, scale=15, size=n // steps)
            stats = {
                "Batch": f"Batch {i+1}",
                "Mean": np.mean(batch),
                "Std Dev": np.std(batch),
                "Min": np.min(batch),
                "Max": np.max(batch),
            }
            data.append(stats)

        # Final progress update
        p.set(value=1, message="Computation complete!")
        time.sleep(0.5)  # Brief pause to show completion

        # Convert results to DataFrame
        return pd.DataFrame(data)

    @render.text
    def instructions():
        return """
        This app demonstrates the use of Progress in Shiny for Python.
        
        1. Adjust the number of samples using the slider
        2. Set the simulation delay to control computation time
        3. Click 'Compute Statistics' to start the calculation
        4. Watch the progress bar update as calculations proceed
        """
