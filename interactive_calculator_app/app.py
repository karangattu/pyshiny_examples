from shiny import App, Inputs, Outputs, Session, reactive, render, ui

app_ui = ui.page_fluid(
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Interactive Calculator"),
            ui.input_numeric("num1", "Number 1", value=0),
            ui.input_numeric("num2", "Number 2", value=0),
            ui.input_select(
                "operation",
                "Operation",
                ["Add", "Subtract", "Multiply", "Divide"],
                selected="add",
            ),
            ui.input_action_button("calculate", "Calculate"),
            ui.output_text("result"),
            width=4,
        )
    )
)


def server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.text
    @reactive.event(input.calculate)
    def result():
        try:
            num1 = int(input.num1())
            num2 = int(input.num2())
            operation = input.operation()
            print(num1, num2, operation)

            if operation == "Add":
                return f"{num1} + {num2} = {num1 + num2}"
            elif operation == "Subtract":
                return f"{num1} - {num2} = {num1 - num2}"
            elif operation == "Multiply":
                return f"{num1} * {num2} = {num1 * num2}"
            elif operation == "Divide":
                if num2 == 0:
                    return "Error: Division by zero"
                else:
                    return f"{num1} / {num2} = {num1 / num2}"
            else:
                return "Error: Invalid operation"
        except ValueError:
            return "Error: Invalid input"


app = App(app_ui, server)
