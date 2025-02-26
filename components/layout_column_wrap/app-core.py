from shiny import App, reactive, render, ui

app_ui = ui.page_fillable(
    # Main layout using layout_column_wrap
    ui.layout_column_wrap(
        *[  # Create 6 cards with different content
            ui.card(
                ui.card_header(f"Card {i+1}"),
                ui.card_body(
                    # Different content based on even/odd cards
                    ui.markdown(
                        f"This is card number {i+1} with some basic content."
                        if i % 2 == 0
                        else f"""This is card number {i+1} with more content to demonstrate 
                        how the layout handles different content lengths.
                        
                        The layout_column_wrap component will ensure all cards have 
                        equal heights when heights_equal="all" is set.
                        
                        This helps maintain a consistent look across all columns."""
                    ),
                    # Add slider to each card
                    ui.input_slider(
                        f"slider_{i+1}", f"Slider {i+1}", min=0, max=100, value=50
                    ),
                    ui.output_text(f"value_{i+1}"),
                ),
                id=f"card_{i+1}",
            )
            for i in range(6)
        ],
        width="250px",  # Width of each column
        fixed_width=True,  # Fixed width columns
        heights_equal="all",  # All cards same height
        fill=True,  # Allow layout to grow/shrink
        fillable=True,  # Each element is wrapped in fillable container
        height="500px",  # Height of the layout
        min_height="200px",  # Minimum height
        max_height="800px",  # Maximum height
        gap="1rem",  # Gap between columns
        class_="my-layout",  # Custom CSS class
        id="demo_layout",  # Layout ID
    ),
    # Footer section
    ui.div(
        "This demo shows how layout_column_wrap can be used to create responsive grid layouts.",
        class_="mt-3 text-muted",
    ),
)


def server(input, output, session):
    # Create render functions for each slider value
    for i in range(6):

        @output
        @render.text
        def value(i=i):  # Use default argument to capture current value of i
            return f"Value: {input[f'slider_{i+1}']()}"

        # Dynamically set the output ID
        value.__name__ = f"value_{i+1}"


app = App(app_ui, server)
