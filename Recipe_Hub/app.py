import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from shiny import App, render, ui, reactive

# Synthetic Data Generation
def generate_recipes():
    cuisines = ['Italian', 'Mexican', 'Indian', 'Chinese', 'Mediterranean', 'American']
    meal_types = ['Breakfast', 'Lunch', 'Dinner', 'Dessert', 'Snack']
    dietary_restrictions = ['Vegetarian', 'Vegan', 'Gluten-Free', 'None']
    
    recipes = []
    for i in range(50):
        recipe = {
            'id': f'recipe_{i+1}',
            'name': f'Recipe {i+1}',
            'cuisine': random.choice(cuisines),
            'meal_type': random.choice(meal_types),
            'dietary_restriction': random.choice(dietary_restrictions),
            'ingredients': [
                f'Ingredient {j}' for j in range(random.randint(3, 8))
            ],
            'cooking_time': random.randint(15, 120),
            'difficulty': random.choice(['Easy', 'Medium', 'Hard']),
            'calories': random.randint(200, 800)
        }
        recipes.append(recipe)
    
    return pd.DataFrame(recipes)

def generate_meal_plan(recipes_df):
    days = pd.date_range(start=datetime.now(), periods=7)
    meal_plan = []
    
    for day in days:
        breakfast = recipes_df[recipes_df['meal_type'] == 'Breakfast'].sample(1).iloc[0]
        lunch = recipes_df[recipes_df['meal_type'] == 'Lunch'].sample(1).iloc[0]
        dinner = recipes_df[recipes_df['meal_type'] == 'Dinner'].sample(1).iloc[0]
        
        meal_plan.append({
            'date': day.date(),
            'breakfast': breakfast['name'],
            'lunch': lunch['name'],
            'dinner': dinner['name']
        })
    
    return pd.DataFrame(meal_plan)

# Generate initial data
recipes_df = generate_recipes()
meal_plan_df = generate_meal_plan(recipes_df)

# Shiny App
app_ui = ui.page_fluid(
    ui.panel_title("🍽️ Recipe Discovery & Meal Planner"),
    ui.head_content(
        ui.HTML('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">')
    ),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_select(
                "cuisine_filter", 
                "Filter by Cuisine", 
                ["All"] + list(recipes_df['cuisine'].unique())
            ),
            ui.input_select(
                "meal_type_filter", 
                "Filter by Meal Type", 
                ["All"] + list(recipes_df['meal_type'].unique())
            ),
            ui.input_select(
                "diet_filter", 
                "Dietary Restrictions", 
                ["All"] + list(recipes_df['dietary_restriction'].unique())
            ),
            ui.input_slider(
                "cooking_time_filter", 
                "Max Cooking Time (minutes)", 
                min=15, max=120, value=120
            ),
        ),
        ui.layout_columns(
            ui.card(
                ui.card_header("Recipe List"),
                ui.output_data_frame("recipe_table"),
                height="600px"
            ),
            ui.card(
                ui.card_header("Recipe Details"),
                ui.output_ui("recipe_details"),
                height="600px"
            )
        )
    ),
    ui.layout_columns(
        ui.card(
            ui.card_header("Weekly Meal Plan"),
            ui.output_data_frame("meal_plan_table"),
            height="400px"
        ),
        ui.card(
            ui.card_header("Grocery List"),
            ui.output_ui("grocery_list"),
            height="400px"
        )
    )
)

def server(input, output, session):
    @reactive.calc
    def filtered_recipes():
        df = recipes_df.copy()
        
        if input.cuisine_filter() != "All":
            df = df[df['cuisine'] == input.cuisine_filter()]
        
        if input.meal_type_filter() != "All":
            df = df[df['meal_type'] == input.meal_type_filter()]
        
        if input.diet_filter() != "All":
            df = df[df['dietary_restriction'] == input.diet_filter()]
        
        df = df[df['cooking_time'] <= input.cooking_time_filter()]
        
        return df

    @render.data_frame
    def recipe_table():
        df = filtered_recipes()
        return render.DataGrid(
            df[['name', 'cuisine', 'meal_type', 'cooking_time']],
            selection_mode="single"
        )

    @render.ui
    def recipe_details():
        selected_rows = recipe_table.data_view(selected=True)
        
        if selected_rows.empty:
            return ui.div("Select a recipe to view details")
        
        recipe = selected_rows.iloc[0]
        recipe_full = recipes_df[recipes_df['name'] == recipe['name']].iloc[0]
        
        return ui.div(
            ui.h4(recipe_full['name']),
            ui.tags.p(f"Cuisine: {recipe_full['cuisine']}"),
            ui.tags.p(f"Meal Type: {recipe_full['meal_type']}"),
            ui.tags.p(f"Difficulty: {recipe_full['difficulty']}"),
            ui.tags.p(f"Cooking Time: {recipe_full['cooking_time']} minutes"),
            ui.tags.p(f"Calories: {recipe_full['calories']} kcal"),
            ui.h5("Ingredients:"),
            ui.tags.ul([ui.tags.li(ing) for ing in recipe_full['ingredients']])
        )

    @render.data_frame
    def meal_plan_table():
        return render.DataGrid(meal_plan_df)

    @render.ui
    def grocery_list():
        selected_recipes = recipe_table.data_view(selected=True)
        
        if selected_recipes.empty:
            return ui.div("Select a recipe to generate a grocery list")
        
        recipe_name = selected_recipes.iloc[0]['name']
        recipe_full = recipes_df[recipes_df['name'] == recipe_name].iloc[0]
        
        return ui.tags.ul([ui.tags.li(ing) for ing in recipe_full['ingredients']])

app = App(app_ui, server)