from shiny import reactive
from shiny.express import input, render, ui

ui.page_opts(title="Task Button Demo", fillable=True)

with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_numeric("n", "Number of simulations", 1000, min=100, max=10000)
        ui.input_task_button("run", "Run Simulations", class_="btn-primary")
        ui.input_action_button("cancel", "Cancel", class_="btn-danger")

    with ui.card():
        ui.card_header("Simulation Results")

        @render.text
        def status():
            if not compute.running():
                return "Ready to run simulations"
            return f"Running {input.n()} simulations..."

        @render.text
        def result():
            if compute.complete():
                return f"Completed {compute.result()} simulations"
            return ""


@reactive.effect
@reactive.event(input.run)
def _():
    compute(input.n())


@reactive.effect
@reactive.event(input.cancel)
def _():
    compute.cancel()


@ui.bind_task_button(button_id="run")
@reactive.extended_task
async def compute(n: int) -> int:
    import asyncio
    import random

    # Simulate some work
    for i in range(n):
        if random.random() < 0.001:  # 0.1% chance of failure
            raise Exception("Random simulation failure!")
        await asyncio.sleep(0.001)

    return n
