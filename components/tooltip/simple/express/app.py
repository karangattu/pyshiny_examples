from shiny import reactive
from shiny.express import input, render, ui

# Page options and title
ui.page_opts(title="Tooltip Demo", fillable=True)

# Add Font Awesome CSS for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
    )
)

# Create some sample data
sales_data = {"Q1": 150000, "Q2": 180000, "Q3": 220000, "Q4": 250000}

# Create a card with tooltips
with ui.card():
    ui.card_header("Sales Performance")

    with ui.tooltip(id="info_tooltip", placement="right"):
        ui.span(
            ui.tags.i(class_="fa-solid fa-circle-info", style="color: #447099;"),
            style="cursor: pointer;",
        )
        "Click on any quarter to see detailed information"

    with ui.layout_column_wrap(width=1 / 2):
        for quarter, amount in sales_data.items():
            with ui.tooltip(id=f"tooltip_{quarter.lower()}", placement="top"):
                ui.input_action_button(
                    f"btn_{quarter.lower()}",
                    f"{quarter}: ${amount:,}",
                    class_="btn-info w-100 mb-3",
                )
                f"Sales for {quarter}: ${amount:,}\nClick for details"


# Show notification when buttons are clicked
@reactive.effect
def handle_clicks():
    for quarter in sales_data.keys():
        btn_id = f"btn_{quarter.lower()}"
        if input[btn_id]():
            ui.notification_show(
                f"Detailed report for {quarter} is being generated...",
                type="message",
                duration=3,
            )
