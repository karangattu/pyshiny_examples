from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd
import numpy as np
import random


# Generate synthetic datasets
def generate_dataset(name):
    np.random.seed(hash(name) % 2**32)
    size = np.random.randint(50, 200)

    if name == "Iris":
        # Synthetic Iris-like dataset
        data = {
            "sepal_length": np.random.normal(5.5, 0.5, size),
            "sepal_width": np.random.normal(3, 0.4, size),
            "petal_length": np.random.normal(4, 0.5, size),
            "petal_width": np.random.normal(1.3, 0.2, size),
            "species": np.random.choice(["setosa", "versicolor", "virginica"], size),
        }
    elif name == "Stocks":
        # Synthetic stock price dataset
        data = {
            "symbol": np.random.choice(["AAPL", "GOOGL", "MSFT", "AMZN"], size),
            "price": np.random.uniform(50, 500, size),
            "volume": np.random.randint(1000, 100000, size),
            "change_percent": np.random.normal(0, 2, size),
        }
    else:  # Cars
        # Synthetic car dataset
        data = {
            "make": np.random.choice(["Toyota", "Ford", "Honda", "Tesla"], size),
            "model": np.random.choice(["Sedan", "SUV", "Truck", "Compact"], size),
            "mpg": np.random.normal(25, 5, size),
            "horsepower": np.random.normal(200, 50, size),
            "price": np.random.uniform(20000, 80000, size),
        }

    return pd.DataFrame(data)


# Available datasets
DATASETS = ["Iris", "Stocks", "Cars"]

# Page setup
ui.page_opts(title="Modal Remove Demo")

# Sidebar with dataset selection
with ui.sidebar():
    ui.input_select("dataset", "Select Dataset", DATASETS)
    ui.input_action_button("show_modal", "Show Dataset Info")
    ui.input_action_button("remove_modal", "Remove Modal")


# Main panel to display dataset
@render.data_frame
def dataset_table():
    df = generate_dataset(input.dataset())
    return df


# Show modal with dataset information
@reactive.effect
@reactive.event(input.show_modal)
def _():
    dataset = input.dataset()
    df = generate_dataset(dataset)

    # Create a modal with dataset details
    m = ui.modal(
        ui.markdown(f"### {dataset} Dataset Information"),
        f"Total rows: {len(df)}",
        f"Columns: {', '.join(df.columns)}",
        title=f"{dataset} Dataset Details",
        footer=ui.modal_button("Close"),
        easy_close=True,
    )
    ui.modal_show(m)


# Remove modal when remove button is clicked
@reactive.effect
@reactive.event(input.remove_modal)
def _():
    ui.modal_remove()
