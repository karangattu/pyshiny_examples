import random
import datetime
from typing import List, Dict

from shiny import App, Inputs, Outputs, Session, reactive, render, ui
from shiny.types import SafeException

# Sample recipe data
recipes = [
    {
        "name": "Spaghetti Bolognese",
        "ingredients": ["ground beef", "onion", "garlic", "tomatoes", "pasta"],
        "instructions": [
            "Cook the ground beef in a pan until browned.",
            "Add the chopped onion and garlic, and cook until softened.",
            "Pour in the diced tomatoes and simmer for 30 minutes.",
            "Cook the pasta according to package instructions.",
            "Serve the Bolognese sauce over the cooked pasta."
        ],
        "servings": 4,
        "prep_time": 15,
        "cook_time": 45
    },
    {
        "name": "Grilled Chicken Salad",
        "ingredients": ["chicken breasts", "lettuce", "tomatoes", "cucumber", "feta cheese"],
        "instructions": [
            "Grill the chicken breasts until cooked through.",
            "Chop the lettuce, tomatoes, and cucumber.",
            "Crumble the feta cheese.",
            "Arrange the salad ingredients on a plate and top with the grilled chicken."
        ],
        "servings": 2,
        "prep_time": 10,
        "cook_time": 20
    },
    {
        "name": "Vegetable Stir-Fry",
        "ingredients": ["broccoli", "bell pepper", "carrots", "mushrooms", "soy sauce", "rice"],
        "instructions": [
            "Chop the broccoli, bell pepper, carrots, and mushrooms.",
            "Heat oil in a wok or large skillet and stir-fry the vegetables until tender-crisp.",
            "Add soy sauce and stir to coat the vegetables.",
            "Serve the stir-fry over cooked rice."
        ],
        "servings": 3,
        "prep_time": 15,
        "cook_time": 20
    }
]

# Sample meal plan data
meal_plans = [
    {
        "date": datetime.date(2023, 5, 1),
        "recipe": recipes[0]["name"],
        "servings": 4
    },
    {
        "date": datetime.date(2023, 5, 2),
        "recipe": recipes[1]["name"],
        "servings": 2
    },
    {
        "date": datetime.date(2023, 5, 3),
        "recipe": recipes[2]["name"],
        "servings": 3
    }
]

# Sample grocery list data
grocery_list: Dict[str, int] = {}
for recipe in recipes:
    for ingredient in recipe["ingredients"]:
        if ingredient in grocery_list:
            grocery_list[ingredient] += recipe["servings"]
        else:
            grocery_list[ingredient] = recipe["servings"]

app_ui = ui.page_fluid(
    ui.panel_title("Recipe Discovery and Meal Planning"),
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Discover Recipes"),
            ui.input_text("search_recipe", "Search Recipes"),
            ui.output_data_frame("recipe_table"),
            ui.download_button("download_recipe", "Save Recipe"),
            width=1 / 2,
        ),
        ui.card(
            ui.card_header("Meal Plan"),
            ui.input_date_range("meal_plan_dates", "Meal Plan Dates"),
            ui.output_data_frame("meal_plan_table"),
            ui.download_button("download_meal_plan", "Save Meal Plan"),
            width=1 / 2,
        ),
        ui.card(
            ui.card_header("Grocery List"),
            ui.output_data_frame("grocery_list_table"),
            ui.download_button("download_grocery_list", "Save Grocery List"),
            width=1,
        ),
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    @reactive.calc
    def filtered_recipes():
        search_term = input.search_recipe().lower()
        return [recipe for recipe in recipes if search_term in recipe["name"].lower()]

    @render.data_frame
    def recipe_table():
        df = pd.DataFrame(filtered_recipes())
        return render.DataGrid(
            df,
            selection_mode="rows",
            width="100%",
            height="400px",
        )

    @render.download
    def download_recipe():
        req(input.recipe_table_selected_rows())
        return [recipes[i] for i in input.recipe_table_selected_rows()]

    @reactive.calc
    def filtered_meal_plan():
        start_date = input.meal_plan_dates()[0]
        end_date = input.meal_plan_dates()[1]
        return [plan for plan in meal_plans if start_date <= plan["date"] <= end_date]

    @render.data_frame
    def meal_plan_table():
        df = pd.DataFrame(filtered_meal_plan())
        return render.DataGrid(
            df,
            width="100%",
            height="400px",
        )

    @render.download
    def download_meal_plan():
        return filtered_meal_plan()

    @render.data_frame
    def grocery_list_table():
        df = pd.DataFrame.from_dict(grocery_list, orient="index")
        df.columns = ["Quantity"]
        return render.DataGrid(
            df,
            width="100%",
            height="400px",
        )

    @render.download
    def download_grocery_list():
        return grocery_list

app = App(app_ui, server)