import numpy as np
import pandas as pd
from shiny import App, Inputs, Outputs, Session, render, ui

# Generate some sample data
np.random.seed(42)
data = pd.DataFrame(
    {
        "A": np.random.normal(0, 1, 100),
        "B": np.random.poisson(3, 100),
        "C": np.random.randint(1, 11, 100),
    }
)

app_ui = ui.page_fluid(
    ui.panel_title("Summary Statistics"),
    ui.layout_column_wrap(
        ui.value_box("Rows", str(data.shape[0]), theme="bg-gradient-blue-green"),
        ui.value_box("Columns", str(data.shape[1]), theme="bg-gradient-orange-red"),
        ui.card(ui.card_header("Summary Statistics"), ui.output_table("summary")),
        width=1 / 2,
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.table
    def summary():
        return data.describe().T.reset_index()


app = App(app_ui, server)
