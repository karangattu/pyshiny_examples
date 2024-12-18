from shiny import reactive
from shiny.express import input, ui, render

# Set page title
ui.page_opts(title="Action Button Demo")

# Create action buttons
ui.input_action_button("btn1", "Click me!", class_="btn-primary me-2")
ui.input_action_button("btn2", "Reset", class_="btn-warning")


# Display click counts
@render.text
def click_count1():
    return f"Button 1 has been clicked {input.btn1()} times"


@render.text
def click_count2():
    return f"Button 2 has been clicked {input.btn2()} times"


# Create a reactive value to store some data
data = reactive.value(100)


# Reset data when button 2 is clicked
@reactive.effect
@reactive.event(input.btn2)
def _():
    data.set(100)


# Update data when button 1 is clicked
@reactive.effect
@reactive.event(input.btn1)
def _():
    current = data.get()
    data.set(current + 10)


# Display the current data value
@render.text
def current_value():
    return f"Current value: {data.get()}"
