from shiny import reactive
from shiny.express import input, ui, render

# Synthetic data for demonstration
course_data = {
    "Python Programming": {
        "description": "A comprehensive course covering Python fundamentals and advanced topics.",
        "duration": "12 weeks",
        "difficulty": "Intermediate",
    },
    "Data Science Bootcamp": {
        "description": "Learn data science from scratch using Python, pandas, and machine learning libraries.",
        "duration": "16 weeks",
        "difficulty": "Advanced",
    },
    "Web Development with Django": {
        "description": "Build full-stack web applications using Python and the Django framework.",
        "duration": "10 weeks",
        "difficulty": "Intermediate",
    },
}

# Set page options
ui.page_opts(title="Course Catalog", fillable=True)

# Create an accordion to display course information
with ui.accordion(id="course_accordion", multiple=True):
    for course_name, details in course_data.items():
        with ui.accordion_panel(course_name):
            ui.markdown(
                f"""
            ### {course_name}
            
            **Description:** {details['description']}
            
            - **Duration:** {details['duration']}
            - **Difficulty Level:** {details['difficulty']}
            """
            )

# Add a section to show which courses are currently expanded
ui.h4("Currently Expanded Courses:")


@render.text
def show_expanded_courses():
    expanded_courses = input.course_accordion()
    if not expanded_courses:
        return "No courses are currently expanded."
    return f"Expanded courses: {', '.join(expanded_courses)}"
