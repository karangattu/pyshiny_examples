from shiny import reactive
from shiny.express import input, render, ui

# Synthetic data for demonstration
departments = {
    "tech": {
        "Software Engineer": "A tech professional who designs, develops, and maintains software systems.",
        "Data Scientist": "An expert who analyzes complex data to help organizations make informed decisions.",
        "Cloud Architect": "Designs and manages cloud computing infrastructure and strategies.",
    },
    "finance": {
        "Financial Analyst": "Provides guidance to businesses and individuals in investment decisions.",
        "Investment Banker": "Helps companies and governments raise capital through securities.",
        "Accountant": "Prepares and examines financial records, ensuring accuracy and compliance.",
    },
    "healthcare": {
        "Physician": "Diagnoses and treats medical conditions, provides patient care.",
        "Nurse Practitioner": "Advanced practice registered nurse providing comprehensive healthcare.",
        "Medical Researcher": "Conducts research to improve medical knowledge and treatments.",
    },
}

# Page configuration
ui.page_opts(title="Radio Buttons Showcase", fillable=True)

# Sidebar with various radio button configurations
with ui.sidebar():
    # Basic radio buttons with simple list of choices
    ui.input_radio_buttons(
        "basic_rb", "Basic Radio Buttons", ["Option A", "Option B", "Option C"]
    )

    # Radio buttons with dictionary (HTML labels)
    ui.input_radio_buttons(
        "html_rb",
        "Radio Buttons with HTML Labels",
        {
            "red": ui.span("Red", style="color: red;"),
            "green": ui.span("Green", style="color: green;"),
            "blue": ui.span("Blue", style="color: blue;"),
        },
    )

    # Radio buttons with initial selection
    ui.input_radio_buttons(
        "selected_rb",
        "Radio Buttons with Initial Selection",
        ["First Choice", "Second Choice", "Third Choice"],
        selected="Second Choice",
    )

    # Inline radio buttons
    ui.input_radio_buttons(
        "inline_rb",
        "Inline Radio Buttons",
        ["Inline 1", "Inline 2", "Inline 3"],
        inline=True,
    )

    # Radio buttons with custom width
    ui.input_radio_buttons(
        "width_rb",
        "Radio Buttons with Custom Width",
        ["Narrow", "Medium", "Wide"],
        width="300px",
    )

# Main panel with outputs
with ui.layout_columns():
    # Display selected basic radio button
    with ui.card():
        ui.card_header("Basic Radio Button Selection")

        @render.text
        def basic_output():
            return f"You selected: {input.basic_rb()}"

    # Display selected HTML radio button
    with ui.card():
        ui.card_header("HTML Radio Button Selection")

        @render.text
        def html_output():
            return f"You selected: {input.html_rb()}"

    # Display selected radio button with initial selection
    with ui.card():
        ui.card_header("Selected Radio Button")

        @render.text
        def selected_output():
            return f"You selected: {input.selected_rb()}"

    # Display selected inline radio button
    with ui.card():
        ui.card_header("Inline Radio Button Selection")

        @render.text
        def inline_output():
            return f"You selected: {input.inline_rb()}"

    # Display selected radio button with custom width
    with ui.card():
        ui.card_header("Width Radio Button Selection")

        @render.text
        def width_output():
            return f"You selected: {input.width_rb()}"


# Nested radio buttons with department and job selection
with ui.sidebar():
    ui.input_radio_buttons("department", "Select Department", list(departments.keys()))

    @reactive.calc
    def job_choices():
        dept = input.department()
        return list(departments.get(dept, {}))

    ui.input_radio_buttons(
        "job",
        "Select Job",
        choices=job_choices(),  # Call the function to get the list
        # Optionally add a default selected job if needed
        # selected=job_choices()[0] if job_choices() else None
    )

# Job description display
with ui.card():
    ui.card_header("Job Description")

    @render.text
    def job_description():
        dept = input.department()
        job = input.job()
        if dept and job:
            return departments[dept].get(job, "No description available.")
        return "Please select a department and job."
