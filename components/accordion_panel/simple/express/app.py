from shiny import reactive
from shiny.express import input, ui, render

# Create synthetic data for demonstration
project_data = {
    "Project A": {
        "description": "A cutting-edge machine learning project focused on predictive analytics.",
        "status": "In Progress",
        "team_size": 5,
        "budget": "$250,000",
    },
    "Project B": {
        "description": "A cloud infrastructure optimization initiative.",
        "status": "Planning",
        "team_size": 3,
        "budget": "$150,000",
    },
    "Project C": {
        "description": "An AI-driven customer experience enhancement platform.",
        "status": "Completed",
        "team_size": 7,
        "budget": "$500,000",
    },
}

# Set page options for better presentation
ui.page_opts(title="Project Management Dashboard", fillable=True)

# Create an accordion with multiple panels
with ui.accordion(id="project_accordion", multiple=True):
    # Dynamically create accordion panels for each project
    for project_name, project_info in project_data.items():
        with ui.accordion_panel(project_name):
            # Display project details in each panel
            ui.markdown(f"### {project_name} Details")
            ui.tags.ul(
                ui.tags.li(f"**Description:** {project_info['description']}"),
                ui.tags.li(f"**Status:** {project_info['status']}"),
                ui.tags.li(f"**Team Size:** {project_info['team_size']} members"),
                ui.tags.li(f"**Budget:** {project_info['budget']}"),
            )

# Add a section to show which projects are currently open
ui.h4("Currently Open Projects:")


@render.text
def show_open_projects():
    return f"Open Projects: {input.project_accordion() or 'None'}"
