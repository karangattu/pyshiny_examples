from shiny import reactive
from shiny.express import input, ui, render

# Set page options for a clean layout
ui.page_opts(title="Panel Absolute Demo", fillable=True)

# Add a container with relative positioning to hold the absolute panels
with ui.tags.div(style="position: relative; height: 100vh;"):

    # Basic panel with top and left positioning
    with ui.panel_absolute(
        top="10px",
        left="10px",
        width="200px",
        height="100px",
        class_="bg-light border p-2",
    ):
        "Panel 1: Fixed position with top and left"

    # Panel with bottom and right positioning
    with ui.panel_absolute(
        bottom="10px",
        right="10px",
        width="200px",
        height="100px",
        class_="bg-light border p-2",
    ):
        "Panel 2: Fixed position with bottom and right"

    # Draggable panel with cursor style
    with ui.panel_absolute(
        top="150px",
        left="50%",
        width="200px",
        height="100px",
        draggable=True,
        cursor="move",
        class_="bg-light border p-2",
    ):
        "Panel 3: Draggable panel with move cursor"

    # Fixed panel that stays in view when scrolling
    with ui.panel_absolute(
        top="20px",
        right="20px",
        width="150px",
        height="80px",
        fixed=True,
        class_="bg-light border p-2",
    ):
        "Panel 4: Fixed position that stays when scrolling"

    # Panel with default cursor
    with ui.panel_absolute(
        bottom="150px",
        left="30px",
        width="200px",
        height="100px",
        cursor="default",
        class_="bg-light border p-2",
    ):
        "Panel 5: Panel with default cursor"

    # Panel with inherit cursor
    with ui.panel_absolute(
        top="50%",
        right="30px",
        width="200px",
        height="100px",
        cursor="inherit",
        class_="bg-light border p-2",
    ):
        "Panel 6: Panel with inherit cursor"

    # Panel with auto cursor (default)
    with ui.panel_absolute(
        top="40%",
        left="40%",
        width="200px",
        height="100px",
        cursor="auto",
        class_="bg-light border p-2",
    ):
        "Panel 7: Panel with auto cursor"

# Add some content for scrolling demonstration
with ui.tags.div(style="height: 2000px; padding: 20px;"):
    ui.markdown(
        """
    ## Scroll down to see fixed panel behavior
    
    The panel marked as 'fixed' will remain visible while scrolling this content.
    Other panels will scroll with the page content.
    """
    )
