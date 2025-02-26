import asyncio
from shiny import App, reactive, render, ui

# Define the UI
app_ui = ui.page_fillable(
    # First card
    ui.card(
        ui.card_header("Progress Demo"),
        ui.input_action_button("start", "Start Progress Demo", class_="m-3"),
        ui.output_ui("status"),
        ui.output_text("progress_demo"),
        full_screen=True,
        height="300px",
        id="card1",
    ),
    # Second card
    ui.card(
        ui.card_header("Results"),
        ui.output_text("results"),
        full_screen=True,
        height="200px",
        id="card2",
    ),
)


# Define the server
def server(input, output, session):
    @output
    @render.ui
    def status():
        return ui.div(id="status")

    @output
    @render.text
    @reactive.event(input.start)
    async def progress_demo():
        # Demo 1: Basic progress with default min=0, max=1
        with ui.Progress() as p1:
            p1.set(message="Basic progress (0 to 1)", detail="Starting...")
            for i in range(10):
                p1.set(i / 10)
                await asyncio.sleep(0.2)

        # Demo 2: Custom min and max values
        with ui.Progress(min=10, max=50) as p2:
            p2.set(message="Custom range (10 to 50)", detail="Processing...")
            for i in range(10, 51, 4):
                p2.set(i, detail=f"Step {i}")
                await asyncio.sleep(0.2)

        # Demo 3: Using increment with custom amounts
        with ui.Progress() as p3:
            p3.set(message="Using increment", detail="Starting increment demo")
            for i in range(5):
                p3.inc(0.2, detail=f"Increment {i+1}")
                await asyncio.sleep(0.2)

        # Demo 4: Multiple updates with message changes
        with ui.Progress(min=0, max=100) as p4:
            stages = ["Initializing", "Processing", "Finalizing"]
            p4.set(message="Multi-stage progress", detail=stages[0])
            for idx, stage in enumerate(stages):
                start = idx * 33
                for i in range(start, start + 33):
                    p4.set(i, detail=f"{stage}: Step {i-start+1}")
                    await asyncio.sleep(0.1)

        return "All progress demonstrations completed!"

    @output
    @render.text
    def results():
        if input.start() > 0:
            return "Progress demonstration has been started."
        return "Click the button above to start the progress demonstration."


# Create and return the app
app = App(app_ui, server)
