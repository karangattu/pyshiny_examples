from shiny import reactive
from shiny.express import input, ui, render
import random
import pandas as pd
from datetime import datetime, timedelta


# Synthetic Data Generation
def generate_sales_data(num_records=50):
    """Generate synthetic sales data."""
    products = ["Laptop", "Smartphone", "Tablet", "Smartwatch", "Headphones"]
    regions = ["North", "South", "East", "West", "Central"]

    data = {
        "Date": [
            datetime.now() - timedelta(days=random.randint(0, 365))
            for _ in range(num_records)
        ],
        "Product": [random.choice(products) for _ in range(num_records)],
        "Region": [random.choice(regions) for _ in range(num_records)],
        "Sales": [random.uniform(100, 10000) for _ in range(num_records)],
    }

    return pd.DataFrame(data)


# Create synthetic sales dataset
sales_df = generate_sales_data()

# Page Configuration with Panel Title Variations
ui.page_opts(title="Panel Title Showcase")

# Demonstrate different panel title usages
with ui.card():
    # Basic string title
    ui.panel_title("Basic String Title")
    ui.markdown("A simple panel title using a string.")

with ui.card():
    # HTML Title with styling
    ui.panel_title(ui.tags.span("HTML Title", style="color: blue; font-weight: bold;"))
    ui.markdown("A panel title using HTML with custom styling.")

with ui.card():
    # Title with window title
    ui.panel_title("Main Display Title", window_title="Browser Tab Title")
    ui.markdown("A panel title with a different browser tab title.")

# Interactive Panel Title
with ui.sidebar():
    ui.input_select(
        "title_type",
        "Title Type",
        choices=["Standard", "Emphasized", "Warning", "Success"],
    )

with ui.card():

    @render.ui
    def dynamic_title():
        title_styles = {
            "Standard": "Standard Dynamic Title",
            "Emphasized": ui.tags.strong("Emphasized Dynamic Title"),
            "Warning": ui.tags.span("Warning Title", style="color: orange;"),
            "Success": ui.tags.span("Success Title", style="color: green;"),
        }
        return ui.panel_title(title_styles[input.title_type()])

    @render.table
    def sales_table():
        filtered_df = sales_df[sales_df["Product"] == input.title_type()]
        return filtered_df if not filtered_df.empty else sales_df


# Data Summary Section
with ui.card():
    ui.panel_title(
        ui.tags.div(
            ui.tags.i(class_="fa-solid fa-chart-line me-2"), "Sales Dashboard with Icon"
        )
    )

    @render.data_frame
    def summary_table():
        return (
            sales_df.groupby("Product")["Sales"]
            .agg(["count", "mean", "sum"])
            .reset_index()
        )


# Reactive Title with Current Time
with ui.card():

    @render.ui
    def time_based_title():
        current_time = datetime.now().strftime("%I:%M:%S %p")
        return ui.panel_title(f"Real-time Dashboard - {current_time}")

    @render.text
    def current_sales():
        return f"Total Sales: ${sales_df['Sales'].sum():.2f}"


# Add Font Awesome CSS for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">'
    )
)
