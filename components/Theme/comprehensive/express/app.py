from shiny import reactive
from shiny.express import input, ui, render
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)

# Ensure all arrays have the same length
regions = ["North", "South", "East", "West", "Central"] * 5
products = ["Electronics", "Clothing", "Furniture", "Food", "Toys"] * 5
sales = np.random.randint(50000, 500000, 25)
profit_margins = np.random.uniform(0.1, 0.5, 25)

sales_data = pd.DataFrame(
    {
        "Region": regions,
        "Product": products,
        "Sales": sales,
        "Profit Margin": profit_margins,
    }
)

# Create a custom theme with various customizations
theme = (
    ui.Theme("shiny")
    .add_defaults(
        # Custom default values
        primary_color="#007bff",
        secondary_color="#6c757d",
        success_color="#28a745",
        dashboard_design=True,
    )
    .add_mixins(
        # Custom mixins for headings and specific elements
        headings_color="$success",
        select_color_text="$primary",
        bar_color="$secondary",
    )
    .add_rules(
        # Custom CSS rules
        """
        em { color: $warning; }
        .sidebar-title { color: $danger; }
        .card-header { background-color: $light; }
        """
    )
)

# Set page options with the custom theme
ui.page_opts(title="Theme Customization Showcase", theme=theme, fillable=True)

# Sidebar with various inputs to demonstrate theme
with ui.sidebar(id="sidebar"):
    ui.input_select(
        "region", "Select Region", choices=sales_data["Region"].unique().tolist()
    )
    ui.input_slider(
        "sales_range", "Sales Range", min=50000, max=500000, value=(100000, 400000)
    )
    ui.input_checkbox_group(
        "products", "Select Products", choices=sales_data["Product"].unique().tolist()
    )

# Main content area with multiple visualizations
with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Sales by Region")

        @render.plot
        def region_sales():
            filtered_data = sales_data[
                (sales_data["Region"] == input.region())
                & (
                    sales_data["Sales"].between(
                        input.sales_range()[0], input.sales_range()[1]
                    )
                )
            ]

            plt.figure(figsize=(8, 5))
            filtered_data.groupby("Product")["Sales"].sum().plot(kind="bar")
            plt.title(f"Sales in {input.region()} Region")
            plt.xlabel("Product")
            plt.ylabel("Total Sales")
            plt.tight_layout()
            return plt.gcf()

    with ui.card(full_screen=True):
        ui.card_header("Profit Margin Distribution")

        @render.plot
        def profit_margin_plot():
            filtered_data = sales_data[
                (sales_data["Region"] == input.region())
                & (
                    sales_data["Product"].isin(
                        input.products() or sales_data["Product"].unique()
                    )
                )
            ]

            plt.figure(figsize=(8, 5))
            filtered_data.boxplot(column="Profit Margin", by="Product")
            plt.title(f"Profit Margin in {input.region()} Region")
            plt.suptitle("")  # Remove automatic suptitle
            plt.ylabel("Profit Margin")
            plt.tight_layout()
            return plt.gcf()


# Theme method showcase section
with ui.accordion(id="theme_methods"):
    with ui.accordion_panel("Theme Methods Demonstration"):
        ui.markdown(
            """
        ### Theme Methods
        - `add_defaults()`: Add custom default values
        - `add_mixins()`: Add custom mixins for specific styling
        - `add_rules()`: Add custom CSS rules
        - `to_sass()`: View the generated Sass
        - `to_css()`: View the compiled CSS
        """
        )

        @render.code
        def sass_output():
            return theme.to_sass()

        @render.code
        def css_output():
            return theme.to_css()


# Additional UI elements to showcase theme
ui.hr()
ui.p(ui.tags.em("This is an emphasized text to show custom theming"))
ui.p("This is a normal paragraph text")
