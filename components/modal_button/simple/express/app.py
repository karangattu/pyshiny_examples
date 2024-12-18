from shiny import reactive
from shiny.express import input, render, ui

# Page title
ui.page_opts(title="Modal Button Demo", fillable=True)

# Main button to trigger modal
ui.input_action_button("show_modal", "Show Project Details", class_="btn-primary")

# Sample project data
project_details = {
    "name": "Data Analysis Project",
    "status": "In Progress",
    "completion": "75%",
    "team": ["John", "Sarah", "Mike"],
    "deadline": "2024-03-31",
}


@reactive.effect
@reactive.event(input.show_modal)
def _():
    modal_content = ui.modal(
        ui.h3("Project Details", class_="text-center mb-4"),
        ui.tags.div(
            ui.tags.p(f"Project Name: {project_details['name']}", class_="mb-2"),
            ui.tags.p(f"Status: {project_details['status']}", class_="mb-2"),
            ui.tags.p(f"Completion: {project_details['completion']}", class_="mb-2"),
            ui.tags.p(
                f"Team Members: {', '.join(project_details['team'])}", class_="mb-2"
            ),
            ui.tags.p(f"Deadline: {project_details['deadline']}", class_="mb-2"),
            class_="mb-4",
        ),
        footer=[
            ui.modal_button("Close", class_="btn-secondary"),
            ui.input_action_button(
                "save_changes", "Save Changes", class_="btn-primary"
            ),
        ],
        easy_close=True,
        title="Project Information",
    )
    ui.modal_show(modal_content)


@reactive.effect
@reactive.event(input.save_changes)
def _():
    ui.notification_show("Changes saved successfully!", type="message")
    ui.modal_remove()


# Display current status
@render.ui
def status_display():
    return ui.card(
        ui.h4("Current Project Status"),
        ui.tags.p(f"Project: {project_details['name']}"),
        ui.tags.p(f"Status: {project_details['status']}"),
        ui.tags.p(f"Click the button above to see full details"),
        class_="mt-3",
    )
