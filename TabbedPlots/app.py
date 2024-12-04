import numpy as np
import pandas as pd
from shiny import App, Inputs, Outputs, Session, render, ui

# Sample data for plots
df1 = pd.DataFrame({"x": np.random.normal(0, 1, 100), "y": np.random.normal(0, 1, 100)})

df2 = pd.DataFrame(
    {"a": np.random.randint(1, 11, 50), "b": np.random.randint(1, 11, 50)}
)

df3 = pd.DataFrame(
    {
        "fruit": np.random.choice(["apple", "banana", "orange"], 30),
        "count": np.random.randint(1, 11, 30),
    }
)

app_ui = ui.page_fluid(
    ui.navset_tab(
        ui.nav_panel("Scatter Plot", ui.output_plot("scatter_plot")),
        ui.nav_panel("Bar Plot", ui.output_plot("bar_plot")),
        ui.nav_panel("Pie Chart", ui.output_plot("pie_chart")),
        id="plot_tabs",
    )
)


def server(input, output, session):
    @render.plot
    def scatter_plot():
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        ax.scatter(df1["x"], df1["y"])
        ax.set_title("Scatter Plot")
        return fig

    @render.plot
    def bar_plot():
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        df2.plot(kind="bar", x="a", y="b", ax=ax)
        ax.set_title("Bar Plot")
        return fig

    @render.plot
    def pie_chart():
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        df3.groupby("fruit")["count"].sum().plot(kind="pie", ax=ax, autopct="%1.1f%%")
        ax.set_title("Pie Chart")
        return fig


app = App(app_ui, server)
