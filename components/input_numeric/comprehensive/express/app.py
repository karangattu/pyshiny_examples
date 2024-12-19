from shiny import reactive
from shiny.express import input, ui, render

# Set page options
ui.page_opts(title="Numeric Input Demo", fillable=True)

# Create a sidebar layout
with ui.layout_sidebar():
    with ui.sidebar():
        # Basic numeric input
        ui.input_numeric(id="basic", label="Basic numeric input", value=10)

        # Numeric input with min/max constraints
        ui.input_numeric(
            id="constrained",
            label="Constrained numeric input (0-100)",
            value=50,
            min=0,
            max=100,
        )

        # Numeric input with step size
        ui.input_numeric(
            id="stepped",
            label="Stepped numeric input (step=5)",
            value=15,
            min=0,
            max=100,
            step=5,
        )

        # Numeric input with custom width
        ui.input_numeric(
            id="custom_width",
            label="Custom width numeric input",
            value=25,
            width="150px",
        )

    # Main panel with reactive outputs
    with ui.card():
        ui.card_header("Current Values")

        @render.ui
        def show_values():
            return ui.tags.div(
                ui.tags.p(ui.tags.strong("Basic Input: "), str(input.basic())),
                ui.tags.p(
                    ui.tags.strong("Constrained Input (0-100): "),
                    str(input.constrained()),
                ),
                ui.tags.p(
                    ui.tags.strong("Stepped Input (step=5): "), str(input.stepped())
                ),
                ui.tags.p(
                    ui.tags.strong("Custom Width Input: "), str(input.custom_width())
                ),
            )

    # Card showing calculations with the inputs
    with ui.card():
        ui.card_header("Calculations")

        @render.ui
        def show_calculations():
            return ui.tags.div(
                ui.tags.p(
                    ui.tags.strong("Sum of all inputs: "),
                    str(
                        input.basic()
                        + input.constrained()
                        + input.stepped()
                        + input.custom_width()
                    ),
                ),
                ui.tags.p(
                    ui.tags.strong("Average of all inputs: "),
                    str(
                        round(
                            (
                                input.basic()
                                + input.constrained()
                                + input.stepped()
                                + input.custom_width()
                            )
                            / 4,
                            2,
                        )
                    ),
                ),
            )

    # Card showing validation status
    with ui.card():
        ui.card_header("Input Validation Status")

        @render.ui
        def show_validation():
            messages = []

            # Check basic input
            if input.basic() is None:
                messages.append("Basic input is empty")

            # Check constrained input
            if input.constrained() is None:
                messages.append("Constrained input is empty")
            elif input.constrained() < 0 or input.constrained() > 100:
                messages.append("Constrained input is out of range (0-100)")

            # Check stepped input
            if input.stepped() is None:
                messages.append("Stepped input is empty")
            elif input.stepped() % 5 != 0:
                messages.append("Stepped input is not a multiple of 5")

            # Check custom width input
            if input.custom_width() is None:
                messages.append("Custom width input is empty")

            if not messages:
                return ui.tags.p("All inputs are valid!", style="color: green;")
            else:
                return ui.tags.div(
                    ui.tags.p("Validation issues:", style="color: red;"),
                    ui.tags.ul([ui.tags.li(msg) for msg in messages]),
                )
