import random

import pandas as pd
from shiny import App, Inputs, Outputs, Session, render, ui, reactive
from faker import Faker

fake = Faker()

# Generate some sample data

def generate_data():
    num_rows = random.randint(5, 10)
    mock_data = pd.DataFrame(
        {
            "Name": [fake.name() for _ in range(num_rows)],
            "Age": [fake.random_int(min=18, max=65) for _ in range(num_rows)],
            "Score": [fake.random_int(min=70, max=100) for _ in range(num_rows)],
            "Email": [fake.email() for _ in range(num_rows)],
            "Address": [fake.address() for _ in range(num_rows)],
            "Phone": [fake.phone_number() for _ in range(num_rows)],
        }
    )
    return mock_data

app_ui = ui.page_fluid(
    ui.tags.style(
        """
        .custom-card {
            background-color: #f2f2f2;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        }
        
        .custom-button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        
        .custom-table {
            width: 100%;
            border-collapse: collapse;
        }
        
        .custom-table th, .custom-table td {
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        
        .custom-table th {
            background-color: #4CAF50;
            color: white;
        }
        """,
        media="all",
    ),
    ui.card(
        ui.card_header("Data Summary"),
        ui.head_content(
            ui.HTML('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">')
        ),
        ui.layout_column_wrap(
            ui.value_box(
                "Total Entries",
                str(len(generate_data())),
                theme="bg-gradient-orange-red",
                showcase=ui.tags.i(
                    class_="fa-solid fa-chart-pie", style="font-size: 2rem;"
                ),
            ),
            ui.value_box(
                "Average Age",
                str(round(generate_data()["Age"].mean(), 2)),
                theme="text-green",
                showcase=ui.tags.i(
                    class_="fa-solid fa-people-arrows", style="font-size: 2rem;"
                ),
            ),
            ui.value_box(
                "Average Score",
                str(round(generate_data()["Score"].mean(), 2)),
                theme="purple",
                showcase=ui.tags.i(
                    class_="bi bi-trophy-fill", style="font-size: 2rem;"
                ),
            ),
            width=1 / 3,
        ),
        class_="custom-card",
    ),
    ui.card(
        ui.card_header("Data Table"),
        ui.output_table("data_table", class_="custom-table"),
        class_="custom-card",
    ),
    ui.input_action_button("refresh", "Refresh Data", class_="custom-button"),
)


def server(input: Inputs, output: Outputs, session: Session):
    data = reactive.Value(generate_data())

    @render.table
    def data_table():
        print("Rendering data table")
        return data.get()

    @reactive.effect
    @reactive.event(input.refresh)
    def refresh_data():
        # Refresh the data
        new_data = generate_data()
        data.set(new_data)


app = App(app_ui, server)