import random
from typing import List, Tuple

from shiny import App, Inputs, Outputs, Session, render, ui

# Define some sample data
function_data: List[Tuple[str, str, str]] = [
    (
        "App",
        "App(self, ui, server, *, static_assets=None, debug=False)",
        "Create a Shiny app instance.",
    ),
    (
        "HTMLDependency",
        "HTMLDependency(self, name, version, *, source=None, script=None, stylesheet=None, all_files=False, meta=None, head=None)",
        "Define an HTML dependency.",
    ),
    (
        "reactive.calc",
        "reactive.Calc(fn=None, *, session=MISSING)",
        "Mark a function as a reactive calculation.",
    ),
    (
        "reactive.effect",
        "reactive.Effect(fn=None, *, suspended=False, priority=0, session=MISSING)",
        "Mark a function as a reactive side effect.",
    ),
    (
        "reactive.event",
        "reactive.event(*args, ignore_none=True, ignore_init=False)",
        'Mark a function to react only when an "event" occurs.',
    ),
]

app_ui = ui.page_fluid(
    ui.row(
        ui.column(4, ui.markdown("## Shiny for Python Function Reference")),
        ui.column(8, ui.output_text_verbatim("function_details")),
    ),
    ui.row(
        ui.column(
            4,
            ui.input_select(
                "function_select", "Select a function", [f[0] for f in function_data]
            ),
        ),
        ui.column(8, ui.output_text_verbatim("function_description")),
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.text
    def function_details():
        selected_function = next(
            (f for f in function_data if f[0] == input.function_select()), None
        )
        if selected_function:
            return f"""
**{selected_function[0]}**
{selected_function[1]}
{selected_function[2]}
"""
        else:
            return "No function selected."

    @render.text
    def function_description():
        selected_function = next(
            (f for f in function_data if f[0] == input.function_select()), None
        )
        if selected_function:
            return selected_function[2]
        else:
            return "No function selected."


app = App(app_ui, server)
