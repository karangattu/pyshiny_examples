import datetime
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from shiny import App, reactive, render, ui

# Synthetic Data Generation
def generate_food_database():
    """Generate a synthetic food database with nutritional information."""
    food_categories = [
        "Proteins", "Vegetables", "Fruits", "Grains", "Dairy", 
        "Snacks", "Beverages"
    ]
    
    foods = []
    for category in food_categories:
        if category == "Proteins":
            items = [
                {"name": "Chicken Breast", "calories": 165, "protein": 31, "carbs": 0, "fat": 3.6},
                {"name": "Salmon", "calories": 208, "protein": 22, "carbs": 0, "fat": 13},
                {"name": "Tofu", "calories": 144, "protein": 17, "carbs": 2.9, "fat": 8.7},
                {"name": "Eggs", "calories": 78, "protein": 6, "carbs": 0.6, "fat": 5.3}
            ]
        elif category == "Vegetables":
            items = [
                {"name": "Broccoli", "calories": 55, "protein": 4, "carbs": 11, "fat": 0.6},
                {"name": "Spinach", "calories": 23, "protein": 2.9, "carbs": 3.6, "fat": 0.4},
                {"name": "Carrots", "calories": 41, "protein": 0.9, "carbs": 10, "fat": 0.2}
            ]
        elif category == "Fruits":
            items = [
                {"name": "Apple", "calories": 95, "protein": 0.5, "carbs": 25, "fat": 0.3},
                {"name": "Banana", "calories": 105, "protein": 1.3, "carbs": 27, "fat": 0.4},
                {"name": "Strawberries", "calories": 50, "protein": 1, "carbs": 12, "fat": 0.5}
            ]
        elif category == "Grains":
            items = [
                {"name": "Brown Rice", "calories": 216, "protein": 5, "carbs": 45, "fat": 1.8},
                {"name": "Quinoa", "calories": 222, "protein": 8, "carbs": 39, "fat": 3.6},
                {"name": "Whole Wheat Bread", "calories": 69, "protein": 3.6, "carbs": 12, "fat": 1}
            ]
        elif category == "Dairy":
            items = [
                {"name": "Greek Yogurt", "calories": 146, "protein": 20, "carbs": 9, "fat": 4.9},
                {"name": "Milk", "calories": 102, "protein": 8, "carbs": 12, "fat": 3.6},
                {"name": "Cheese", "calories": 402, "protein": 25, "carbs": 1.3, "fat": 33}
            ]
        elif category == "Snacks":
            items = [
                {"name": "Almonds", "calories": 164, "protein": 6, "carbs": 6, "fat": 14},
                {"name": "Protein Bar", "calories": 210, "protein": 20, "carbs": 25, "fat": 7},
                {"name": "Popcorn", "calories": 31, "protein": 1, "carbs": 6, "fat": 0.4}
            ]
        else:  # Beverages
            items = [
                {"name": "Water", "calories": 0, "protein": 0, "carbs": 0, "fat": 0},
                {"name": "Green Tea", "calories": 2, "protein": 0, "carbs": 0.5, "fat": 0},
                {"name": "Orange Juice", "calories": 110, "protein": 2, "carbs": 26, "fat": 0}
            ]
        
        foods.extend(items)
    
    return pd.DataFrame(foods)

# Generate initial food database
food_database = generate_food_database()

app_ui = ui.page_fluid(
    ui.head_content(
        ui.tags.style("""
            .nutrition-card { border: 1px solid #ddd; padding: 15px; margin-bottom: 15px; }
            .macronutrient-bar { height: 20px; }
        """)
    ),
    ui.panel_title("🥗 Daily Nutrition Tracker"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_select(
                "food_category", 
                "Select Food Category", 
                list(food_database["name"].unique())
            ),
            ui.input_numeric("quantity", "Quantity", value=1, min=1),
            ui.input_action_button("add_food", "Add to Daily Log"),
            ui.input_action_button("reset_log", "Reset Daily Log"),
        ),
        ui.layout_columns(
            ui.card(
                ui.card_header("Daily Nutrition Summary"),
                ui.output_text_verbatim("daily_summary"),
                ui.output_plot("macronutrient_breakdown"),
                full_screen=True
            ),
            ui.card(
                ui.card_header("Daily Food Log"),
                ui.output_data_frame("daily_log_table"),
                full_screen=True
            ),
            col_widths=[6, 6]
        )
    )
)

def server(input, output, session):
    # Reactive value to track daily food log
    daily_log = reactive.Value(pd.DataFrame(columns=["Food", "Quantity", "Calories", "Protein", "Carbs", "Fat"]))

    @reactive.effect
    @reactive.event(input.add_food)
    def _():
        selected_food = input.food_category()
        quantity = input.quantity()
        
        food_info = food_database[food_database["name"] == selected_food].iloc[0]
        
        new_entry = pd.DataFrame({
            "Food": [selected_food],
            "Quantity": [quantity],
            "Calories": [food_info["calories"] * quantity],
            "Protein": [food_info["protein"] * quantity],
            "Carbs": [food_info["carbs"] * quantity],
            "Fat": [food_info["fat"] * quantity]
        })
        
        updated_log = pd.concat([daily_log(), new_entry], ignore_index=True)
        daily_log.set(updated_log)

    @reactive.effect
    @reactive.event(input.reset_log)
    def _():
        daily_log.set(pd.DataFrame(columns=["Food", "Quantity", "Calories", "Protein", "Carbs", "Fat"]))

    @render.text
    def daily_summary():
        log = daily_log()
        if log.empty:
            return "No food logged yet."
        
        total_calories = log["Calories"].sum()
        total_protein = log["Protein"].sum()
        total_carbs = log["Carbs"].sum()
        total_fat = log["Fat"].sum()
        
        return (
            f"Total Daily Intake:\n"
            f"Calories: {total_calories:.0f} kcal\n"
            f"Protein: {total_protein:.1f}g\n"
            f"Carbohydrates: {total_carbs:.1f}g\n"
            f"Fat: {total_fat:.1f}g"
        )

    @render.plot
    def macronutrient_breakdown():
        log = daily_log()
        if log.empty:
            plt.figure(figsize=(6, 4))
            plt.text(0.5, 0.5, "No Data", horizontalalignment='center')
            plt.axis('off')
            return plt.gcf()

        total_protein = log["Protein"].sum()
        total_carbs = log["Carbs"].sum()
        total_fat = log["Fat"].sum()

        plt.figure(figsize=(8, 4))
        plt.bar(["Protein", "Carbohydrates", "Fat"], 
                [total_protein, total_carbs, total_fat], 
                color=['blue', 'green', 'red'])
        plt.title("Daily Macronutrient Breakdown")
        plt.ylabel("Grams")
        return plt.gcf()

    @render.data_frame
    def daily_log_table():
        log = daily_log()
        return render.DataGrid(log, selection_mode="multiple")

app = App(app_ui, server)