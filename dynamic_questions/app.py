from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Define the quiz questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris",
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Jupiter",
    },
    {
        "question": "What is the currency used in Japan?",
        "options": ["Dollar", "Euro", "Yen", "Pound"],
        "answer": "Yen",
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Michelangelo", "Van Gogh", "Leonardo da Vinci", "Rembrandt"],
        "answer": "Leonardo da Vinci",
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean",
    },
]

app_ui = ui.page_fluid(
    ui.panel_title("Quiz App"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_action_button("next_button", "Next Question"),
            ui.input_action_button("reset_button", "Reset Quiz"),
        ),
        ui.div(
            ui.output_ui("question_container"),
            ui.output_ui("options_container"),
            ui.output_ui("result_container"),
        ),
    ),
)


def server(input, output, session):
    # Create a reactive value for tracking the current question index
    current_question_index = reactive.Value(0)

    @reactive.effect
    @reactive.event(input.reset_button)
    def _():
        current_question_index.set(0)

    @reactive.effect
    @reactive.event(input.next_button)
    def _():
        current_index = current_question_index()
        if current_index < len(quiz_data) - 1:
            current_question_index.set(current_index + 1)
        else:
            current_question_index.set(len(quiz_data))

    @render.ui
    def question_container():
        current_index = current_question_index()
        if current_index < len(quiz_data):
            return ui.p(quiz_data[current_index]["question"])
        else:
            return ui.p("Quiz completed!")

    @render.ui
    def options_container():
        current_index = current_question_index()
        if current_index < len(quiz_data):
            options = quiz_data[current_index]["options"]
            return ui.input_radio_buttons("answer", "Choose an answer:", options)
        else:
            return ui.p("")

    @render.ui
    def result_container():
        current_index = current_question_index()
        if current_index < len(quiz_data):
            selected_answer = input.answer()
            correct_answer = quiz_data[current_index]["answer"]
            if selected_answer == correct_answer:
                return ui.p("Correct!")
            else:
                return ui.p(f"Incorrect. The correct answer is {correct_answer}.")
        else:
            return ui.p("")


app = App(app_ui, server)
