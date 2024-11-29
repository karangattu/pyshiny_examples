import random

import pandas as pd
from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Generate some sample data
data = {
    "Name": ["John", "Jane", "Bob", "Alice", "Tom"],
    "Age": [30, 25, 35, 28, 40],
    "Score": [85, 92, 78, 88, 90],
}
df = pd.DataFrame(data)

app_ui = ui.page_fluid(
    ui.panel_title("Shiny for Python App"),
    ui.layout_column_wrap(
        ui.value_box(
            "Average Score",
            str(round(df["Score"].mean(), 2)),
            "Based on the data",
            showcase=ui.HTML(
                '<i class="bi bi-bar-chart-fill" style="font-size: 2rem;"></i>'
            ),
            theme="bg-gradient-primary",
            class_="mb-4",
        ),
        ui.value_box(
            "Highest Score",
            str(df["Score"].max()),
            "Top performer",
            showcase=ui.HTML(
                '<i class="bi bi-trophy-fill" style="font-size: 2rem;"></i>'
            ),
            theme="bg-gradient-success",
            class_="mb-4",
        ),
        ui.value_box(
            "Lowest Score",
            str(df["Score"].min()),
            "Needs improvement",
            showcase=ui.HTML(
                '<i class="bi bi-emoji-frown-fill" style="font-size: 2rem;"></i>'
            ),
            theme="bg-gradient-danger",
            class_="mb-4",
        ),
        width=1 / 3,
    ),
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Data Table"),
            ui.output_data_frame("data_table"),
            class_="mb-4",
        ),
        ui.card(
            ui.card_header("Data Summary"),
            ui.output_text_verbatim("data_summary"),
            class_="mb-4",
        ),
        width=1,
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.data_frame
    def data_table():
        return df

    @render.text
    def data_summary():
        return f"""
        Number of Rows: {len(df)}
        Number of Columns: {len(df.columns)}
        """


app = App(app_ui, server)
