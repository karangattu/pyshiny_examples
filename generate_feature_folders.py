import os

import ollama

shiny_app_features = [
    "Develop an interactive dashboard to track and manage inventory levels of raw materials, work-in-progress, and finished goods for breweries and wineries.",
    "Create an interactive tool to explore career paths, including required skills, education, and experience, as well as potential career progression and salary growth.",
    "Develop an app to analyze spending habits, identify areas for optimization, and provide personalized recommendations.",
    "Create interactive visualizations to explore disease prevalence, treatment efficacy, and adverse event profiles.",
    "Develop a personalized app to empower patients with interactive health education, medication management, and appointment reminders. Utilize gamification, quizzes, and visualizations to enhance patient understanding and engagement.",
    "Develop an interactive dashboard to visualize project timelines, track task assignments and progress, and monitor team performance metrics.",
    "Develop an interactive dashboard to visualize real-time stock prices, track portfolio performance, and analyze market trends. Utilize charts, heatmaps, and alerts to provide actionable insights on stocks, ETFs, and indices.",
    "An app to find and track volunteer opportunities",
    "An app with interactive maps visualizing disease outbreaks, cases and vaccination rates.",
    "An app to plan and track daily nutrition, including calorie intake and macronutrient balance",
    "An app to track and visualize personal fitness goals, progress, and achievements",
    "An app to visualize traffic congestion, accidents, and road closures in real-time",
    "An app to discover and save recipes, including meal planning and grocery lists",
    "Develop a comprehensive restaurant management app enabling owners to create, manage and update menus, track inventory, monitor sales and optimize customer experiences.",
    "Create a comprehensive weather app offering real-time forecasts, current weather conditions, and alerts for temperature, humidity, wind speed, and precipitation across global locations.",
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
