from shiny.express import input, ui, render
from pathlib import Path

# Set page options
ui.page_opts(title="CSS Demo App", fillable=True)

# Add CSS using ui.head_content instead of include_css
ui.head_content(
    ui.tags.style(
        """
        .custom-card {
            background-color: #f0f8ff;
            border: 2px solid #4682b4;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
        }

        .highlight-text {
            color: #4682b4;
            font-weight: bold;
            font-size: 1.2em;
        }

        .custom-button {
            background-color: #4682b4;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .custom-button:hover {
            background-color: #357abd;
        }
        """
    )
)

# Sample data
sample_data = {"Product A": 150, "Product B": 300, "Product C": 200, "Product D": 450}

# Create UI elements using custom CSS classes
with ui.card(class_="custom-card"):
    ui.h3("Sales Dashboard")
    ui.input_select("product", "Select Product", list(sample_data.keys()))
    ui.input_action_button("show_sales", "Show Sales", class_="custom-button")

with ui.card(class_="custom-card"):

    @render.ui
    def sales_info():
        if not input.show_sales():
            return "Click the button to see sales data"

        selected_product = input.product()
        sales = sample_data[selected_product]
        return ui.div(
            [
                "Sales for ",
                ui.span(selected_product, class_="highlight-text"),
                f": ${sales:,}",
            ]
        )
