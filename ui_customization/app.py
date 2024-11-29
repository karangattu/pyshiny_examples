import random

from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Sample data
sample_data = [
    {"name": "Function 1", "description": "This is the description for Function 1."},
    {"name": "Function 2", "description": "This is the description for Function 2."},
    {"name": "Function 3", "description": "This is the description for Function 3."},
    {"name": "Function 4", "description": "This is the description for Function 4."},
    {"name": "Function 5", "description": "This is the description for Function 5."},
]

app_ui = ui.page_fluid(
    ui.tags.head(
        ui.tags.style(
            """
            .function-card {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 20px;
                margin-bottom: 20px;
            }
            .function-card h3 {
                margin-top: 0;
            }
            """
        )
    ),
    ui.row(
        ui.column(
            4,
            ui.input_select(
                "function_select", "Select a function", [d["name"] for d in sample_data]
            ),
        ),
        ui.column(8, ui.output_ui("function_details")),
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.ui
    def function_details():
        selected_function = next(
            (d for d in sample_data if d["name"] == input.function_select()), None
        )
        if selected_function:
            random_image_url = f"https://picsum.photos/200/{random.randint(300, 500)}"
            return ui.div(
                {"class": "function-card"},
                ui.h3(selected_function["name"]),
                ui.p(selected_function["description"]),
                ui.tags.img(
                    src=random_image_url,
                    width="100%",
                    height="200px",
                    style="border-radius: 5px; object-fit: cover;",
                ),
            )
        else:
            return ui.p("No function selected.")


app = App(app_ui, server)
