from shiny import reactive
from shiny.express import input, ui, render

ui.page_opts(title="Text Area Demo", fillable=True)

# Example of a basic text area with default settings
with ui.layout_column_wrap(width=1 / 2):
    with ui.card():
        ui.card_header("Basic Text Area")
        ui.input_text_area(
            id="text1",
            label="Default Text Area",
            value="This is some default text.\nIt can span multiple lines.",
            width="100%",
        )

    # Example with placeholder text and custom height
    with ui.card():
        ui.card_header("Text Area with Placeholder & Height")
        ui.input_text_area(
            id="text2",
            label="With Placeholder",
            value="",
            placeholder="Enter your text here...",
            height="150px",
            width="100%",
        )

    # Example with columns and rows specified
    with ui.card():
        ui.card_header("Text Area with Columns & Rows")
        ui.input_text_area(
            id="text3",
            label="Specified Dimensions",
            value="This text area has specific dimensions.",
            cols=40,
            rows=5,
            width="100%",
        )

    # Example with resize options
    with ui.card():
        ui.card_header("Text Area with Resize Options")
        ui.input_text_area(
            id="text4",
            label="Vertical Resize Only",
            value="This text area can only be resized vertically.",
            resize="vertical",
            width="100%",
        )

    # Example with autoresize
    with ui.card():
        ui.card_header("Auto-resizing Text Area")
        ui.input_text_area(
            id="text5",
            label="Auto-resize Enabled",
            value="This text area will automatically resize as you type more content.",
            autoresize=True,
            width="100%",
        )

    # Example with spellcheck and autocomplete
    with ui.card():
        ui.card_header("Text Area with Spellcheck & Autocomplete")
        ui.input_text_area(
            id="text6",
            label="Spellcheck & Autocomplete",
            value="This text area has spellchecking enabled.",
            spellcheck="true",
            autocomplete="on",
            width="100%",
        )

# Display the current values of all text areas
with ui.card():
    ui.card_header("Current Values")

    @render.ui
    def show_values():
        return ui.tags.div(
            ui.tags.h4("Text Area 1:"),
            ui.tags.pre(input.text1()),
            ui.tags.h4("Text Area 2:"),
            ui.tags.pre(input.text2()),
            ui.tags.h4("Text Area 3:"),
            ui.tags.pre(input.text3()),
            ui.tags.h4("Text Area 4:"),
            ui.tags.pre(input.text4()),
            ui.tags.h4("Text Area 5:"),
            ui.tags.pre(input.text5()),
            ui.tags.h4("Text Area 6:"),
            ui.tags.pre(input.text6()),
            class_="p-3",
        )


# Add a character count display for each text area
@render.ui
def char_counts():
    counts = {
        "Text Area 1": len(input.text1() or ""),
        "Text Area 2": len(input.text2() or ""),
        "Text Area 3": len(input.text3() or ""),
        "Text Area 4": len(input.text4() or ""),
        "Text Area 5": len(input.text5() or ""),
        "Text Area 6": len(input.text6() or ""),
    }

    return ui.tags.div(
        ui.tags.h3("Character Counts:"),
        *[ui.tags.p(f"{name}: {count} characters") for name, count in counts.items()],
        class_="p-3",
    )
