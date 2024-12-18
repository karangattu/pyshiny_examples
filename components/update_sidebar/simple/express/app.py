from shiny import reactive
from shiny.express import input, ui, render

# Create some synthetic data
departments = ["Sales", "Marketing", "Engineering", "Finance", "HR"]
employee_counts = [45, 30, 75, 25, 20]
average_salaries = [85000, 75000, 120000, 95000, 65000]

ui.page_opts(title="Department Dashboard")

# Create a sidebar with an initial state
with ui.sidebar(id="sidebar", open="desktop"):
    ui.input_radio_buttons("dept_select", "Select Department", choices=departments)

# Main content area
with ui.layout_columns():

    @render.text
    def employee_count():
        selected_dept = input.dept_select()
        index = departments.index(selected_dept)
        return f"Number of Employees: {employee_counts[index]}"

    @render.text
    def avg_salary():
        selected_dept = input.dept_select()
        index = departments.index(selected_dept)
        return f"Average Salary: ${average_salaries[index]:,}"


# Buttons to control sidebar
ui.input_action_button("open_sidebar", "Open Sidebar")
ui.input_action_button("close_sidebar", "Close Sidebar")


# Reactive effects to update sidebar visibility
@reactive.effect
@reactive.event(input.open_sidebar)
def _():
    ui.update_sidebar("sidebar", show=True)


@reactive.effect
@reactive.event(input.close_sidebar)
def _():
    ui.update_sidebar("sidebar", show=False)


# Optional: Show current sidebar state
@render.text
def sidebar_state():
    return f"Sidebar state: {input.sidebar()}"
