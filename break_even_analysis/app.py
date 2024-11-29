import matplotlib.pyplot as plt
import numpy as np
from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Define some sample data
fixed_costs = 10000
variable_cost_per_unit = 5
selling_price_per_unit = 15

app_ui = ui.page_fluid(
    ui.panel_title("Break-Even Analysis"),
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Input Parameters"),
            ui.input_numeric("fixed_costs", "Fixed Costs", fixed_costs, min=0),
            ui.input_numeric(
                "variable_cost_per_unit",
                "Variable Cost per Unit",
                variable_cost_per_unit,
                min=0,
            ),
            ui.input_numeric(
                "selling_price_per_unit",
                "Selling Price per Unit",
                selling_price_per_unit,
                min=0,
            ),
            width=1 / 2,
        ),
        ui.card(
            ui.card_header("Break-Even Analysis"),
            ui.output_text_verbatim("break_even_units_text"),  # Update ID
            ui.output_text_verbatim("break_even_revenue_text"),  # Update ID
            ui.output_plot("break_even_plot"),  # Add plot
            width=1 / 2,
        ),
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    @reactive.calc
    def break_even_units():
        fixed_costs = input.fixed_costs()
        variable_cost_per_unit = input.variable_cost_per_unit()
        selling_price_per_unit = input.selling_price_per_unit()

        if selling_price_per_unit > variable_cost_per_unit:
            return fixed_costs / (selling_price_per_unit - variable_cost_per_unit)
        else:
            return "N/A"

    @reactive.calc
    def break_even_revenue():
        fixed_costs = input.fixed_costs()
        variable_cost_per_unit = input.variable_cost_per_unit()
        selling_price_per_unit = input.selling_price_per_unit()

        if selling_price_per_unit > variable_cost_per_unit:
            return (
                fixed_costs
                + (fixed_costs / (selling_price_per_unit - variable_cost_per_unit))
                * variable_cost_per_unit
            )
        else:
            return "N/A"

    @render.text
    def break_even_units_text():
        units = break_even_units()
        if isinstance(units, str):
            return units
        else:
            return f"Break-even units: {units:.2f}"

    @render.text
    def break_even_revenue_text():
        revenue = break_even_revenue()
        if isinstance(revenue, str):
            return revenue
        else:
            return f"Break-even revenue: ${revenue:.2f}"

    @render.plot
    def break_even_plot():
        fixed_costs = input.fixed_costs()
        variable_cost_per_unit = input.variable_cost_per_unit()
        selling_price_per_unit = input.selling_price_per_unit()

        units = np.linspace(0, 1000, 100)
        revenue = selling_price_per_unit * units
        cost = fixed_costs + variable_cost_per_unit * units

        fig, ax = plt.subplots()
        ax.plot(units, revenue, label="Revenue")
        ax.plot(units, cost, label="Cost")
        ax.set_xlabel("Units")
        ax.set_ylabel("Amount ($)")
        ax.set_title("Break-Even Analysis")
        ax.legend()
        return fig


app = App(app_ui, server)
