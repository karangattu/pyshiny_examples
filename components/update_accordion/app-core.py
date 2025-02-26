from shiny import App, reactive, render, ui

app_ui = ui.page_fillable(
    # Add Font Awesome CSS for icons
    ui.head_content(
        ui.HTML('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">')
    ),
    
    ui.layout_column_wrap(
        # Create buttons panel
        ui.card(
            ui.card_header("Controls"),
            ui.input_action_button("update_all", "Update All Sections", class_="m-1"),
            ui.input_action_button("show_ac", "Show only A & C", class_="m-1"),
            ui.input_action_button("show_b", "Show only B", class_="m-1"),
            ui.input_action_button("show_none", "Collapse All", class_="m-1"),
            ui.input_action_button("show_all", "Expand All", class_="m-1")
        ),
        
        # Create accordion panel
        ui.card(
            ui.card_header("Accordion Demo"),
            ui.accordion(
                ui.accordion_panel("Section A", "Original content for Section A", value="sec_a"),
                ui.accordion_panel("Section B", "Original content for Section B", value="sec_b"),
                ui.accordion_panel("Section C", "Original content for Section C", value="sec_c"),
                id="acc",
                multiple=True
            )
        ),
        width=1/2
    ),
    
    ui.output_text("acc_state")
)

def server(input, output, session):
    # Effect to demonstrate updating content, title, and icon
    @reactive.effect
    @reactive.event(input.update_all)
    def _():
        # Update section A with new content, title and icon
        ui.update_accordion_panel(
            id="acc",
            target="sec_a",
            "Updated content for Section A",
            title="New Section A Title",
            icon=ui.tags.i(class_="fa-solid fa-star")
        )
        
        # Update section B with just new content
        ui.update_accordion_panel(
            id="acc",
            target="sec_b",
            "Updated content for Section B"
        )
        
        # Update section C with new content and value
        ui.update_accordion_panel(
            id="acc",
            target="sec_c", 
            "Updated content for Section C",
            value="sec_c_new"
        )

    # Effect to show only sections A and C
    @reactive.effect
    @reactive.event(input.show_ac)
    def _():
        ui.update_accordion("acc", show=["sec_a", "sec_c"])

    # Effect to show only section B
    @reactive.effect
    @reactive.event(input.show_b)
    def _():
        ui.update_accordion("acc", show="sec_b")

    # Effect to collapse all sections
    @reactive.effect
    @reactive.event(input.show_none)
    def _():
        ui.update_accordion("acc", show=False)

    # Effect to expand all sections
    @reactive.effect
    @reactive.event(input.show_all)
    def _():
        ui.update_accordion("acc", show=True)

    # Add output to show current accordion state
    @output
    @render.text
    def acc_state():
        return f"Current accordion state: {input.acc()}"

app = App(app_ui, server)