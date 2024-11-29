import numpy as np
import pandas as pd
from shiny import App, Inputs, Outputs, Session, render, ui

np.random.seed(0)  # For reproducibility

data = pd.DataFrame(
    {
        "Name": [
            "Emily Chen",
            "Michael Brown",
            "Sarah Lee",
            "David Kim",
            "Jennifer White",
            "Kevin Hall",
            "Lisa Nguyen",
            "Brian Martin",
            "Hannah Patel",
            "William Davis",
            "Olivia Taylor",
            "Richard Garcia",
            "Ava Brooks",
            "Charles Sanchez",
            "Mia Rodriguez",
            "Alexander Hernandez",
            "Isabella Lopez",
            "Ethan Walker",
            "Julia Russell",
            "Liam Jenkins",
        ],
        "Age": np.random.randint(25, 60, 20),
        "Salary": np.random.randint(40000, 120000, 20),
        "Department": np.random.choice(
            ["Sales", "Marketing", "IT", "HR", "Finance"], 20
        ),
    }
)

app_ui = ui.page_fluid(
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Data Table"),
            ui.output_data_frame("data_table"),
            width="100%",
            height="500px",
        )
    )
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.data_frame
    def data_table():
        return render.DataGrid(
            data,
            width="100%",
            height="100%",
            filters=True,
            editable=False,
            selection_mode="rows",
        )


app = App(app_ui, server)
