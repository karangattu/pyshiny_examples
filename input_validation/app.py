from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui

# Made-up data
FUNCTION_DATA = [
    {
        "File Name": "App",
        "Usage": "App(self, ui, server, *, static_assets=None, debug=False)",
        "Description": "Create a Shiny app instance.",
        "Parameters": "**ui**: Defines the user interface of the app.\n**server**:  A function that defines the server-side logic of the app.\n**static_assets**: Specifies the path to static assets like CSS or images.\n**debug**: Enables debug mode for more detailed error messages.",
        "Examples": "```python\napp_ui = ui.page_fluid(ui.h1('Hello Shiny!'))\n\ndef server(input, output, session):\n    pass\n\napp = App(app_ui, server)\n```",
    },
    {
        "File Name": "Htmltools",
        "Usage": "HTMLDependency(self, name, version, *, source=None, script=None, stylesheet=None, all_files=False, meta=None, head=None)",
        "Description": "Define an HTML dependency. This is useful for including external CSS, JavaScript, or other web resources in your Shiny app.",
        "Parameters": "**name**: The name of the dependency.\n**version**: The version of the dependency.\n**source**: A dictionary or string specifying the source of the dependency (e.g., a local directory or a URL).\n**script**:  A list of dictionaries or strings specifying JavaScript files to include.\n**stylesheet**: A list of dictionaries or strings specifying CSS files to include.\n**all_files**: If `True`, includes all files in the source directory.\n**meta**:  A list of dictionaries specifying meta tags to include.\n**head**:  A string of HTML to be included in the head section.",
        "Examples": "```python\njquery_dep = ui.HTMLDependency(\n    name='jquery',\n    version='3.5.1',\n    source={'href': 'https://code.jquery.com/', 'integrity': 'sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0='},\n    script={'src': 'jquery-3.5.1.min.js'}\n)\n\napp_ui = ui.page_fluid(\n   jquery_dep,\n   ui.h1('Shiny with jQuery')\n)\n```",
    },
    {
        "File Name": "ui.page_fluid",
        "Usage": "ui.page_fluid(*args, title=None, theme=None, lang=None, head_content=None, **kwargs)",
        "Description": "Creates a fluid page layout. This is a common layout for Shiny apps, where content is arranged in rows that automatically adjust to the width of the browser window.",
        "Parameters": "**\\*args**:  UI elements to include in the page.\n**title**: The title of the page.\n**theme**: A Shiny theme object or a path to a CSS file.\n**lang**: The language of the page.\n**head_content**:  Additional content to include in the head section.\n**\\*\\*kwargs**:  Additional attributes to apply to the page container.",
        "Examples": "```python\napp_ui = ui.page_fluid(\n    ui.h1('My Shiny App'),\n    ui.input_text('name', 'Enter your name:'),\n    ui.output_text('greeting')\n)\n```",
    },
    {
        "File Name": "ui.input_text",
        "Usage": "ui.input_text(id, label, value='', placeholder=None, width=None)",
        "Description": "Creates a text input control.",
        "Parameters": "**id**: The ID of the input control. This is used to access the input value in the server function.\n**label**: The label to display next to the input control.\n**value**: The initial value of the input control.\n**placeholder**: The placeholder text to display in the input control when it is empty.\n**width**: The width of the input control.",
        "Examples": "```python\nui.input_text('name', 'Enter your name:', value='John Doe')\n```",
    },
    {
        "File Name": "ui.input_action_button",
        "Usage": "ui.input_action_button(id, label, icon=None, width=None)",
        "Description": "Creates an action button.",
        "Parameters": "**id**: The ID of the button. This is used to trigger events in the server function.\n**label**: The label to display on the button.\n**icon**: An optional icon to display on the button.\n**width**: The width of the button.",
        "Examples": "```python\nui.input_action_button('submit', 'Submit')\n```",
    },
    {
        "File Name": "ui.output_ui",
        "Usage": "ui.output_ui(id)",
        "Description": "Creates a placeholder for dynamic UI elements.",
        "Parameters": "**id**: The ID of the output UI element. This is used to update the UI element in the server function.",
        "Examples": "```python\nui.output_ui('greeting')\n```",
    },
    {
        "File Name": "ui.TagList",
        "Usage": "ui.TagList(*args)",
        "Description": "Creates a list of HTML tags.",
        "Parameters": "**\\*args**: The HTML tags to include in the list.",
        "Examples": "```python\nui.TagList(\n    ui.h1('Hello Shiny!'),\n    ui.p('Welcome to my app.')\n)\n```",
    },
    {
        "File Name": "ui.h2",
        "Usage": "ui.h2(text)",
        "Description": "Creates a level 2 heading.",
        "Parameters": "**text**: The text to display in the heading.",
        "Examples": "```python\nui.h2('Section Title')\n```",
    },
    {
        "File Name": "ui.markdown",
        "Usage": "ui.markdown(text)",
        "Description": "Creates a Markdown block.",
        "Parameters": "**text**: The Markdown text to display.",
        "Examples": "```python\nui.markdown('**Hello Shiny!**')\n```",
    },
    {
        "File Name": "ui.p",
        "Usage": "ui.p(text)",
        "Description": "Creates a paragraph element.",
        "Parameters": "**text**: The text to display in the paragraph.",
        "Examples": "```python\nui.p('This is a paragraph.')\n```",
    },
    {
        "File Name": "ui.HTMLDependency",
        "Usage": "ui.HTMLDependency(name, version, *, source=None, script=None, stylesheet=None, all_files=False, meta=None, head=None)",
        "Description": "Define an HTML dependency. This is useful for including external CSS, JavaScript, or other web resources in your Shiny app.",
        "Parameters": "**name**: The name of the dependency.\n**version**: The version of the dependency.\n**source**: A dictionary or string specifying the source of the dependency (e.g., a local directory or a URL).\n**script**:  A list of dictionaries or strings specifying JavaScript files to include.\n**stylesheet**: A list of dictionaries or strings specifying CSS files to include.\n**all_files**: If `True`, includes all files in the source directory.\n**meta**:  A list of dictionaries specifying meta tags to include.\n**head**:  A string of HTML to be included in the head section.",
        "Examples": "```python\njquery_dep = ui.HTMLDependency(\n    name='jquery',\n    version='3.5.1',\n    source={'href': 'https://code.jquery.com/', 'integrity': 'sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0='},\n    script={'src': 'jquery-3.5.1.min.js'}\n)\n```",
    },
    {
        "File Name": "ui.h1",
        "Usage": "ui.h1(text)",
        "Description": "Creates a level 1 heading.",
        "Parameters": "**text**: The text to display in the heading.",
        "Examples": "```python\nui.h1('Hello Shiny!')\n```",
    },
    {
        "File Name": "ui.input_checkbox",
        "Usage": "ui.input_checkbox(id, label, value=False)",
        "Description": "Creates a checkbox input control.",
        "Parameters": "**id**: The ID of the input control. This is used to access the input value in the server function.\n**label**: The label to display next to the checkbox.\n**value**: The initial value of the checkbox.",
        "Examples": "```python\nui.input_checkbox('agree', 'I agree to the terms and conditions')\n```",
    },
    {
        "File Name": "ui.output_text",
        "Usage": "ui.output_text(id, value='')",
        "Description": "Creates a text output element.",
        "Parameters": "**id**: The ID of the output element. This is used to update the output in the server function.\n**value**: The initial value of the output element.",
        "Examples": "```python\nui.output_text('greeting', value='Hello, world!')\n```",
    },
    {
        "File Name": "ui.input_radio",
        "Usage": "ui.input_radio(id, label, choices, selected=None)",
        "Description": "Creates a radio button input control.",
        "Parameters": "**id**: The ID of the input control. This is used to access the input value in the server function.\n**label**: The label to display next to the radio buttons.\n**choices**: A list of dictionaries specifying the radio button choices.\n**selected**: The initial selected choice.",
        "Examples": "```python\nui.input_radio('color', 'Select a color:', [{'label': 'Red', 'value': 'red'}, {'label': 'Blue', 'value': 'blue'}])\n```",
    },
    {
        "File Name": "ui.input_select",
        "Usage": "ui.input_select(id, label, choices, selected=None)",
        "Description": "Creates a select input control.",
        "Parameters": "**id**: The ID of the input control. This is used to access the input value in the server function.\n**label**: The label to display next to the select control.\n**choices**: A list of dictionaries specifying the select options.\n**selected**: The initial selected option.",
        "Examples": "```python\nui.input_select('color', 'Select a color:', [{'label': 'Red', 'value': 'red'}, {'label': 'Blue', 'value': 'blue'}])\n```",
    },
    {
        "File Name": "ui.input_slider",
        "Usage": "ui.input_slider(id, label, min=0, max=100, value=50, step=1, format=None)",
        "Description": "Creates a slider input control.",
        "Parameters": "**id**: The ID of the input control. This is used to access the input value in the server function.\n**label**: The label to display next to the slider.\n**min**: The minimum value of the slider.\n**max**: The maximum value of the slider.\n**value**: The initial value of the slider.\n**step**: The step size of the slider.\n**format**: A format string to display the value.",
        "Examples": "```python\nui.input_slider('age', 'Select your age:', min=18, max=100, value=30, step=1)\n```",
    },
    {
        "File Name": "ui.input_textarea",
        "Usage": "ui.input_textarea(id, label, value='', placeholder=None, rows=3)",
        "Description": "Creates a textarea input control.",
        "Parameters": "**id**: The ID of the input control. This is used to access the input value in the server function.\n**label**: The label to display above the textarea.\n**value**: The initial value of the textarea.\n**placeholder**: The placeholder text to display in the textarea when it is empty.\n**rows**: The number of rows in the textarea.",
        "Examples": "```python\nui.input_textarea('comments', 'Enter your comments:', placeholder='Type here...', rows=5)\n```",
    },
    {
        "File Name": "ui.output_html",
        "Usage": "ui.output_html(id, value='')",
        "Description": "Creates an HTML output element.",
        "Parameters": "**id**: The ID of the output element. This is used to update the output in the server function.\n**value**: The initial value of the output element.",
        "Examples": "```python\nui.output_html('html_output', value='<h1>Hello, world!</h1>')\n```",
    },
    {
        "File Name": "ui.output_image",
        "Usage": "ui.output_image(id, src, alt='', width=None, height=None)",
        "Description": "Creates an image output element.",
        "Parameters": "**id**: The ID of the output element. This is used to update the output in the server function.\n**src**: The URL or path to the image file.\n**alt**: The alternative text for the image.\n**width**: The width of the image.\n**height**: The height of the image.",
        "Examples": "```python\nui.output_image('logo', 'logo.png', alt='Logo', width=100, height=100)\n```",
    },
    {
        "File Name": "ui.output_textarea",
        "Usage": "ui.output_textarea(id, value='', rows=3)",
        "Description": "Creates a textarea output element.",
        "Parameters": "**id**: The ID of the output element. This is used to update the output in the server function.\n**value**: The initial value of the output element.\n**rows**: The number of rows in the textarea.",
        "Examples": "```python\nui.output_textarea('comments', value='This is a comment.', rows=5)\n```",
    },
    {
        "File Name": "ui.output_verbatim",
        "Usage": "ui.output_verbatim(id, value='')",
        "Description": "Creates a verbatim output element.",
        "Parameters": "**id**: The ID of the output element. This is used to update the output in the server function.\n**value**: The initial value of the output element.",
        "Examples": "```python\nui.output_verbatim('output', value='This is verbatim text.')\n```",
    },
    # Add more function data as needed
]

app_ui = ui.page_fluid(
    ui.input_text(
        "function_name",
        "Enter a function name:",
        placeholder="e.g., App, Htmltools, ui.page_fluid",
    ),
    ui.input_action_button("search", "Search"),
    ui.output_ui("function_info"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.ui
    @reactive.event(input.search)
    def function_info():
        function_name = input.function_name().strip()
        req(function_name, "Please enter a function name.")

        for function_data in FUNCTION_DATA:
            if function_data["File Name"].lower() == function_name.lower():
                return ui.TagList(
                    ui.h2(function_data["File Name"]),
                    ui.markdown(
                        f"**Usage:**\n```python\n{function_data['Usage']}\n```\n"
                    ),
                    ui.markdown(f"**Description:**\n{function_data['Description']}\n"),
                    ui.markdown(f"**Parameters:**\n{function_data['Parameters']}\n"),
                    ui.markdown(f"**Examples:**\n{function_data['Examples']}\n"),
                )
        return ui.p("No matching functions found.")


app = App(app_ui, server)
