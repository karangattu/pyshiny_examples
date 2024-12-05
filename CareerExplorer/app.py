from shiny import App, render, ui, reactive
import pandas as pd
import plotly.express as px
from shinywidgets import output_widget, render_widget

# Create synthetic data
career_paths = pd.DataFrame({
    "role": [
        "Junior Developer", "Senior Developer", "Tech Lead", "Software Architect",
        "Junior Data Scientist", "Senior Data Scientist", "Data Science Manager", "Chief Data Officer",
        "Junior PM", "Senior PM", "Program Manager", "Director of Product"
    ],
    "track": [
        "Software Development", "Software Development", "Software Development", "Software Development",
        "Data Science", "Data Science", "Data Science", "Data Science",
        "Product Management", "Product Management", "Product Management", "Product Management"
    ],
    "level": [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],
    "min_experience": [0, 3, 5, 8, 0, 3, 5, 8, 0, 3, 5, 8],
    "base_salary": [
        75000, 110000, 150000, 180000,
        80000, 120000, 160000, 190000,
        70000, 100000, 140000, 170000
    ]
})

required_skills = {
    "Software Development": [
        "Python", "Java", "JavaScript", "Git", "SQL", "System Design",
        "Cloud Platforms", "Agile Methodologies", "CI/CD", "Software Architecture"
    ],
    "Data Science": [
        "Python", "R", "SQL", "Machine Learning", "Statistics", "Data Visualization",
        "Big Data", "Deep Learning", "Data Mining", "Business Intelligence"
    ],
    "Product Management": [
        "Agile", "User Stories", "Market Research", "Strategy", "Analytics",
        "Stakeholder Management", "Roadmapping", "A/B Testing", "User Research", "Business Analysis"
    ]
}

education_req = {
    "Software Development": [
        "Bachelor's in Computer Science",
        "Bachelor's in Software Engineering",
        "Related Technical Degree"
    ],
    "Data Science": [
        "Master's in Data Science",
        "Master's in Statistics",
        "PhD in related field"
    ],
    "Product Management": [
        "Bachelor's in Business",
        "Bachelor's in Computer Science",
        "MBA (preferred)"
    ]
}

app_ui = ui.page_fluid(
    ui.panel_title("Career Path Explorer"),
    
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_select(
                "career_track",
                "Select Career Track",
                choices=list(career_paths["track"].unique())
            ),
            ui.input_slider(
                "experience",
                "Years of Experience",
                min=0,
                max=15,
                value=0
            ),
            width=250
        ),
        
        ui.layout_column_wrap(
            ui.value_box(
                "Current Eligible Role",
                ui.output_text("eligible_role"),
                theme="primary"
            ),
            ui.value_box(
                "Expected Base Salary",
                ui.output_text("expected_salary"),
                theme="success"
            ),
            width=1/2
        ),
        
        ui.card(
            ui.card_header("Career Progression"),
            output_widget("career_plot")
        ),
        
        ui.layout_column_wrap(
            ui.card(
                ui.card_header("Required Skills"),
                ui.output_ui("skills_list")
            ),
            ui.card(
                ui.card_header("Education Requirements"),
                ui.output_ui("education_list")
            ),
            width=1/2
        )
    )
)

def server(input, output, session):
    
    @reactive.calc
    def filtered_data():
        return career_paths[career_paths["track"] == input.career_track()]
    
    @reactive.calc
    def current_level():
        df = filtered_data()
        experience = input.experience()
        eligible_roles = df[df["min_experience"] <= experience]
        if len(eligible_roles) > 0:
            return eligible_roles.iloc[-1]
        return None
    
    @render.text
    def eligible_role():
        level = current_level()
        if level is not None:
            return level["role"]
        return "Not eligible yet"
    
    @render.text
    def expected_salary():
        level = current_level()
        if level is not None:
            return f"${level['base_salary']:,.0f}"
        return "N/A"
    
    @render_widget
    def career_plot():
        df = filtered_data()
        fig = px.line(
            df, 
            x="min_experience", 
            y="base_salary",
            text="role",
            markers=True,
            title=f"Salary Progression in {input.career_track()}"
        )
        
        # Add current experience marker
        if current_level() is not None:
            fig.add_vline(
                x=input.experience(),
                line_dash="dash",
                line_color="red",
                annotation_text="You are here"
            )
            
        fig.update_traces(textposition="top center")
        fig.update_layout(
            xaxis_title="Years of Experience",
            yaxis_title="Base Salary ($)",
            showlegend=False
        )
        return fig
    
    @render.ui
    def skills_list():
        track = input.career_track()
        skills = required_skills[track]
        return ui.tags.div(
            ui.tags.p("Key skills needed for this career track:"),
            ui.tags.ul([ui.tags.li(skill) for skill in skills])
        )
    
    @render.ui
    def education_list():
        track = input.career_track()
        education = education_req[track]
        return ui.tags.div(
            ui.tags.p("Recommended education:"),
            ui.tags.ul([ui.tags.li(edu) for edu in education])
        )

app = App(app_ui, server)