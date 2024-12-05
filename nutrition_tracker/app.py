from datetime import date, datetime, timedelta
import numpy as np
import pandas as pd
import plotly.express as px
from shinywidgets import output_widget, render_widget

from shiny import App, reactive, render, ui

# Generate sample food database
food_db = pd.DataFrame({
    "food": [
        "Chicken Breast", "Salmon", "Brown Rice", "Sweet Potato", 
        "Broccoli", "Eggs", "Oatmeal", "Greek Yogurt", "Almonds", "Banana"
    ],
    "serving_size": [
        "100g", "100g", "100g", "100g", 
        "100g", "1 large", "100g", "100g", "28g", "1 medium"
    ],
    "calories": [165, 208, 112, 86, 55, 72, 389, 59, 164, 105],
    "protein": [31, 22, 2.6, 1.6, 3.7, 6.3, 16.9, 10.2, 6, 1.3],
    "carbs": [0, 0, 23.5, 20.1, 11.2, 0.4, 66.3, 3.6, 6.1, 27],
    "fats": [3.6, 13, 0.9, 0.1, 0.6, 4.8, 6.9, 0.4, 14, 0.3]
})

# Generate sample meal logs
def generate_meal_logs(days_back: int = 30) -> pd.DataFrame:
    dates = [date.today() - timedelta(days=x) for x in range(days_back)]
    records = []
    
    for d in dates:
        # Randomly select 3-5 foods for each day
        n_foods = np.random.randint(3, 6)
        foods = food_db.sample(n=n_foods)
        
        for _, food in foods.iterrows():
            records.append({
                "date": d,
                "food": food["food"],
                "serving_size": food["serving_size"],
                "servings": round(np.random.uniform(0.5, 2.0), 1),
                "calories": food["calories"],
                "protein": food["protein"],
                "carbs": food["carbs"],
                "fats": food["fats"]
            })
    
    return pd.DataFrame(records)

meal_logs = generate_meal_logs()

app_ui = ui.page_fluid(
    ui.panel_title("Daily Nutrition Tracker"),
    
    ui.layout_sidebar(
        ui.sidebar(
            ui.h4("Add Food Entry"),
            ui.input_date("entry_date", "Date", value=date.today()),
            ui.input_selectize(
                "food_select", 
                "Select Food", 
                choices=food_db["food"].tolist()
            ),
            ui.input_numeric(
                "servings", 
                "Number of Servings",
                value=1,
                min=0.1,
                step=0.1
            ),
            ui.input_action_button(
                "add_food", 
                "Add Food",
                class_="btn-primary"
            ),
            ui.hr(),
            ui.input_date_range(
                "date_range",
                "Date Range for Analysis",
                start=date.today() - timedelta(days=7),
                end=date.today()
            ),
            width=300
        ),
        
        ui.navset_tab(
            ui.nav_panel(
                "Daily Summary",
                ui.layout_column_wrap(
                    ui.value_box(
                        "Total Calories", 
                        ui.output_text("total_calories"),
                        showcase=ui.tags.i(class_="fa-solid fa-fire", style="font-size: 2rem;"),
                        theme="bg-gradient-orange-red"
                    ),
                    ui.value_box(
                        "Protein (g)", 
                        ui.output_text("total_protein"),
                        showcase=ui.tags.i(class_="fa-solid fa-drumstick-bite", style="font-size: 2rem;"),
                        theme="bg-gradient-blue-purple"
                    ),
                    ui.value_box(
                        "Carbs (g)", 
                        ui.output_text("total_carbs"),
                        showcase=ui.tags.i(class_="fa-solid fa-bread-slice", style="font-size: 2rem;"),
                        theme="bg-gradient-yellow-red"
                    ),
                    ui.value_box(
                        "Fats (g)", 
                        ui.output_text("total_fats"),
                        showcase=ui.tags.i(class_="fa-solid fa-cheese", style="font-size: 2rem;"),
                        theme="bg-gradient-green-blue"
                    ),
                ),
                ui.card(
                    ui.card_header("Today's Food Log"),
                    ui.output_data_frame("daily_log")
                ),
            ),
            ui.nav_panel(
                "Trends",
                output_widget("calories_trend"),
                ui.br(),
                output_widget("macros_trend")
            ),
        )
    ),
    ui.head_content(
        ui.HTML('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">')
    ),
)

def server(input, output, session):
    # Reactive value to store meal logs
    logs = reactive.Value(meal_logs)
    
    @reactive.effect
    @reactive.event(input.add_food)
    def _():
        global meal_logs
        food_info = food_db[food_db["food"] == input.food_select()].iloc[0]
        new_entry = pd.DataFrame([{
            "date": input.entry_date(),
            "food": food_info["food"],
            "serving_size": food_info["serving_size"],
            "servings": input.servings(),
            "calories": food_info["calories"],
            "protein": food_info["protein"],
            "carbs": food_info["carbs"],
            "fats": food_info["fats"]
        }])
        meal_logs = pd.concat([meal_logs, new_entry], ignore_index=True)
        logs.set(meal_logs)
        
    @reactive.calc
    def filtered_logs():
        df = logs.get()
        mask = (df["date"] >= input.date_range()[0]) & (df["date"] <= input.date_range()[1])
        return df[mask]
    
    @reactive.calc
    def daily_logs():
        df = logs.get()
        return df[df["date"] == input.entry_date()]
    
    @render.text
    def total_calories():
        df = daily_logs()
        total = round(sum(df["calories"] * df["servings"]))
        return f"{total:,}"
    
    @render.text
    def total_protein():
        df = daily_logs()
        total = round(sum(df["protein"] * df["servings"]))
        return f"{total:,}"
    
    @render.text
    def total_carbs():
        df = daily_logs()
        total = round(sum(df["carbs"] * df["servings"]))
        return f"{total:,}"
    
    @render.text
    def total_fats():
        df = daily_logs()
        total = round(sum(df["fats"] * df["servings"]))
        return f"{total:,}"
    
    @render.data_frame
    def daily_log():
        df = daily_logs()
        if len(df) == 0:
            return pd.DataFrame()
        
        summary = df.copy()
        summary["calories"] = summary["calories"] * summary["servings"]
        summary["protein"] = summary["protein"] * summary["servings"]
        summary["carbs"] = summary["carbs"] * summary["servings"]
        summary["fats"] = summary["fats"] * summary["servings"]
        
        return render.DataGrid(
            summary[["food", "serving_size", "servings", "calories", "protein", "carbs", "fats"]],
            row_selection_mode="none"
        )
    
    @render_widget
    def calories_trend():
        df = filtered_logs()
        daily_calories = df.groupby("date").apply(
            lambda x: sum(x["calories"] * x["servings"])
        ).reset_index()
        daily_calories.columns = ["date", "calories"]
        
        fig = px.line(
            daily_calories, 
            x="date", 
            y="calories",
            title="Daily Calorie Intake"
        )
        fig.update_layout(showlegend=False)
        return fig
    
    @render_widget
    def macros_trend():
        df = filtered_logs()
        daily_macros = df.groupby("date").apply(
            lambda x: pd.Series({
                "protein": sum(x["protein"] * x["servings"]),
                "carbs": sum(x["carbs"] * x["servings"]),
                "fats": sum(x["fats"] * x["servings"])
            })
        ).reset_index()
        
        fig = px.line(
            daily_macros, 
            x="date",
            y=["protein", "carbs", "fats"],
            title="Daily Macronutrient Intake"
        )
        return fig

app = App(app_ui, server)