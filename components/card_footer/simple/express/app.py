from shiny import reactive
from shiny.express import input, ui, render

ui.page_opts(title="Card Footer Demo", fillable=True)

# Sample data
sales_data = {"Q1": 125000, "Q2": 165000, "Q3": 185000, "Q4": 215000}


# Define render functions outside of UI layout
@render.text
def projected_sales():
    base_sales = sales_data[input.quarter()]
    growth = input.growth() / 100
    return f"${base_sales * (1 + growth):,.2f}"


with ui.layout_column_wrap(width=1 / 2):
    # First card with a static footer
    with ui.card():
        ui.card_header("Quarterly Sales")
        ui.h3(f"${sum(sales_data.values()):,}")
        ui.card_footer(
            ui.div(
                {"class": "d-flex justify-content-between align-items-center"},
                ui.p("Total Annual Sales", class_="m-0"),
                ui.span(f"{len(sales_data)} Quarters", class_="text-muted"),
            )
        )

    # Second card with a dynamic footer based on user input
    with ui.card():
        ui.card_header("Sales Calculator")
        ui.input_select(
            "quarter", "Select Quarter", choices=list(sales_data.keys()), selected="Q1"
        )
        ui.input_numeric("growth", "Growth Percentage", value=10, min=0, max=100)

        # projected_sales()

        ui.card_footer(
            ui.div(
                {"class": "d-flex justify-content-between align-items-center"},
                ui.p("Projected Sales", class_="m-0"),
            )
        )

        @render.ui
        def footer_details():
            return ui.span(
                f"Base: ${sales_data[input.quarter()]:,}", class_="text-muted"
            )
