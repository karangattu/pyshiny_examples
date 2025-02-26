from shiny import App, reactive, render, ui

# Define the UI
app_ui = ui.page_fillable(
    # Add Font Awesome to head
    ui.head_content(
        ui.HTML(
            '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">'
        )
    ),
    # Add title
    ui.h2("Dynamic Accordion Panel Demo"),
    # Add description
    ui.markdown(
        """
        Click the button below to add new panels to the accordion dynamically.
        Each new panel will have a star icon and custom content.
        """
    ),
    # Button to insert panels
    ui.input_action_button("add_panel", "Add New Panel", class_="btn-primary mb-3"),
    # Initial accordion setup
    ui.accordion(
        ui.accordion_panel(
            "Initial Panel",
            "This is the first panel with some initial content",
            value="panel1",
            icon=ui.HTML('<i class="fa-solid fa-home"></i>'),
        ),
        id="accordion_demo",
        open=True,
    ),
    # Output for panel counter
    ui.output_text("panel_counter"),
)


# Define the server
def server(input, output, session):
    # Counter to keep track of added panels
    panel_count = reactive.value(1)

    @reactive.effect
    @reactive.event(input.add_panel)
    def add_new_panel():
        current_count = panel_count.get()
        panel_count.set(current_count + 1)

        # Create new panel content
        new_panel = ui.accordion_panel(
            f"Panel {current_count + 1}",
            value=f"panel{current_count + 1}",
            icon=ui.HTML('<i class="fa-solid fa-star"></i>'),
        )

        # Insert the new panel
        ui.insert_accordion_panel(
            id="accordion_demo",
            panel=new_panel,
            target="panel1" if current_count == 1 else f"panel{current_count}",
            position="after",
        )

    @output
    @render.text
    def panel_counter():
        return f"Current number of panels: {panel_count.get()}"


# Create and return the app
app = App(app_ui, server)
