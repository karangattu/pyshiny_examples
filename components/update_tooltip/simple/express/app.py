from shiny import reactive
from shiny.express import input, render, ui

ui.page_opts(title="Tooltip Demo", fillable=True)

ui.input_action_button("btn_show", "Show tooltip", class_="mt-3 me-3")
ui.input_action_button("btn_close", "Close tooltip", class_="mt-3 me-3")
ui.input_action_button("btn_update", "Update tooltip content", class_="mt-3 me-3")

# Counter for dynamic tooltip content
counter = reactive.value(1)

with ui.tooltip(id="tooltip_id"):
    ui.input_action_button(
        "btn_w_tooltip",
        "Hover over me!",
        class_="mt-5 ms-3",
    )
    "Initial tooltip message"


@reactive.effect
@reactive.event(input.btn_show)
def _():
    ui.update_tooltip("tooltip_id", show=True)


@reactive.effect
@reactive.event(input.btn_close)
def _():
    ui.update_tooltip("tooltip_id", show=False)


@reactive.effect
@reactive.event(input.btn_update)
def _():
    counter.set(counter.get() + 1)
    content = f"Tooltip content updated {counter.get()} times!"
    ui.update_tooltip("tooltip_id", content, show=True)


@reactive.effect
@reactive.event(input.btn_w_tooltip)
def _():
    ui.notification_show("Button clicked!", duration=1)
