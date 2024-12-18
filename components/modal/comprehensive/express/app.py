from shiny import reactive
from shiny.express import input, ui, render

# Page options for styling
ui.page_opts(title="Modal Demo", fillable=True)

# Create some sample data
sample_data = {
    "title": "Sample Data Overview",
    "body": """
    This is a comprehensive demonstration of modal features in Shiny for Python.
    - Modals can be used to display important information
    - They can be customized in size and behavior
    - They support different types of content
    """,
}

# Different modal buttons for demonstration
with ui.layout_column_wrap(width=1 / 3):
    ui.input_action_button("show_small", "Show Small Modal", class_="btn-primary")
    ui.input_action_button("show_medium", "Show Medium Modal", class_="btn-info")
    ui.input_action_button("show_large", "Show Large Modal", class_="btn-success")
    ui.input_action_button("show_xl", "Show Extra Large Modal", class_="btn-warning")
    ui.input_action_button(
        "show_no_close", "Modal without Easy Close", class_="btn-danger"
    )
    ui.input_action_button("show_no_fade", "Modal without Fade", class_="btn-secondary")


# Small Modal
@reactive.effect
@reactive.event(input.show_small)
def show_small_modal():
    m = ui.modal(
        "This is a small modal dialog.",
        title="Small Modal",
        size="s",
        easy_close=True,
        footer=ui.modal_button("Close"),
    )
    ui.modal_show(m)


# Medium Modal
@reactive.effect
@reactive.event(input.show_medium)
def show_medium_modal():
    m = ui.modal(
        "This is a medium modal dialog with custom footer.",
        title="Medium Modal",
        size="m",
        footer=[
            ui.modal_button("Cancel", class_="btn-secondary"),
            ui.modal_button("OK", class_="btn-primary"),
        ],
    )
    ui.modal_show(m)


# Large Modal
@reactive.effect
@reactive.event(input.show_large)
def show_large_modal():
    with ui.hold() as modal_content:
        ui.h3("Large Modal with Dynamic Content")
        ui.input_text("modal_input", "Enter some text:")
        ui.input_numeric("modal_number", "Enter a number:", value=0)

        @render.text
        def modal_output():
            return f"You entered: {input.modal_input()} and {input.modal_number()}"

    m = ui.modal(
        modal_content, title="Large Interactive Modal", size="l", easy_close=True
    )
    ui.modal_show(m)


# Extra Large Modal
@reactive.effect
@reactive.event(input.show_xl)
def show_xl_modal():
    m = ui.modal(
        ui.HTML(
            f"""
            <h3>{sample_data['title']}</h3>
            <p>{sample_data['body']}</p>
            <hr>
            <div class="alert alert-info">
                This is an extra large modal with HTML content.
            </div>
        """
        ),
        title="Extra Large Modal",
        size="xl",
        footer=ui.modal_button("Got it!"),
    )
    ui.modal_show(m)


# Modal without Easy Close
@reactive.effect
@reactive.event(input.show_no_close)
def show_no_close_modal():
    m = ui.modal(
        "This modal can only be closed using the button below.",
        title="Modal without Easy Close",
        easy_close=False,
        footer=ui.modal_button("I understand", class_="btn-warning"),
    )
    ui.modal_show(m)


# Modal without Fade
@reactive.effect
@reactive.event(input.show_no_fade)
def show_no_fade_modal():
    m = ui.modal(
        "This modal appears instantly without fade animation.",
        title="Modal without Fade",
        fade=False,
        footer=ui.modal_button("Close"),
    )
    ui.modal_show(m)


# Main app content
ui.h2("Modal Component Demonstration")
ui.markdown(
    """
This app demonstrates all possible parameters of the Shiny modal component:

- **size**: 's' (small), 'm' (medium), 'l' (large), 'xl' (extra large)
- **easy_close**: True/False - whether clicking outside or pressing Escape closes the modal
- **fade**: True/False - whether to show fade animation
- **title**: Custom title for the modal
- **footer**: Custom footer content (buttons, text, etc.)
"""
)
