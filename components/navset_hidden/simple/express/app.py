import pandas as pd
from shiny import reactive
from shiny.express import input, render, ui

# Sample data
sales_data = pd.DataFrame(
    {
        "month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "revenue": [10000, 12000, 9000, 15000, 11000],
        "units": [100, 120, 90, 150, 110],
    }
)

ui.page_opts(title="Hidden Navigation Demo", fillable=True)

with ui.sidebar():
    ui.input_radio_buttons(
        "view_type",
        "Select View",
        choices=["Data Table", "Revenue Chart", "Units Chart"],
        selected="Data Table",
    )

with ui.navset_hidden(id="main_content"):
    # Panel for data table
    with ui.nav_panel(None, value="panel1"):

        @render.data_frame
        def data_table():
            return sales_data

    # Panel for revenue chart
    with ui.nav_panel(None, value="panel2"):

        @render.plot
        def revenue_plot():
            import matplotlib.pyplot as plt

            fig, ax = plt.subplots()
            ax.bar(sales_data["month"], sales_data["revenue"])
            ax.set_title("Monthly Revenue")
            ax.set_ylabel("Revenue ($)")
            return fig

    # Panel for units chart
    with ui.nav_panel(None, value="panel3"):

        @render.plot
        def units_plot():
            import matplotlib.pyplot as plt

            fig, ax = plt.subplots()
            ax.plot(sales_data["month"], sales_data["units"], marker="o")
            ax.set_title("Monthly Units Sold")
            ax.set_ylabel("Units")
            return fig


@reactive.effect
def _():
    selection = input.view_type()
    if selection == "Data Table":
        ui.update_navs("main_content", selected="panel1")
    elif selection == "Revenue Chart":
        ui.update_navs("main_content", selected="panel2")
    else:
        ui.update_navs("main_content", selected="panel3")
