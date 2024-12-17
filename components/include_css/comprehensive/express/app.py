from pathlib import Path
from shiny import reactive
from shiny.express import input, ui, render

# Create a synthetic CSS content as a string
css_content = """
body {
    background-color: #f4f4f4;
    font-family: Arial, sans-serif;
}

.highlight {
    color: #007bff;
    font-weight: bold;
}

.custom-text {
    font-style: italic;
    text-decoration: underline;
}
"""

# Create a temporary CSS file for demonstration
temp_css_path = Path(__file__).parent / "temp_styles.css"
with open(temp_css_path, "w") as f:
    f.write(css_content)

# Synthetic data for demonstration
data = {
    "names": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "scores": [85, 92, 78, 95, 88],
    "departments": ["Sales", "Marketing", "Engineering", "HR", "Finance"],
}

# Page setup with title
ui.page_opts(title="ui.include_css() Demonstration", fillable=True)

# Sidebar for CSS inclusion method selection
with ui.sidebar():
    ui.input_radio_buttons(
        "css_method", "CSS Inclusion Method", ["link", "link_files", "inline"]
    )
    ui.input_checkbox("apply_custom", "Apply Custom Styles", value=False)

# Main content area
with ui.layout_column_wrap(width=1 / 2):
    # Data display card
    with ui.card():
        ui.card_header("Employee Data")

        @render.data_frame
        def employee_table():
            import pandas as pd

            df = pd.DataFrame(data)
            return df

    # CSS Method Demonstration Card
    with ui.card():
        ui.card_header("CSS Method Demonstration")

        @render.ui
        def css_demo():
            # Conditional CSS inclusion based on radio button
            if input.css_method() == "link":
                ui.include_css(temp_css_path, method="link")
            elif input.css_method() == "link_files":
                ui.include_css(temp_css_path, method="link_files")
            else:  # inline method
                ui.include_css(temp_css_path, method="inline")

            # Conditional custom styling
            if input.apply_custom():
                classes = "highlight custom-text"
            else:
                classes = ""

            return ui.div(f"CSS Method: {input.css_method()}", class_=classes)


# Inline CSS demonstration
ui.tags.style(
    """
.dynamic-style {
    color: green;
    font-size: 1.2em;
}
"""
)

# Additional demonstration of CSS application
with ui.card():
    ui.card_header("Dynamic Styling")

    @render.ui
    def dynamic_style_demo():
        return ui.div(
            "Dynamic Style Demonstration",
            class_="dynamic-style" if input.apply_custom() else "",
        )
