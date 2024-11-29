from typing import Dict, List

from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Mock data for the function reference documentation
function_docs: List[Dict] = [
    {
        "File Name": "App",
        "Usage": "App(self, ui, server, *, static_assets=None, debug=False)",
        "Description": "Create a Shiny app instance.",
        "Parameters": "...",
        "Examples": "...",
    },
    {
        "File Name": "Htmltools",
        "Usage": "HTMLDependency(self, name, version, *, source=None, script=None, stylesheet=None, all_files=False, meta=None, head=None)",
        "Description": "Define an HTML dependency.",
        "Parameters": "...",
        "Examples": "...",
    },
    # Add more function reference documentation as needed
]

app_ui = ui.page_fluid(
    ui.panel_title("Shiny for Python Function Reference"),
    ui.layout_column_wrap(
        *[
            ui.value_box(
                doc["File Name"],
                doc["Usage"],
                doc["Description"],
                showcase=ui.HTML(f"<pre>{doc['Examples']}</pre>"),
                theme="bg-gradient-primary-secondary",
                full_screen=True,
            )
            for doc in function_docs
        ],
        width=1 / 2,
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    pass


app = App(app_ui, server)
