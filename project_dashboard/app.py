from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import plotly.express as px
from shinywidgets import output_widget, render_widget
from shiny import App, ui, render, reactive

# Generate synthetic data
def generate_sample_data():
    # Projects data
    projects = pd.DataFrame({
        'project_id': range(1, 6),
        'project_name': [f'Project {i}' for i in range(1, 6)],
        'start_date': [datetime.now() - timedelta(days=x) for x in [60, 45, 30, 15, 5]],
        'end_date': [datetime.now() + timedelta(days=x) for x in [30, 45, 60, 75, 90]],
        'status': np.random.choice(['On Track', 'Delayed', 'Completed'], 5)
    })

    # Team members
    team_members = ['John', 'Alice', 'Bob', 'Emma', 'David']

    # Tasks data - Convert numpy int to regular int for timedelta
    random_days = [int(x) for x in np.random.randint(-10, 30, 20)]
    tasks = pd.DataFrame({
        'task_id': range(1, 21),
        'project_id': np.random.choice(range(1, 6), 20),
        'task_name': [f'Task {i}' for i in range(1, 21)],
        'assignee': np.random.choice(team_members, 20),
        'status': np.random.choice(['Not Started', 'In Progress', 'Completed'], 20),
        'progress': np.random.randint(0, 101, 20),
        'due_date': [datetime.now() + timedelta(days=x) for x in random_days]
    })

    # Performance metrics
    performance = pd.DataFrame({
        'team_member': team_members,
        'tasks_completed': np.random.randint(5, 16, 5),
        'on_time_delivery': np.random.randint(70, 101, 5),
        'productivity_score': np.random.randint(80, 101, 5)
    })

    return projects, tasks, performance

# Generate data
projects_df, tasks_df, performance_df = generate_sample_data()

app_ui = ui.page_fluid(
    ui.head_content(
        ui.HTML('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">')
    ),
    ui.panel_title("Project Management Dashboard"),
    
    # Project Overview Section
    ui.card(
        ui.card_header("Project Timeline Overview"),
        output_widget("project_timeline"),
        full_screen=True
    ),
    
    ui.layout_column_wrap(
        # Task Management Section
        ui.card(
            ui.card_header("Task Management"),
            ui.input_select(
                "project_filter",
                "Filter by Project:",
                choices=["All"] + [f"Project {i}" for i in range(1, 6)]
            ),
            ui.input_select(
                "status_filter",
                "Filter by Status:",
                choices=["All", "Not Started", "In Progress", "Completed"]
            ),
            ui.output_table("task_table")
        ),
        
        # Team Performance Section
        ui.card(
            ui.card_header("Team Performance Metrics"),
            output_widget("performance_chart")
        ),
        width=1/2
    ),
    
    # Project Status Cards
    ui.layout_column_wrap(
        ui.value_box(
            "Total Projects",
            ui.output_text("total_projects"),
            showcase=ui.tags.i(class_="fa-solid fa-diagram-project", style="font-size: 2rem;"),
            theme="primary"
        ),
        ui.value_box(
            "Tasks in Progress",
            ui.output_text("tasks_in_progress"),
            showcase=ui.tags.i(class_="fa-solid fa-list-check", style="font-size: 2rem;"),
            theme="warning"
        ),
        ui.value_box(
            "Completed Tasks",
            ui.output_text("completed_tasks"),
            showcase=ui.tags.i(class_="fa-solid fa-circle-check", style="font-size: 2rem;"),
            theme="success"
        ),
        width=1/3
    ),
)

def server(input, output, session):
    # Project Timeline
    @render_widget
    def project_timeline():
        fig = px.timeline(
            projects_df,
            x_start="start_date",
            x_end="end_date",
            y="project_name",
            color="status",
            title="Project Timelines"
        )
        fig.update_layout(height=300)
        return fig

    # Filtered Tasks Table
    @reactive.calc
    def filtered_tasks():
        df = tasks_df.copy()
        
        if input.project_filter() != "All":
            project_id = int(input.project_filter().split()[-1])
            df = df[df['project_id'] == project_id]
            
        if input.status_filter() != "All":
            df = df[df['status'] == input.status_filter()]
            
        return df

    @render.table
    def task_table():
        return filtered_tasks()[['task_name', 'assignee', 'status', 'progress', 'due_date']]

    # Team Performance Chart
    @render_widget
    def performance_chart():
        fig = px.bar(
            performance_df,
            x='team_member',
            y=['tasks_completed', 'on_time_delivery', 'productivity_score'],
            title="Team Performance Metrics",
            barmode='group'
        )
        fig.update_layout(height=400)
        return fig

    # Value Box Metrics
    @render.text
    def total_projects():
        return str(len(projects_df))

    @render.text
    def tasks_in_progress():
        return str(len(tasks_df[tasks_df['status'] == 'In Progress']))

    @render.text
    def completed_tasks():
        return str(len(tasks_df[tasks_df['status'] == 'Completed']))

app = App(app_ui, server)