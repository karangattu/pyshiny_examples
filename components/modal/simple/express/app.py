from shiny import reactive
from shiny.express import input, ui, render

# Sample data for demonstration
sample_data = {
    "Project A": {"status": "In Progress", "completion": "75%", "team": "Alpha"},
    "Project B": {"status": "Completed", "completion": "100%", "team": "Beta"},
    "Project C": {"status": "Planning", "completion": "10%", "team": "Gamma"},
    "Project D": {"status": "On Hold", "completion": "45%", "team": "Delta"},
}

ui.page_opts(title="Project Status Dashboard", fillable=True)

# Create a button for each project
with ui.layout_column_wrap(width=1 / 2):
    for project in sample_data:
        ui.input_action_button(
            f"view_{project.lower().replace(' ', '_')}",
            f"View {project} Details",
            class_="btn-primary m-1",
        )

# Define reactive effects for each project button
for project_name, project_info in sample_data.items():
    button_id = f"view_{project_name.lower().replace(' ', '_')}"

    @reactive.effect
    @reactive.event(lambda p=button_id: input[p]())
    def show_modal(project=project_name, info=project_info):
        modal_content = ui.modal(
            ui.h3(f"{project} Details", class_="text-center"),
            ui.tags.hr(),
            ui.p(f"Status: {info['status']}", class_="fw-bold"),
            ui.p(f"Completion: {info['completion']}", class_="fw-bold"),
            ui.p(f"Team: {info['team']}", class_="fw-bold"),
            title=project,
            easy_close=True,
            footer=ui.modal_button("Close"),
        )
        ui.modal_show(modal_content)


# Add some descriptive text
ui.markdown(
    """
### Project Status Overview
Click on any project button above to view detailed information in a modal dialog.
The modal can be closed by:
* Clicking the Close button
* Clicking outside the modal
* Pressing the Escape key
"""
)
