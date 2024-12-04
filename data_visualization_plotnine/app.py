import numpy as np
import pandas as pd
from plotnine import (aes, element_text, geom_line, geom_point, ggplot, theme,
                      xlim, ylim)
from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Sample data
np.random.seed(42)
data = pd.DataFrame(
    {
        "x": np.random.normal(0, 1, 100),
        "y": np.random.normal(0, 1, 100),
        "category": np.random.choice(["A", "B", "C"], 100),
    }
)

app_ui = ui.page_fluid(
    ui.panel_title("Shiny for Python Function Reference"),
    ui.layout_column_wrap(
        ui.value_box(
            "Function Reference",
            "Explore the Shiny for Python function reference",
            showcase=ui.HTML(
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" class="bi bi-book" style="fill:currentColor;height:100%;" aria-hidden="true" role="img"><path d="M1 2.828c.885-.37 2.154-.769 3.388-.893 1.33-.134 2.458.063 3.112.752v9.746c-.935-.53-2.12-.603-3.213-.493-1.18.12-2.37.461-3.287.811V2.828zm7.5-.141c.654-.689 1.782-.886 3.112-.752 1.234.124 2.503.523 3.388.893v9.923c-.918-.35-2.107-.692-3.287-.81-1.094-.111-2.278-.039-3.213.492V2.687zM8 1.783C7.015.936 5.587.81 4.287.94c-1.514.153-3.042.672-3.994 1.105A.5.5 0 0 0 0 2.5v11a.5.5 0 0 0 .707.455c.882-.4 2.303-.881 3.68-1.02 1.409-.142 2.59.087 3.223.877a.5.5 0 0 0 .78 0c.633-.79 1.814-1.019 3.222-.877 1.378.139 2.8.62 3.681 1.02A.5.5 0 0 0 16 13.5v-11a.5.5 0 0 0-.293-.455c-.952-.433-2.48-.952-3.994-1.105C10.413.809 8.985.936 8 1.783z"/></svg>'
            ),
            theme="bg-gradient-blue-purple",
            full_screen=True,
        ),
        ui.value_box(
            "Data Visualization",
            "Explore data using plotnine",
            showcase=ui.output_plot("plot"),
            theme="bg-gradient-orange-red",
            full_screen=True,
            showcase_layout="bottom",
            height="500px",
        ),
        ui.value_box(
            "Inputs",
            "Interact with the app",
            ui.input_select(
                "category", "Select Category", ["A", "B", "C"], selected="A"
            ),
            ui.input_slider("x_range", "X Range", -3, 3, value=(-2, 2)),
            ui.input_slider("y_range", "Y Range", -3, 3, value=(-2, 2)),
            theme="bg-gradient-green-teal",
            full_screen=True,
        ),
    ),
)


def server(input: Inputs, output: Outputs, session: Session):

    @render.plot
    def plot():
        category_data = data[data.category == input.category()]
        if category_data.empty:
            return "No data for selected category"

        p = (
            ggplot(data, aes(x="x", y="y", color="category"))
            + geom_point()
            + geom_line()
            + geom_point(data=category_data, size=3)
            + theme(
                text=element_text(size=12),
                legend_title=element_text(size=14),
                legend_text=element_text(size=12),
            )
            + theme(figure_size=(8, 6))
            + xlim(input.x_range()[0], input.x_range()[1])
            + ylim(input.y_range()[0], input.y_range()[1])
        )
        return p


app = App(app_ui, server)
