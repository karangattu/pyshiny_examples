from shiny import reactive
from shiny.express import input, ui, render

# Add Font Awesome to use icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
    )
)

ui.page_opts(title="Task Button Demo", fillable=True)

with ui.layout_columns(width=1 / 2):
    # Basic task button with default parameters
    ui.input_task_button(
        id="basic_task",
        label="Basic Task",
    )

    # Task button with custom icon
    ui.input_task_button(
        id="icon_task",
        label="Task with Icon",
        icon=ui.tags.i(class_="fa-solid fa-rocket", style="font-size: 1.2rem;"),
    )

    # Task button with custom busy label
    ui.input_task_button(
        id="busy_label_task",
        label="Custom Busy Label",
        label_busy="Processing... Please Wait...",
    )

    # Task button with custom busy icon
    ui.input_task_button(
        id="busy_icon_task",
        label="Custom Busy Icon",
        icon=ui.tags.i(class_="fa-solid fa-play"),
        icon_busy=ui.tags.i(class_="fa-solid fa-spinner fa-spin"),
    )

    # Task button with custom width
    ui.input_task_button(id="width_task", label="Wide Button", width="100%")

    # Task button with custom type (changes color)
    ui.input_task_button(id="type_task", label="Danger Type", type="danger")

    # Task button that doesn't auto-reset
    ui.input_task_button(id="no_reset_task", label="No Auto Reset", auto_reset=False)

# Results display area
with ui.card():
    ui.card_header("Task Results")

    @render.text
    def task_status():
        clicks = {
            "basic": input.basic_task(),
            "icon": input.icon_task(),
            "busy_label": input.busy_label_task(),
            "busy_icon": input.busy_icon_task(),
            "width": input.width_task(),
            "type": input.type_task(),
            "no_reset": input.no_reset_task(),
        }
        return "\n".join([f"{k}: {v} clicks" for k, v in clicks.items()])


# Handle the tasks
@reactive.effect
@reactive.event(input.basic_task)
async def handle_basic():
    import asyncio

    await asyncio.sleep(2)  # Simulate work


@reactive.effect
@reactive.event(input.icon_task)
async def handle_icon():
    import asyncio

    await asyncio.sleep(3)  # Simulate work


@reactive.effect
@reactive.event(input.busy_label_task)
async def handle_busy_label():
    import asyncio

    await asyncio.sleep(4)  # Simulate work


@reactive.effect
@reactive.event(input.busy_icon_task)
async def handle_busy_icon():
    import asyncio

    await asyncio.sleep(2)  # Simulate work


@reactive.effect
@reactive.event(input.width_task)
async def handle_width():
    import asyncio

    await asyncio.sleep(2)  # Simulate work


@reactive.effect
@reactive.event(input.type_task)
async def handle_type():
    import asyncio

    await asyncio.sleep(2)  # Simulate work


@reactive.effect
@reactive.event(input.no_reset_task)
async def handle_no_reset():
    import asyncio

    await asyncio.sleep(2)  # Simulate work
    # Manually reset the button after 2 more seconds
    await asyncio.sleep(2)
    ui.update_task_button("no_reset_task", state="ready")
