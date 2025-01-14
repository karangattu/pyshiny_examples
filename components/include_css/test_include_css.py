# Modified version with IDs
ui.p("This text uses the 'custom-text' class", id="custom_text_p", class_="custom-text")

with ui.div(id="custom_box_div", class_="custom-box"):
    "This content is in a custom box"

with ui.div(id="custom_border_div", class_="custom-border"):
    "This content has a custom border"
