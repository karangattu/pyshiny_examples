from shiny import App, ui

app_ui = ui.page_fillable(
    # Add a container with relative positioning to hold the absolute panels
    ui.tags.div(
        style="position: relative; height: 100vh;",
        # Basic panel with top and left positioning
        ui.panel_absolute(
            "Panel 1: Fixed position with top and left",
            top="10px",
            left="10px",
            width="200px",
            height="100px",
            class_="bg-light border p-2",
        ),
        
        # Panel with bottom and right positioning
        ui.panel_absolute(
            "Panel 2: Fixed position with bottom and right",
            bottom="10px",
            right="10px",
            width="200px",
            height="100px",
            class_="bg-light border p-2",
        ),
        
        # Draggable panel with cursor style
        ui.panel_absolute(
            "Panel 3: Draggable panel with move cursor",
            top="150px",
            left="50%",
            width="200px",
            height="100px",
            draggable=True,
            cursor="move",
            class_="bg-light border p-2",
        ),
        
        # Fixed panel that stays in view when scrolling
        ui.panel_absolute(
            "Panel 4: Fixed position that stays when scrolling",
            top="20px",
            right="20px",
            width="150px",
            height="80px",
            fixed=True,
            class_="bg-light border p-2",
        ),
        
        # Panel with default cursor
        ui.panel_absolute(
            "Panel 5: Panel with default cursor",
            bottom="150px",
            left="30px",
            width="200px",
            height="100px",
            cursor="default",
            class_="bg-light border p-2",
        ),
        
        # Panel with inherit cursor
        ui.panel_absolute(
            "Panel 6: Panel with inherit cursor",
            top="50%",
            right="30px",
            width="200px",
            height="100px",
            cursor="inherit",
            class_="bg-light border p-2",
        ),
        
        # Panel with auto cursor (default)
        ui.panel_absolute(
            "Panel 7: Panel with auto cursor",
            top="40%",
            left="40%",
            width="200px",
            height="100px",
            cursor="auto",
            class_="bg-light border p-2",
        ),
    ),
    
    # Add some content for scrolling demonstration
    ui.tags.div(
        ui.markdown(
            """
            ## Scroll down to see fixed panel behavior
            
            The panel marked as 'fixed' will remain visible while scrolling this content.
            Other panels will scroll with the page content.
            """
        ),
        style="height: 2000px; padding: 20px;"
    ),
)

def server(input, output, session):
    pass

app = App(app_ui, server)