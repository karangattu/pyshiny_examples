import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta
from shiny import App, reactive, render, ui

# Generate synthetic career path data
def generate_career_paths():
    career_paths = [
        {
            "career": "Software Engineer",
            "entry_level_skills": ["Python", "JavaScript", "Git", "SQL"],
            "mid_level_skills": ["Cloud Computing", "Machine Learning", "Docker", "Kubernetes"],
            "senior_level_skills": ["System Architecture", "DevOps", "Technical Leadership"],
            "education_path": ["Bachelor's in Computer Science", "Master's in Software Engineering"],
            "salary_progression": [75000, 110000, 150000, 200000],
            "typical_progression": [
                "Junior Software Engineer",
                "Software Engineer",
                "Senior Software Engineer", 
                "Lead Software Engineer",
                "Technical Architect"
            ]
        },
        {
            "career": "Data Scientist",
            "entry_level_skills": ["Python", "Statistics", "R", "Excel"],
            "mid_level_skills": ["Machine Learning", "Deep Learning", "SQL", "Data Visualization"],
            "senior_level_skills": ["Advanced ML", "AI Strategy", "Big Data", "Research"],
            "education_path": ["Bachelor's in Statistics/Computer Science", "Master's/PhD in Data Science"],
            "salary_progression": [80000, 120000, 160000, 220000],
            "typical_progression": [
                "Junior Data Analyst",
                "Data Scientist",
                "Senior Data Scientist", 
                "Lead Data Scientist",
                "Chief Data Officer"
            ]
        },
        {
            "career": "Product Manager",
            "entry_level_skills": ["Communication", "Basic Analytics", "Project Management"],
            "mid_level_skills": ["Strategic Planning", "User Research", "Agile Methodologies"],
            "senior_level_skills": ["Product Strategy", "Business Development", "Innovation Management"],
            "education_path": ["Bachelor's in Business/Tech", "MBA", "Product Management Certification"],
            "salary_progression": [85000, 125000, 170000, 250000],
            "typical_progression": [
                "Associate Product Manager",
                "Product Manager",
                "Senior Product Manager", 
                "Director of Product",
                "VP of Product"
            ]
        }
    ]
    return career_paths

# Generate synthetic skills data
def generate_skills_data(career_paths_list):
    skills_data = []
    for career in career_paths_list:
        for skill_level in ['entry_level_skills', 'mid_level_skills', 'senior_level_skills']:
            for skill in career[skill_level]:
                skills_data.append({
                    'career': career['career'],
                    'skill_level': skill_level.replace('_', ' ').title(),
                    'skill': skill
                })
    return pd.DataFrame(skills_data)

# Generate synthetic progression data
def generate_progression_data(career_paths_list):
    progression_data = []
    for career in career_paths_list:
        for i, role in enumerate(career['typical_progression']):
            progression_data.append({
                'career': career['career'],
                'role': role,
                'avg_years_in_role': i + 1,
                'avg_salary': career['salary_progression'][min(i, len(career['salary_progression'])-1)]
            })
    return pd.DataFrame(progression_data)

# Prepare data
career_paths_list = generate_career_paths()
career_paths_df = pd.DataFrame(career_paths_list)
skills_df = generate_skills_data(career_paths_list)
progression_df = generate_progression_data(career_paths_list)

# Shiny App
app_ui = ui.page_fluid(
    ui.panel_title("Career Path Explorer"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_select(
                "selected_career", 
                "Select Career Path", 
                choices=career_paths_df['career'].tolist()
            ),
            ui.input_radio_buttons(
                "view_type", 
                "View Type", 
                choices=["Skills", "Progression", "Salary"]
            )
        ),
        ui.navset_card_tab(
            ui.nav_panel("Career Details", ui.output_ui("career_details")),
            ui.nav_panel("Visualization", ui.output_plot("career_plot"))
        )
    )
)

def server(input, output, session):
    @reactive.calc
    def selected_career_data():
        return career_paths_df[career_paths_df['career'] == input.selected_career()].iloc[0]

    @render.ui
    def career_details():
        career = selected_career_data()
        
        details_html = f"""
        <div class='card-body'>
            <h4>{career['career']} Career Path</h4>
            
            <h5>Education Path:</h5>
            <ul>
                {"".join(f"<li>{edu}</li>" for edu in career['education_path'])}
            </ul>
            
            <h5>Skills Progression:</h5>
            <h6>Entry Level Skills:</h6>
            <p>{", ".join(career['entry_level_skills'])}</p>
            
            <h6>Mid Level Skills:</h6>
            <p>{", ".join(career['mid_level_skills'])}</p>
            
            <h6>Senior Level Skills:</h6>
            <p>{", ".join(career['senior_level_skills'])}</p>
            
            <h5>Typical Career Progression:</h5>
            <ul>
                {"".join(f"<li>{role}</li>" for role in career['typical_progression'])}
            </ul>
        </div>
        """
        return ui.HTML(details_html)

    @render.plot
    def career_plot():
        career_name = input.selected_career()
        view_type = input.view_type()
        
        plt.figure(figsize=(10, 6))
        
        if view_type == "Skills":
            career_skills = skills_df[skills_df['career'] == career_name]
            skill_counts = career_skills.groupby('skill_level')['skill'].count()
            skill_counts.plot(kind='bar', color='skyblue')
            plt.title(f"Skills Distribution for {career_name}")
            plt.xlabel("Skill Level")
            plt.ylabel("Number of Skills")
        
        elif view_type == "Progression":
            career_progression = progression_df[progression_df['career'] == career_name]
            plt.plot(career_progression['role'], career_progression['avg_years_in_role'], marker='o')
            plt.title(f"Career Progression: Years in Role for {career_name}")
            plt.xlabel("Role")
            plt.ylabel("Average Years")
            plt.xticks(rotation=45, ha='right')
        
        elif view_type == "Salary":
            career_progression = progression_df[progression_df['career'] == career_name]
            plt.plot(career_progression['role'], career_progression['avg_salary'], marker='o')
            plt.title(f"Salary Progression for {career_name}")
            plt.xlabel("Role")
            plt.ylabel("Average Salary ($)")
            plt.xticks(rotation=45, ha='right')
        
        plt.tight_layout()
        return plt.gcf()

app = App(app_ui, server)