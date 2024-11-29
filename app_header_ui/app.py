import random

from shiny import App, Inputs, Outputs, Session, render, ui

# Make up some data
functions = [
    {
        "File Name": "App",
        "Usage": "App(self, ui, server, *, static_assets=None, debug=False)",
        "Description": "Create a Shiny app instance.",
        "Parameters": "\n<code>[**ui**]{.parameter-name} [:]{.parameter-annotation-sep} [[Tag](`htmltools.Tag`) \\| [TagList](`htmltools.TagList`) \\| [Callable](`typing.Callable`)\\[\\[[Request](`starlette.requests.Request`)\\], [Tag](`htmltools.Tag`) \\| [TagList](`htmltools.TagList`)\\] \\| [Path](`pathlib.Path`)]{.parameter-annotation}</code>\n\n:   The UI definition for the app (e.g., a call to [](:func:`~shiny.ui.page_fluid`) or similar, with layouts and controls nested inside). You can also pass a function that takes a [](:class:`~starlette.requests.Request`) and returns a UI definition, if you need the UI definition to be created dynamically for each pageview.\n\n<code>[**server**]{.parameter-name} [:]{.parameter-annotation-sep} [[Callable](`typing.Callable`)\\[\\[[Inputs](`shiny.session._session.Inputs`)\\], None\\] \\| [Callable](`typing.Callable`)\\[\\[[Inputs](`shiny.session._session.Inputs`), [Outputs](`shiny.session._session.Outputs`), [Session](`shiny.session._session.Session`)\\], None\\] \\| None]{.parameter-annotation}</code>\n\n:   A function which is called once for each session, ensuring that each session is independent.\n\n<code>[**static_assets**]{.parameter-name} [:]{.parameter-annotation-sep} [[Optional](`typing.Optional`)\\[[str](`str`) \\| [Path](`pathlib.Path`) \\| [Mapping](`typing.Mapping`)\\[[str](`str`), [str](`str`) \\| [Path](`pathlib.Path`)\\]\\]]{.parameter-annotation} [ = ]{.parameter-default-sep} [None]{.parameter-default}</code>\n\n:   Static files to be served by the app. If this is a string or Path object, it must be a directory, and it will be mounted at `/`. If this is a dictionary, each key is a mount point and each value is a file or directory to be served at that mount point.\n\n<code>[**debug**]{.parameter-name} [:]{.parameter-annotation-sep} [[bool](`bool`)]{.parameter-annotation} [ = ]{.parameter-default-sep} [False]{.parameter-default}</code>\n\n:   Whether to enable debug mode.\n",
        "Examples": 'from shiny import  App, Inputs, Outputs, Session, ui\n\napp_ui = ui.page_fluid("Hello Shiny!")\n\ndef server(input: Inputs, output: Outputs, session: Session):\n    pass\n\napp = App(app_ui, server)\n',
    },
    {
        "File Name": "Htmltools",
        "Usage": "HTMLDependency(\n    self,\n    name,\n    version,\n    *,\n    source=None,\n    script=None,\n    stylesheet=None,\n    all_files=False,\n    meta=None,\n    head=None,\n)",
        "Description": "Define an HTML dependency.",
        "Parameters": "\n<code>[**name**]{.parameter-name} [:]{.parameter-annotation-sep} [[str](`str`)]{.parameter-annotation}</code>\n\n:   Library name.\n\n<code>[**version**]{.parameter-name} [:]{.parameter-annotation-sep} [[str](`str`) \\| [Version](`packaging.version.Version`)]{.parameter-annotation}</code>\n\n:   Library version.\n\n<code>[**source**]{.parameter-name} [:]{.parameter-annotation-sep} [[Optional](`typing.Optional`)\\[[HTMLDependencySource](`htmltools._core.HTMLDependencySource`) \\| [HTMLDependencyUrl](`htmltools._core.HTMLDependencyUrl`)\\]]{.parameter-annotation} [ = ]{.parameter-default-sep} [None]{.parameter-default}</code>\n\n:   A specification for the location of dependency files.\n\n<code>[**script**]{.parameter-name} [:]{.parameter-annotation-sep} [[Optional](`typing.Optional`)\\[[ScriptItem](`htmltools._core.ScriptItem`) \\| [list](`list`)\\[[ScriptItem](`htmltools._core.ScriptItem`)\\]\\]]{.parameter-annotation} [ = ]{.parameter-default-sep} [None]{.parameter-default}</code>\n\n:   ``<script>`` tags to include in the document's ``<head>``. Each tag definition should include at least the ``src`` attribute (which should be file path relative to the ``source`` file location).\n\n<code>[**stylesheet**]{.parameter-name} [:]{.parameter-annotation-sep} [[Optional](`typing.Optional`)\\[[StylesheetItem](`htmltools._core.StylesheetItem`) \\| [list](`list`)\\[[StylesheetItem](`htmltools._core.StylesheetItem`)\\]\\]]{.parameter-annotation} [ = ]{.parameter-default-sep} [None]{.parameter-default}</code>\n\n:   ``<link>`` tags to include in the document's ``<head>``. Each tag definition should include at least the ``href`` attribute (which should be file path relative to the ``source`` file location).\n\n<code>[**all_files**]{.parameter-name} [:]{.parameter-annotation-sep} [[bool](`bool`)]{.parameter-annotation} [ = ]{.parameter-default-sep} [False]{.parameter-default}</code>\n\n:   Whether all files under the ``source`` directory are dependency files. If ``False``, only the files specified in script and stylesheet are treated as dependency files.\n\n<code>[**meta**]{.parameter-name} [:]{.parameter-annotation-sep} [[Optional](`typing.Optional`)\\[[MetaItem](`htmltools._core.MetaItem`) \\| [list](`list`)\\[[MetaItem](`htmltools._core.MetaItem`)\\]\\]]{.parameter-annotation} [ = ]{.parameter-default-sep} [None]{.parameter-default}</code>\n\n:   ``<meta>`` tags to include in the document's ``<head>``.\n\n<code>[**head**]{.parameter-name} [:]{.parameter-annotation-sep} [[TagChild](`htmltools._core.TagChild`)]{.parameter-annotation} [ = ]{.parameter-default-sep} [None]{.parameter-default}</code>\n\n:   Tags to include in the document's ``<head>``.\n",
        "Examples": '>>> dep = HTMLDependency(\n        name="mypackage",\n        version="1.0",\n        source={\n            "package": "mypackage",\n            "subdir": "lib/",\n        },\n        script={"src": "foo.js"},\n        stylesheet={"href": "css/foo.css"},\n    )\n\n>>> x = div("Hello", dep)\n>>> x.render()\n',
    },
]

app_ui = ui.page_fluid(
    ui.panel_title("Shiny for Python Function Reference"),
    ui.markdown(
        "This app showcases the function reference documentation for Shiny for Python."
    ),
    ui.layout_column_wrap(
        *[
            ui.card(
                ui.card_header(f["File Name"]),
                ui.markdown(f["Description"]),
                ui.markdown(f"**Usage:** `{f['Usage']}`"),
                ui.markdown("**Parameters:**"),
                ui.markdown(f["Parameters"]),
                ui.markdown("**Examples:**"),
                ui.markdown(f["Examples"]),
                width=1 / 2,
            )
            for f in functions
        ]
    ),
)


def server(input, output, session):
    pass


app = App(app_ui, server)
