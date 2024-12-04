from datetime import date, datetime, timedelta
import pandas as pd
import numpy as np
from shiny import App, ui, render, reactive
import matplotlib.pyplot as plt

# Sample data
recipes_data = pd.DataFrame({
    'id': range(1, 11),
    'name': [
        'Spaghetti Carbonara', 'Chicken Stir Fry', 'Vegetable Curry', 
        'Beef Tacos', 'Greek Salad', 'Mushroom Risotto', 
        'Grilled Salmon', 'Veggie Pizza', 'Quinoa Bowl',
        'Chocolate Cake'
    ],
    'category': [
        'Italian', 'Asian', 'Indian', 'Mexican', 'Mediterranean',
        'Italian', 'Seafood', 'Italian', 'Healthy', 'Dessert'
    ],
    'prep_time': [30, 25, 35, 20, 15, 40, 25, 45, 20, 50],
    'servings': [4, 4, 6, 4, 2, 4, 2, 6, 2, 8],
    'difficulty': [
        'Medium', 'Easy', 'Medium', 'Easy', 'Easy',
        'Hard', 'Medium', 'Medium', 'Easy', 'Hard'
    ]
})

ingredients_data = pd.DataFrame({
    'recipe_id': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4],
    'ingredient': [
        'Pasta', 'Eggs', 'Bacon', 'Chicken', 'Vegetables', 'Soy Sauce',
        'Rice', 'Curry Paste', 'Coconut Milk', 'Tortillas'
    ],
    'amount': [500, 4, 200, 400, 300, 50, 300, 100, 400, 8],
    'unit': ['g', 'pcs', 'g', 'g', 'g', 'ml', 'g', 'g', 'ml', 'pcs']
})

meal_plan = pd.DataFrame({
    'date': pd.date_range(start=date.today(), periods=7),
    'meal_type': ['Breakfast', 'Lunch', 'Dinner'] * 2 + ['Breakfast'],
    'recipe_id': np.random.choice(recipes_data['id'], 7)
})

app_ui = ui.page_fluid(
    ui.navset_tab(
        ui.nav_panel("Recipes",
            ui.layout_sidebar(
                ui.sidebar(
                    ui.input_select(
                        "category_filter",
                        "Filter by Category",
                        choices=["All"] + list(recipes_data["category"].unique())
                    ),
                    ui.input_select(
                        "difficulty_filter",
                        "Filter by Difficulty",
                        choices=["All"] + list(recipes_data["difficulty"].unique())
                    ),
                    ui.input_numeric(
                        "max_prep_time",
                        "Maximum Preparation Time (minutes)",
                        value=60,
                        min=0,
                        max=120
                    )
                ),
                ui.card(
                    ui.card_header("Recipe List"),
                    ui.output_data_frame("recipe_table")
                ),
                ui.card(
                    ui.card_header("Recipe Details"),
                    ui.output_text_verbatim("recipe_details"),
                    ui.output_text_verbatim("ingredients_list")
                )
            )
        ),
        ui.nav_panel("Meal Planning",
            ui.layout_sidebar(
                ui.sidebar(
                    ui.input_date_range(
                        "meal_plan_dates",
                        "Select Date Range",
                        start=date.today(),
                        end=date.today() + timedelta(days=7)
                    ),
                    ui.input_select(
                        "meal_type",
                        "Meal Type",
                        choices=["Breakfast", "Lunch", "Dinner"]
                    ),
                    ui.input_select(
                        "recipe_select",
                        "Select Recipe",
                        choices=list(recipes_data["name"])
                    ),
                    ui.input_action_button(
                        "add_meal",
                        "Add to Meal Plan",
                        class_="btn-primary"
                    )
                ),
                ui.card(
                    ui.card_header("Current Meal Plan"),
                    ui.output_data_frame("meal_plan_table")
                ),
                ui.card(
                    ui.card_header("Shopping List"),
                    ui.output_text_verbatim("shopping_list")
                )
            )
        )
    )
)

def server(input, output, session):
    # Reactive filtered recipes
    @reactive.calc
    def filtered_recipes():
        df = recipes_data.copy()
        
        if input.category_filter() != "All":
            df = df[df["category"] == input.category_filter()]
            
        if input.difficulty_filter() != "All":
            df = df[df["difficulty"] == input.difficulty_filter()]
            
        df = df[df["prep_time"] <= input.max_prep_time()]
        return df

    # Recipe table output
    @render.data_frame
    def recipe_table():
        return render.DataGrid(filtered_recipes(), selection_mode="single")

    # Recipe details output
    @render.text
    def recipe_details():
        selected = recipe_table.value
        if not selected:
            return "Select a recipe to view details"
        
        recipe = filtered_recipes().iloc[selected[0]]
        return (
            f"Recipe: {recipe['name']}\n"
            f"Category: {recipe['category']}\n"
            f"Preparation Time: {recipe['prep_time']} minutes\n"
            f"Servings: {recipe['servings']}\n"
            f"Difficulty: {recipe['difficulty']}"
        )

    # Ingredients list output
    @render.text
    def ingredients_list():
        selected = recipe_table.value
        if not selected:
            return ""
        
        recipe_id = filtered_recipes().iloc[selected[0]]["id"]
        recipe_ingredients = ingredients_data[ingredients_data["recipe_id"] == recipe_id]
        
        result = "\nIngredients:\n"
        for _, ing in recipe_ingredients.iterrows():
            result += f"- {ing['amount']} {ing['unit']} {ing['ingredient']}\n"
        return result

    # Meal plan table
    @render.data_frame
    def meal_plan_table():
        df = meal_plan.merge(
            recipes_data[["id", "name"]],
            left_on="recipe_id",
            right_on="id"
        )[["date", "meal_type", "name"]]
        df = df.rename(columns={"name": "recipe"})
        return render.DataGrid(df)

    # Add meal to plan
    @reactive.effect
    @reactive.event(input.add_meal)
    def add_to_meal_plan():
        global meal_plan
        recipe_id = recipes_data[recipes_data["name"] == input.recipe_select()]["id"].iloc[0]
        new_meal = pd.DataFrame({
            "date": [input.meal_plan_dates()[0]],
            "meal_type": [input.meal_type()],
            "recipe_id": [recipe_id]
        })
        meal_plan = pd.concat([meal_plan, new_meal], ignore_index=True)

    # Shopping list
    @render.text
    def shopping_list():
        start_date, end_date = input.meal_plan_dates()
        
        # Filter meal plan for selected date range
        planned_meals = meal_plan[
            (meal_plan["date"] >= start_date) &
            (meal_plan["date"] <= end_date)
        ]
        
        # Get all ingredients needed
        shopping_items = {}
        for _, meal in planned_meals.iterrows():
            recipe_ingredients = ingredients_data[
                ingredients_data["recipe_id"] == meal["recipe_id"]
            ]
            
            for _, ing in recipe_ingredients.iterrows():
                key = (ing["ingredient"], ing["unit"])
                if key in shopping_items:
                    shopping_items[key] += ing["amount"]
                else:
                    shopping_items[key] = ing["amount"]
        
        # Format shopping list
        result = "Shopping List:\n"
        for (ingredient, unit), amount in shopping_items.items():
            result += f"- {amount} {unit} {ingredient}\n"
        
        return result

app = App(app_ui, server)