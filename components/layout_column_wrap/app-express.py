from shiny import reactive
from shiny.express import input, ui, render

# Page options for better display
ui.page_opts(title="layout_column_wrap Demo", fillable=True)

# Example with all layout_column_wrap parameters
with ui.layout_column_wrap(
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
):
    # Create 6 cards with different content to demonstrate the layout
    for i in range(6):
        with ui.card(id=f"card_{i+1}"):
            ui.card_header(f"Card {i+1}")
            with ui.card_body():
                if i % 2 == 0:
                    # Even numbered cards have less content
                    ui.markdown(f"This is card number {i+1} with some basic content.")
                else:
                    # Odd numbered cards have more content
                    ui.markdown(
                        f"""This is card number {i+1} with more content to demonstrate 
                        how the layout handles different content lengths.
                        
                        The layout_column_wrap component will ensure all cards have 
                        equal heights when heights_equal="all" is set.
                        
                        This helps maintain a consistent look across all columns."""
                    )

                # Add some interactive elements
                ui.input_slider(
                    f"slider_{i+1}", f"Slider {i+1}", min=0, max=100, value=50
                )

                @render.text
                def value():
                    return f"Value: {input[f'slider_{i+1}']()}"


# Add a footer section outside the layout
ui.div(
    "This demo shows how layout_column_wrap can be used to create responsive grid layouts.",
    class_="mt-3 text-muted",
)
