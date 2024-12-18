from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np

# Sample data
df = pd.DataFrame(
    {
        "date": pd.date_range(start="2024-01-01", periods=10),
        "value": np.random.randn(10),
        "category": np.random.choice(["A", "B", "C"], 10),
    }
)

ui.page_opts(title="Modal Demo", fillable=True)

# Add Font Awesome for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">'
    )
)

with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_action_button("show_simple", "Show Simple Modal", class_="mb-3")
        ui.input_action_button("show_large", "Show Large Modal", class_="mb-3")
        ui.input_action_button("show_small", "Show Small Modal", class_="mb-3")
        ui.input_action_button("show_footer", "Show Modal with Footer", class_="mb-3")
        ui.input_action_button("show_no_fade", "Show Modal without Fade", class_="mb-3")
        ui.input_action_button(
            "show_easy_close", "Show Easy Close Modal", class_="mb-3"
        )


@reactive.effect
@reactive.event(input.show_simple)
def show_simple_modal():
    m = ui.modal(
        "This is a basic modal with default settings",
        title="Simple Modal",
        easy_close=False,
        footer=None,
    )
    ui.modal_show(m)


@reactive.effect
@reactive.event(input.show_large)
def show_large_modal():
    m = ui.modal(
        ui.output_table("large_table"),
        title="Large Modal with Data",
        size="l",
        easy_close=False,
        footer=ui.modal_button("Close"),
    )
    ui.modal_show(m)


@reactive.effect
@reactive.event(input.show_small)
def show_small_modal():
    m = ui.modal(
        ui.tags.i(class_="fa-solid fa-check fa-4x text-success"),
        ui.tags.h4("Operation Successful!", class_="mt-3"),
        title="Small Modal",
        size="s",
        easy_close=False,
        footer=ui.modal_button("OK"),
    )
    ui.modal_show(m)


@reactive.effect
@reactive.event(input.show_footer)
def show_footer_modal():
    m = ui.modal(
        "This modal has custom footer buttons",
        title="Modal with Footer",
        footer=[
            ui.modal_button("Cancel", class_="btn-secondary"),
            ui.modal_button("Save", class_="btn-primary"),
        ],
    )
    ui.modal_show(m)


@reactive.effect
@reactive.event(input.show_no_fade)
def show_no_fade_modal():
    m = ui.modal(
        "This modal appears instantly without fade animation",
        title="No Fade Modal",
        fade=False,
        footer=ui.modal_button("Close"),
    )
    ui.modal_show(m)


@reactive.effect
@reactive.event(input.show_easy_close)
def show_easy_close_modal():
    m = ui.modal(
        "Click outside or press ESC to close this modal",
        title="Easy Close Modal",
        easy_close=True,
    )
    ui.modal_show(m)


# Render table for large modal
@render.table
def large_table():
    return df


# Main content area with instructions
with ui.card():
    ui.card_header("Modal Demo App")
    ui.markdown(
        """
    This app demonstrates different modal configurations:
    
    * **Simple Modal**: Basic modal with default settings
    * **Large Modal**: Shows a data table in a large modal
    * **Small Modal**: Compact modal with success message
    * **Modal with Footer**: Custom footer buttons
    * **No Fade Modal**: Modal without fade animation
    * **Easy Close Modal**: Can be closed by clicking outside or pressing ESC
    
    Click the buttons in the sidebar to see different modal types.
    """
    )
