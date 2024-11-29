from shiny import App, Inputs, Outputs, Session, reactive, render, ui

# Sample data
pet_types = ["Dog", "Cat", "Bird", "Hamster", "Rabbit"]
pet_names = {
    "Dog": ["Buddy", "Bella", "Max", "Lucy"],
    "Cat": ["Whiskers", "Mittens", "Simba", "Cleo"],
    "Bird": ["Tweety", "Polly", "Chirpy", "Feathers"],
    "Hamster": ["Hammy", "Nugget", "Peanut", "Buttercup"],
    "Rabbit": ["Thumper", "Bun Bun", "Hoppy", "Fluffy"],
}

app_ui = ui.page_fluid(
    ui.input_select("pet_type", "Pet Type", pet_types),
    ui.input_select("pet_name", "Pet Name", []),
    ui.output_text_verbatim("selected_pet"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @reactive.effect
    @reactive.event(input.pet_type)
    def update_pet_names():
        pet_type = input.pet_type()
        if pet_type:
            ui.update_select("pet_name", choices=pet_names[pet_type])
        else:
            ui.update_select("pet_name", choices=[])

    @render.text
    def selected_pet():
        pet_type = input.pet_type()
        pet_name = input.pet_name()
        if pet_type and pet_name:
            return f"You selected a {pet_type} named {pet_name}."
        else:
            return "Please select a pet type and name."


app = App(app_ui, server)
