import os

import ollama

shiny_app_features = [
    "An app to track expenses, income, and budgets, providing visualizations and insights for financial planning",
    "A real-time weather app displaying forecasts, temperature, humidity, and wind speed for various locations",
    "An app to analyze stock performance, trends, and predictions using historical data",
    "An app to visualize traffic congestion, accidents, and road closures in real-time",
    "An interactive dashboard to display election results, voter turnout, and demographic analysis",
    "An app to diagnose potential health issues based on user-inputted symptoms",
    "An app to monitor mental health, tracking mood, sleep, and stress levels",
    "An app to set and track fitness goals, including workout plans and progress tracking",
    "An app to plan and track daily nutrition, including calorie intake and macronutrient balance",
    "An app to track disease outbreaks, cases, and vaccination rates with maps",
    "An app to provide interactive math lessons, quizzes, and exercises",
    "An app to learn new languages, including interactive lessons and quizzes",
    "An app to simulate science experiments, allowing users to explore and learn",
    "An app to explore career paths, job requirements, and salary ranges",
    "An app to find and compare university courses, including tuition fees and course details",
    "An app to manage tasks, deadlines, and reminders",
    "An app to track time spent on tasks, projects, and activities",
    "An app to schedule meetings, including attendee availability and reminders",
    "An interactive dashboard to track project progress, tasks, and team performance",
    "An app to plan trips, including itinerary, flights, and accommodation booking",
    "An app to recommend movies based on user preferences",
    "An app to discover new music, including personalized recommendations",
    "An app to explore destinations, including attractions, restaurants, and activities",
    "An app to find and track events, including concerts, festivals, and sports games",
    "An app to discover and save recipes, including meal planning and grocery lists",
    "An app to calculate and track carbon footprint",
    "An app to track water usage and provide conservation tips",
    "An interactive dashboard to track natural disasters, response efforts, and relief resources",
    "An app to find and track volunteer opportunities",
    "An app to provide tips and resources for sustainable living",
]

# iterate through shiny_app_features and create a folder for each item with a markdown file called "prompt.md"
for feature in shiny_app_features:
    response = ollama.chat(
        model="gemma2:9b",
        messages=[
            {
                "role": "user",
                "content": f'Given this response: "{feature}". Suggest an appropriate directory name to sum up this feature. Make it unique and Keep the naming professional and answer with just the name. Also, dont add any whitespaces or random symbols in the directory name and use _ instead',
            },
        ],
    )
    folder_name = response["message"]["content"]
    folder_name = (
        folder_name.strip()
        .replace(" ", "_")
        .replace("?", "")
        .replace("/", "")
        .replace("\n", "")
    )
    try:
        os.makedirs(folder_name, exist_ok=False)
    except FileExistsError:
        print(f"Folder {folder_name} already exists")
        os.makedirs(f"{folder_name}_1", exist_ok=False)
    with open(f"{folder_name}/PROMPT.md", "w") as f:
        f.write(f"{feature}")
