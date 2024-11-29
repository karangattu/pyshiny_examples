import random
from pathlib import Path

import pandas as pd
from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# --- UI Configuration ---
FONT_AWESOME_LINK = (
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
)

# --- Data Generation ---
nutrients = [
    "Calories",
    "Total Fat",
    "Saturated Fat",
    "Cholesterol",
    "Sodium",
    "Total Carbohydrates",
    "Dietary Fiber",
    "Sugars",
    "Protein",
]
sample_data = {
    "Nutrient": nutrients,
    "Amount": [random.randint(50, 500) for _ in range(len(nutrients))],
    "Unit": ["kcal", "g", "g", "mg", "mg", "g", "g", "g", "g"],
    "Daily Value": [
        random.randint(5, 150) for _ in range(len(nutrients))
    ],  # Example Daily Values, extended range to showcase more icons
}
nutrition_df = pd.DataFrame(sample_data)

# Set 'Nutrient' as index for easier access
nutrition_df = nutrition_df.set_index("Nutrient")

# --- UI Styling and Layout ---
app_ui = ui.page_fluid(
    ui.head_content(
        ui.HTML(f'<link rel="stylesheet" href="{FONT_AWESOME_LINK}">'),
        ui.tags.style(
            """
            .nutri-card {
                border: none;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                margin-bottom: 20px;
            }
            .nutri-card .card-header {
                background-color: #f8f9fa;
                border-bottom: 1px solid rgba(0,0,0,.125);
                font-weight: bold;
            }
            .daily-value {
                font-size: 0.8em;
                color: #6c757d;
            }
            .nutrition-label {
                font-family: Arial, sans-serif;
                border: 1px solid #ddd;
                padding: 10px;
                margin-top: 20px;
                border-radius: 5px;
            }
            .nutrition-label > div {
                margin-bottom: 5px;
            }
            .nutrition-label .label-bold {
                font-weight: bold;
                margin-right: 5px;
            }
            .nutrition-label hr {
                margin-top: 5px;
                margin-bottom: 5px;
            }
           .value-box-container {
                display: flex;
                flex-wrap: wrap;
                justify-content: space-between;
            }
            .value-box-item {
                flex: 1;
                min-width: 200px;
                margin: 5px;
            }

            @media (max-width: 768px) {
                .value-box-item {
                    min-width: 100%;
                }
            }
            """
        ),
    ),
    ui.panel_title(ui.h2("Nutrition Analysis and Labeling", class_="text-center mb-4")),
    ui.div(
        {"class": "value-box-container"},
        ui.div(
            {"class": "value-box-item"},
            ui.value_box(
                ui.tags.div(
                    ui.tags.i(class_="fas fa-fire me-2"),  # Using Font Awesome icon
                    "Total Calories",
                ),
                f"{nutrition_df.loc['Calories', 'Amount']} {nutrition_df.loc['Calories', 'Unit']}",
                "Based on 2,000 calorie diet",
                showcase=ui.HTML(""),
                theme="bg-gradient-orange-red",
                full_screen=False,
            ),
        ),
        ui.div(
            {"class": "value-box-item"},
            ui.value_box(
                ui.tags.div(
                    ui.tags.i(
                        class_="fas fa-hamburger me-2"
                    ),  # Using Font Awesome icon
                    "Total Fat",
                ),
                f"{nutrition_df.loc['Total Fat', 'Amount']} {nutrition_df.loc['Total Fat', 'Unit']}",
                "Recommended daily limit: 78g",
                showcase=ui.HTML(""),
                theme="text-success",
                showcase_layout="top right",
                full_screen=False,
            ),
        ),
        ui.div(
            {"class": "value-box-item"},
            ui.value_box(
                ui.tags.div(
                    ui.tags.i(class_="fas fa-leaf me-2"),  # Using Font Awesome icon
                    "Dietary Fiber",
                ),
                f"{nutrition_df.loc['Dietary Fiber', 'Amount']} {nutrition_df.loc['Dietary Fiber', 'Unit']}",
                "Recommended daily intake: 25-30g",
                showcase=ui.HTML(""),
                theme="bg-gradient-purple",
                showcase_layout="bottom",
                full_screen=False,
            ),
        ),
    ),
    ui.hr(),
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Nutrition Facts", class_="nutri-card"),
            ui.output_data_frame("nutrition_table"),
            {"class": "nutri-card"},
            height="450px",
        ),
        ui.card(
            ui.card_header("Nutrition Label", class_="nutri-card"),
            ui.output_ui("nutrition_label"),
            {"class": "nutri-card"},
            height="450px",
        ),
        width=1 / 2,
    ),
)


# --- Server Logic ---
def server(input: Inputs, output: Outputs, session: Session):
    @render.data_frame
    def nutrition_table():
        # Add daily value icon to the table
        df_copy = nutrition_df.copy()
        # Reorder columns to put Daily Value Icon at the end
        df_copy = df_copy[["Amount", "Unit", "Daily Value"]]
        return df_copy

    @render.ui
    def nutrition_label():
        label = ui.div(
            {"class": "nutrition-label"},
            ui.h4("Nutrition Facts", class_="text-center"),
            ui.div(
                ui.span({"class": "label-bold"}, "Serving Size:"),
                ui.span("1 serving"),
            ),
            ui.div(
                ui.span({"class": "label-bold"}, "Servings Per Container:"),
                ui.span("1"),
            ),
            ui.hr(),
            *[
                ui.div(
                    {"class": "d-flex justify-content-between align-items-center"},
                    ui.span({"class": "label-bold"}, nutrient),
                    ui.div(
                        ui.div(
                            f"{nutrition_df.loc[nutrient, 'Amount']} {nutrition_df.loc[nutrient, 'Unit']}"
                        ),
                        ui.div(
                            f"DV: {nutrition_df.loc[nutrient, 'Daily Value']}%",
                            class_="daily-value",
                        ),
                    ),
                )
                for nutrient in nutrients
            ],
        )
        return label


app = App(app_ui, server)
