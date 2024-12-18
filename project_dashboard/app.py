import datetime
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from shiny import App, reactive, render, ui

# Synthetic Data Generation
def generate_project_data():
    # Project Details
    projects = [
        "Digital Transformation", 
        "E-commerce Platform", 
        "Mobile App Redesign", 
        "Cloud Migration", 
        "Customer Analytics"
    ]
    
    # Team Members
    team_members = [
        "Alice Johnson", "Bob Smith", "Charlie Brown", 
        "Diana Martinez", "Ethan Wong", "Fiona Lee"
    ]
    
    # Task Statuses
    statuses = ["Not Started", "In Progress", "Completed", "On Hold"]
    
    # Generate Project Tasks
    project_tasks = []
    for project in projects:
        num_tasks = random.randint(5, 10)
        for i in range(num_tasks):
            start_date = datetime.date(2023, random.randint(1, 12), random.randint(1, 28))
            duration = random.randint(7, 45)
            end_date = start_date + datetime.timedelta(days=duration)
            
            project_tasks.append({
                "Project": project,
                "Task": f"Task {i+1}",
                "Assignee": random.choice(team_members),
                "Start Date": start_date,
                "End Date": end_date,
                "Status": random.choice(statuses),
                "Progress": random.randint(0, 100)
            })
    
    return pd.DataFrame(project_tasks)

# Generate synthetic performance data
def generate_performance_data(project_df):
    performance_data = []
    for member in project_df["Assignee"].unique():
        member_tasks = project_df[project_df["Assignee"] == member]
        performance_data.append({
            "Team Member": member,
            "Total Tasks": len(member_tasks),
            "Completed Tasks": len(member_tasks[member_tasks["Status"] == "Completed"]),
            "Average Progress": member_tasks["Progress"].mean(),
            "On Time %": random.uniform(60, 95)
        })
    
    return pd.DataFrame(performance_data)

# Generate data
project_df = generate_project_data()
performance_df = generate_performance_data(project_df)

# Shiny App UI
app_ui = ui.page_fluid(
    ui.panel_title("Project Management Dashboard"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_select(
                "selected_project", 
                "Select Project", 
                choices=project_df["Project"].unique().tolist()
            ),
            ui.input_select(
                "selected_team_member", 
                "Select Team Member", 
                choices=["All"] + project_df["Assignee"].unique().tolist()
            ),
            ui.input_date_range(
                "date_range", 
                "Date Range",
                start=project_df["Start Date"].min(),
                end=project_df["End Date"].max()
            )
        ),
        ui.layout_columns(
            ui.card(
                ui.card_header("Project Tasks"),
                ui.output_data_frame("tasks_table")
            ),
            ui.card(
                ui.card_header("Performance Metrics"),
                ui.output_plot("performance_plot")
            )
        )
    )
)

def server(input, output, session):
    @reactive.calc
    def filtered_tasks():
        df = project_df.copy()
        
        # Project filter
        df = df[df["Project"] == input.selected_project()]
        
        # Team member filter
        if input.selected_team_member() != "All":
            df = df[df["Assignee"] == input.selected_team_member()]
        
        # Date range filter
        start_date = input.date_range()[0]
        end_date = input.date_range()[1]
        df = df[(df["Start Date"] >= start_date) & (df["End Date"] <= end_date)]
        
        return df

    @render.data_frame
    def tasks_table():
        df = filtered_tasks()
        return render.DataGrid(
            df[["Task", "Assignee", "Start Date", "End Date", "Status", "Progress"]],
            selection_mode="rows"
        )

    @render.plot
    def performance_plot():
        df = performance_df.copy()
        
        plt.figure(figsize=(10, 6))
        plt.bar(df["Team Member"], df["On Time %"], color='skyblue')
        plt.title("Team Performance: On-Time Percentage")
        plt.xlabel("Team Member")
        plt.ylabel("On-Time Percentage (%)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        return plt.gcf()

app = App(app_ui, server)