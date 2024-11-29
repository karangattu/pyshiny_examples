import random

import matplotlib.pyplot as plt
import pandas as pd
from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Generate some sample data
teams = ["Team A", "Team B", "Team C", "Team D"]
games_played = [random.randint(10, 30) for _ in range(4)]
wins = [random.randint(5, 25) for _ in range(4)]
losses = [game - win for game, win in zip(games_played, wins)]
points_for = [random.randint(500, 1000) for _ in range(4)]
points_against = [random.randint(500, 1000) for _ in range(4)]

data = pd.DataFrame(
    {
        "Team": teams,
        "Games Played": games_played,
        "Wins": wins,
        "Losses": losses,
        "Points For": points_for,
        "Points Against": points_against,
    }
)

app_ui = ui.page_fluid(
    ui.panel_title("Sports Analytics Dashboard"),
    ui.layout_column_wrap(
        ui.value_box(
            "Total Games Played",
            int(data["Games Played"].sum()),
            theme="bg-gradient-orange-red",
            showcase=ui.HTML('<i class="fas fa-calendar-alt"></i>'),
            width="100%",
        ),
        ui.value_box(
            "Total Wins",
            int(data["Wins"].sum()),
            theme="bg-gradient-green-blue",
            showcase=ui.HTML('<i class="fas fa-trophy"></i>'),
            width="100%",
        ),
        ui.value_box(
            "Total Losses",
            int(data["Losses"].sum()),
            theme="bg-gradient-red-pink",
            showcase=ui.HTML('<i class="fas fa-frown"></i>'),
            width="100%",
        ),
        ui.value_box(
            "Total Points For",
            int(data["Points For"].sum()),
            theme="bg-gradient-yellow-orange",
            showcase=ui.HTML('<i class="fas fa-chart-line"></i>'),
            width="100%",
        ),
        ui.value_box(
            "Total Points Against",
            int(data["Points Against"].sum()),
            theme="bg-gradient-purple-pink",
            showcase=ui.HTML('<i class="fas fa-chart-line"></i>'),
            width="100%",
        )
    ),
    ui.layout_column_wrap(
        ui.card(
            ui.card_header("Team Statistics"),
            ui.output_table("team_stats"),
            width="100%",
        ),
        ui.card(
            ui.card_header("Points For vs Points Against"),
            ui.output_plot("points_plot"),
            width="100%",
        )
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.table
    def team_stats():
        return data

    @render.plot
    def points_plot():
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(data["Points For"], data["Points Against"])
        ax.set_xlabel("Points For")
        ax.set_ylabel("Points Against")
        ax.set_title("Points For vs Points Against")
        return fig


app = App(app_ui, server)
