from shiny import ui, reactive
from shiny.express import input, render, ui as express_ui
import random
import pandas as pd
import numpy as np


# Synthetic data generation
def generate_product_data(n=50):
    products = [
        "Laptop",
        "Smartphone",
        "Tablet",
        "Smartwatch",
        "Headphones",
        "Camera",
        "Speaker",
        "Monitor",
    ]
    return pd.DataFrame(
        {
            "product": [random.choice(products) for _ in range(n)],
            "price": np.random.uniform(100, 2000, n).round(2),
            "rating": np.random.uniform(1, 5, n).round(1),
            "stock": np.random.randint(10, 500, n),
        }
    )


# Generate initial data
product_df = generate_product_data()

# Page options and styling
express_ui.page_opts(title="TagList Showcase", fillable=True)

# Add Font Awesome for icons
express_ui.head_content(
    express_ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">'
    )
)

# Sidebar for interactions
with express_ui.sidebar():
    express_ui.input_select(
        "method",
        "Select TagList Method",
        [
            "append",
            "extend",
            "insert",
            "get_dependencies",
            "get_html_string",
            "render",
            "save_html",
            "show",
        ],
    )
    express_ui.input_action_button("generate", "Regenerate Data")

# Main content area
with express_ui.layout_columns():
    with express_ui.card():
        express_ui.card_header("TagList Demonstration")

        @render.ui
        def taglist_demo():
            method = input.method()

            # Create a base TagList
            base_taglist = express_ui.TagList(
                express_ui.tags.h3("Product Showcase"),
                express_ui.tags.p("Exploring TagList methods in Shiny for Python"),
            )

            # Demonstrate different TagList methods
            if method == "append":
                base_taglist.append(express_ui.tags.div("Appended content"))
                return base_taglist

            elif method == "extend":
                base_taglist.extend(
                    [
                        express_ui.tags.div("Extended content 1"),
                        express_ui.tags.div("Extended content 2"),
                    ]
                )
                return base_taglist

            elif method == "insert":
                base_taglist.insert(1, express_ui.tags.div("Inserted content"))
                return base_taglist

            elif method == "get_dependencies":
                dependencies = base_taglist.get_dependencies()
                return express_ui.tags.pre(str(dependencies))

            elif method == "get_html_string":
                html_string = base_taglist.get_html_string()
                return express_ui.tags.pre(html_string)

            elif method == "render":
                rendered = base_taglist.render()
                return express_ui.tags.pre(str(rendered))

            elif method == "save_html":
                import tempfile

                with tempfile.NamedTemporaryFile(
                    mode="w", delete=False, suffix=".html"
                ) as temp:
                    base_taglist.save_html(temp.name)
                    with open(temp.name, "r") as f:
                        return express_ui.tags.pre(f.read())

            elif method == "show":
                # This will open in browser or IPython
                base_taglist.show()
                return express_ui.tags.p("Check your browser or IPython environment")

    with express_ui.card():
        express_ui.card_header("Product Data")

        @render.data_frame
        def product_table():
            return product_df


# Reactive effect to regenerate data
@reactive.effect
@reactive.event(input.generate)
def _():
    global product_df
    product_df = generate_product_data()
