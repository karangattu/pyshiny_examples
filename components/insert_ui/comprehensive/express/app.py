from shiny import reactive
from shiny.express import input, render, ui
import pandas as pd

ui.page_opts(title="Insert UI Demo", fillable=True)

# Add Font Awesome for icons
ui.head_content(
    ui.HTML('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">')
)

with ui.layout_sidebar():
    with ui.sidebar():
        ui.h4("Insert UI Controls")
        
        ui.input_select(
            "selector",
            "Target Selector",
            choices={
                "#top": "Top Container",
                "#middle": "Middle Container",
                "#bottom": "Bottom Container"
            }
        )
        
        ui.input_select(
            "where",
            "Insert Position",
            choices={
                "beforeBegin": "Before Element",
                "afterBegin": "After Start",
                "beforeEnd": "Before End",
                "afterEnd": "After Element"
            }
        )
        
        ui.input_checkbox("multiple", "Insert to Multiple Elements", value=False)
        ui.input_checkbox("immediate", "Insert Immediately", value=False)
        
        ui.input_action_button(
            "insert_text", 
            "Insert Text",
            class_="btn-primary w-100 my-2"
        )
        
        ui.input_action_button(
            "insert_card", 
            "Insert Card",
            class_="btn-success w-100 my-2"
        )
        
        ui.input_action_button(
            "clear", 
            "Clear All",
            class_="btn-warning w-100 my-2"
        )

    # Main content area with target containers
    ui.div(
        ui.div(
            with ui.card(class_="bg-light"):
                ui.h4("Top Container", class_="card-title"),
            id="top",
            class_="my-3"
        ),
        ui.div(
            with ui.card(class_="bg-light"):
                ui.h4("Middle Container", class_="card-title"),
            id="middle",
            class_="my-3"
        ),
        ui.div(
            with ui.card(class_="bg-light"):
                ui.h4("Bottom Container", class_="card-title"),
            id="bottom",
            class_="my-3"
        )
    )

# Counter for unique IDs
counter = reactive.value(0)

@reactive.effect
@reactive.event(input.insert_text)
def insert_text():
    counter.set(counter.get() + 1)
    current_time = pd.Timestamp.now().strftime("%H:%M:%S")
    
    # Create text element with timestamp
    text_element = ui.p(
        ui.tags.i(class_="fa-solid fa-clock me-2"),
        f"Inserted text #{counter.get()} at {current_time}",
        class_="alert alert-info"
    )
    
    # Insert the element using specified parameters
    ui.insert_ui(
        text_element,
        selector=input.selector(),
        where=input.where(),
        multiple=input.multiple(),
        immediate=input.immediate()
    )

@reactive.effect
@reactive.event(input.insert_card)
def insert_card():
    counter.set(counter.get() + 1)
    
    # Create a card with random content
    with ui.hold() as card_element:
        with ui.card(class_="bg-success text-white"):
            ui.h5(f"Inserted Card #{counter.get()}", class_="card-title")
            ui.p(
                ui.tags.i(class_="fa-solid fa-star me-2"),
                "This is a dynamically inserted card!",
                class_="card-text"
            )
    
    # Insert the card using specified parameters
    ui.insert_ui(
        card_element,
        selector=input.selector(),
        where=input.where(),
        multiple=input.multiple(),
        immediate=input.immediate()
    )

@reactive.effect
@reactive.event(input.clear)
def clear_all():
    # Remove all dynamically inserted elements
    selectors = ["#top", "#middle", "#bottom"]
    for selector in selectors:
        ui.remove_ui(
            selector + " .alert, " + selector + " .card.bg-success",
            multiple=True,
            immediate=True
        )
    counter.set(0)