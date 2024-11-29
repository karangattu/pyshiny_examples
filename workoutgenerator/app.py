import random

from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Define some sample workout data
workouts = {
    "Cardio": ["Running", "Cycling", "Swimming", "Jumping Jacks", "Burpees"],
    "Strength": ["Squats", "Pushups", "Lunges", "Bicep Curls", "Shoulder Press"],
    "Flexibility": [
        "Yoga",
        "Stretching",
        "Pilates",
        "Foam Rolling",
        "Mobility Exercises",
    ],
}

app_ui = ui.page_fluid(
    ui.panel_title("Workout Routine Generator"),
    ui.layout_column_wrap(
        ui.input_selectize(
            "workout_type", "Workout Type", list(workouts.keys()), multiple=True
        ),
        ui.input_slider("duration", "Workout Duration (minutes)", 10, 120, 45),
        ui.input_checkbox("include_warmup", "Include Warm-up", True),
        ui.input_checkbox("include_cooldown", "Include Cool-down", True),
        width=1 / 2,
    ),
    ui.output_text_verbatim("routine"),
)


def server(input, output, session):
    @render.text
    def routine():
        workout_type = input.workout_type()
        duration = input.duration()
        include_warmup = input.include_warmup()
        include_cooldown = input.include_cooldown()

        routine_items = []
        if include_warmup:
            routine_items.append("Warm-up")

        for wtype in workout_type:
            exercises = random.sample(workouts[wtype], 2)
            routine_items.extend(exercises)

        if include_cooldown:
            routine_items.append("Cool-down")

        return "Your {}-minute workout routine:\n\n- {}".format(
            duration, "\n- ".join(routine_items)
        )


app = App(app_ui, server)
