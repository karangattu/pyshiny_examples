from shiny import reactive
from shiny.express import input, ui, render

# Page title and options
ui.page_opts(title="Checkbox Input Demo", fillable=True)

# Main app layout
with ui.layout_columns(width=1 / 2):
    # Basic checkbox
    ui.input_checkbox(id="basic_check", label="Basic checkbox", value=False)

    # Checkbox with initial value True
    ui.input_checkbox(id="checked_box", label="Pre-checked checkbox", value=True)

    # Checkbox with custom width
    ui.input_checkbox(
        id="wide_check",
        label="Checkbox with custom width (300px)",
        value=False,
        width="300px",
    )

    # Checkbox with full width
    ui.input_checkbox(
        id="full_width", label="Checkbox with 100% width", value=False, width="100%"
    )

# Display results section
with ui.card():
    ui.card_header("Checkbox States")

    @render.ui
    def checkbox_states():
        states = {
            "Basic Checkbox": input.basic_check(),
            "Pre-checked Checkbox": input.checked_box(),
            "Wide Checkbox": input.wide_check(),
            "Full Width Checkbox": input.full_width(),
        }

        result = ui.TagList()
        for name, state in states.items():
            result.append(
                ui.p(
                    f"{name}: ",
                    ui.span(
                        str(state),
                        style=f"color: {'green' if state else 'red'}; font-weight: bold;",
                    ),
                )
            )
        return result


# Add a section to demonstrate reactive updates
with ui.card():
    ui.card_header("Reactive Updates Demo")

    @render.text
    def total_checked():
        count = sum(
            [
                input.basic_check(),
                input.checked_box(),
                input.wide_check(),
                input.full_width(),
            ]
        )
        return f"Total number of checked boxes: {count}"
