from shiny import reactive
from shiny.express import input, ui

# Synthetic data for the example
employee_data = [
    {"name": "Alice Johnson", "department": "Sales", "salary": 75000},
    {"name": "Bob Smith", "department": "Marketing", "salary": 68000},
    {"name": "Charlie Brown", "department": "Engineering", "salary": 95000},
    {"name": "Diana Prince", "department": "HR", "salary": 72000},
    {"name": "Ethan Hunt", "department": "IT", "salary": 85000},
]

# Page options
ui.page_opts(title="Employee Details Modal Demo")

# Main UI layout
ui.input_action_button("show_modal", "View Employee Details")


# Modal trigger effect
@reactive.effect
@reactive.event(input.show_modal)
def _():
    # Create a modal with employee information
    m = ui.modal(
        ui.p("Select an employee to view details:"),
        ui.input_select(
            "employee_select",
            "Choose Employee",
            {emp["name"]: emp["name"] for emp in employee_data},
        ),
        title="Employee Information",
        footer=ui.modal_button("Close"),
        easy_close=True,
    )
    ui.modal_show(m)


# Render employee details when an employee is selected
@reactive.effect
@reactive.event(input.employee_select)
def show_employee_details():
    if input.employee_select():
        # Find the selected employee's details
        selected_emp = next(
            (emp for emp in employee_data if emp["name"] == input.employee_select()),
            None,
        )

        if selected_emp:
            # Create a details modal
            details_modal = ui.modal(
                ui.tags.div(
                    ui.tags.p(f"Name: {selected_emp['name']}"),
                    ui.tags.p(f"Department: {selected_emp['department']}"),
                    ui.tags.p(f"Salary: ${selected_emp['salary']:,}"),
                    style="text-align: center;",
                ),
                title=f"Details for {selected_emp['name']}",
                footer=ui.modal_button("Close"),
                size="m",
            )
            ui.modal_show(details_modal)
