from shiny import reactive
from shiny.express import input, ui, render

# Simple app showing update_action_button usage
ui.page_opts(title="Update Action Button Demo")

with ui.sidebar():
    ui.input_action_button("btn1", "Click me!", class_="btn-primary")
    ui.input_action_button("btn2", "Disabled button", disabled=True)
    ui.input_action_button("btn3", "Change label & icon")

click_count = reactive.value(0)


@reactive.effect
@reactive.event(input.btn1)
def _():
    click_count.set(click_count.get() + 1)
    # Enable btn2 after 3 clicks of btn1
    if click_count.get() >= 3:
        ui.update_action_button(
            "btn2", disabled=False, label=f"Enabled after {click_count.get()} clicks!"
        )


@reactive.effect
@reactive.event(input.btn3)
def _():
    # Update button label and add/change icon
    new_label = f"Changed {input.btn3()} times!"
    new_icon = ui.tags.i(class_="fa-solid fa-arrows-rotate")
    ui.update_action_button("btn3", label=new_label, icon=new_icon)


@render.text
def show_clicks():
    return f"Button 1 clicked {click_count.get()} times"
