from shiny import reactive
from shiny.express import input, ui, render

ui.page_opts(title="Modal Remove Example", fillable=True)

ui.h2("Modal Remove Example")

ui.input_action_button("show", "Show Modal")
ui.input_action_button("remove", "Remove Modal")


@reactive.effect
@reactive.event(input.show)
def _():
    m = ui.modal(
        "This is a modal message that can be removed programmatically.",
        title="Important Message",
        easy_close=False,
        footer=ui.modal_button("Close"),
    )
    ui.modal_show(m)


@reactive.effect
@reactive.event(input.remove)
def _():
    ui.modal_remove()


@render.text
def msg():
    return "Click 'Show Modal' to display a modal dialog. Click 'Remove Modal' to remove it programmatically."
