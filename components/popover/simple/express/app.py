from shiny import reactive
from shiny.express import input, render, ui

ui.page_opts(title="Popover Demo", fillable=True)

# Add Font Awesome CSS for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">'
    )
)

# Sample data
sales_data = {"Q1": 150000, "Q2": 180000, "Q3": 220000, "Q4": 250000}

with ui.layout_column_wrap(width=1 / 2):
    with ui.card():
        with ui.card_header():
            "Sales Performance"
            with ui.popover(placement="right", id="sales_info"):
                ui.span(
                    ui.tags.i(
                        class_="fa-solid fa-circle-info", style="cursor: pointer;"
                    )
                )
                "Click on any quarter to see detailed information"
                ui.input_select("metric", "View Metric", ["Revenue", "Growth Rate"])

        with ui.popover(id="q1_pop"):
            ui.tags.button(f"Q1: ${sales_data['Q1']:,}", class_="btn btn-primary m-2")
            "Q1 Performance Details"
            ui.tags.ul(
                [
                    ui.tags.li("January: $45,000"),
                    ui.tags.li("February: $48,000"),
                    ui.tags.li("March: $57,000"),
                ]
            )

        with ui.popover(id="q2_pop"):
            ui.tags.button(f"Q2: ${sales_data['Q2']:,}", class_="btn btn-info m-2")
            "Q2 Performance Details"
            ui.tags.ul(
                [
                    ui.tags.li("April: $58,000"),
                    ui.tags.li("May: $62,000"),
                    ui.tags.li("June: $60,000"),
                ]
            )

        @render.text
        def selected_metric():
            return f"Currently viewing: {input.metric()}"

    with ui.card():
        with ui.card_header():
            "Help & Documentation"

        with ui.popover(id="help_pop", placement="left"):
            ui.tags.button("Need Help?", class_="btn btn-secondary")
            ui.markdown(
                """
            ### Quick Help Guide
            
            * Use the dropdown to switch metrics
            * Click on quarter buttons for details
            * Data is updated in real-time
            """
            )

ui.input_action_button("show_all", "Show All Popovers", class_="mt-3")


@reactive.effect
@reactive.event(input.show_all)
def _():
    ui.update_popover("q1_pop", show=True)
    ui.update_popover("q2_pop", show=True)
    ui.update_popover("help_pop", show=True)
    ui.update_popover("sales_info", show=True)
