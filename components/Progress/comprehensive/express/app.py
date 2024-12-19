import asyncio
import numpy as np
import pandas as pd
from shiny import reactive
from shiny.express import input, ui, render

ui.page_opts(title="Progress Demo", fillable=True)


# Create some sample data
def generate_data(n_rows=1000):
    return pd.DataFrame(
        {
            "id": range(n_rows),
            "value": np.random.normal(100, 15, n_rows),
            "category": np.random.choice(["A", "B", "C"], n_rows),
            "date": pd.date_range(start="2024-01-01", periods=n_rows),
        }
    )


with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_slider("n_steps", "Number of Steps", min=5, max=20, value=10)
        ui.input_slider("min_val", "Progress Min", min=0, max=5, value=0)
        ui.input_slider("max_val", "Progress Max", min=5, max=20, value=10)
        ui.input_action_button("start", "Start Processing", class_="btn-primary")
        ui.hr()
        ui.input_action_button(
            "start_inc", "Start with Increment", class_="btn-success"
        )
        ui.input_action_button("cancel_btn", "Cancel Processing", class_="btn-danger")

    with ui.card():
        ui.card_header("Progress Demo")

        @render.data_frame
        @reactive.event(input.start)
        async def result_table():
            # Initialize progress with custom min and max
            with ui.Progress(min=input.min_val(), max=input.max_val()) as p:
                # Set initial message
                p.set(message="Starting process...", detail="Initializing")
                await asyncio.sleep(1)

                # Generate base data
                df = generate_data()

                # Process data in steps
                n_steps = input.n_steps()
                for i in range(n_steps):
                    # Check for cancellation
                    if input.cancel_btn() > 0:
                        p.set(message="Process cancelled!", detail="User interrupted")
                        await asyncio.sleep(1)
                        return pd.DataFrame()

                    current_val = input.min_val() + (
                        i * ((input.max_val() - input.min_val()) / n_steps)
                    )
                    p.set(
                        value=current_val,
                        message=f"Processing step {i+1}/{n_steps}",
                        detail=f"Processing records {i*100}/{n_steps*100}",
                    )

                    # Simulate processing
                    await asyncio.sleep(0.5)

                    # Update data
                    mask = df["id"] % n_steps == i
                    df.loc[mask, "value"] *= 1.1

                # Final message
                p.set(
                    value=input.max_val(),
                    message="Processing complete!",
                    detail="All steps finished",
                )
                await asyncio.sleep(1)

                return df.head(10)

        @render.data_frame
        @reactive.event(input.start_inc)
        async def result_table_inc():
            # Initialize progress with increment demonstration
            with ui.Progress(min=input.min_val(), max=input.max_val()) as p:
                p.set(message="Starting incremental process...", detail="Initializing")
                await asyncio.sleep(1)

                df = generate_data(500)

                for i in range(input.n_steps()):
                    if input.cancel_btn() > 0:
                        p.set(message="Process cancelled!", detail="User interrupted")
                        await asyncio.sleep(1)
                        return pd.DataFrame()

                    # Demonstrate increment usage
                    increment = (input.max_val() - input.min_val()) / input.n_steps()
                    p.inc(
                        amount=increment,
                        message=f"Incremental step {i+1}/{input.n_steps()}",
                        detail=f"Processing with increment {increment:.2f}",
                    )

                    await asyncio.sleep(0.5)

                    # Update data
                    mask = df["id"] % input.n_steps() == i
                    df.loc[mask, "value"] *= 1.05

                p.set(message="Incremental processing complete!")
                await asyncio.sleep(1)

                return df.head(10)

    with ui.card():
        ui.card_header("Description")
        ui.markdown(
            """
        This app demonstrates the Progress functionality in Shiny for Python with:
        
        * Custom min/max values for the progress bar
        * Two different processing methods:
            * Regular progress updates using `set()`
            * Incremental updates using `inc()`
        * Progress messages and detailed status
        * Cancellation handling
        * Process step visualization
        """
        )
