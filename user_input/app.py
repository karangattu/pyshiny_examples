from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Made-up data
data = {
    "apple": {"price": 1.99, "quantity": 50},
    "banana": {"price": 0.79, "quantity": 30},
    "orange": {"price": 2.49, "quantity": 20},
    "grape": {"price": 3.99, "quantity": 15},
}

app_ui = ui.page_fluid(
    ui.input_text("product", "Enter a product:", "apple"),
    ui.output_text_verbatim("product_info"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.text
    @reactive.event(input.product)
    def product_info():
        product = input.product().lower()
        if product in data:
            return f"""
                Product: {product.capitalize()}
                Price: ${data[product]['price']:.2f}
                Quantity: {data[product]['quantity']}
            """
        else:
            return f"No information available for '{product}'"


app = App(app_ui, server)
