import os

items = [
    "accordion_panel",
    "accordion",
    "busy_indicators.options",
    "card_footer",
    "card_header",
    "card",
    "Chat",
    "include_css",
    "include_js",
    "input_action_button",
    "input_action_link",
    "input_checkbox_group",
    "input_checkbox",
    "input_dark_mode",
    "input_date_range",
    "input_date",
    "input_file",
    "input_numeric",
    "input_password",
    "input_radio_buttons",
    "input_select",
    "input_selectize",
    "input_slider",
    "input_switch",
    "input_task_button",
    "input_text_area",
    "input_text",
    "insert_accordion_panel",
    "insert_ui",
    "layout_column_wrap",
    "layout_columns",
    "layout_sidebar",
    "markdown",
    "modal_button",
    "modal_remove",
    "modal_show",
    "modal",
    "nav_menu",
    "nav_panel",
    "navset_bar",
    "navset_card_pill",
    "navset_card_tab",
    "navset_card_underline",
    "navset_hidden",
    "navset_pill_list",
    "navset_pill",
    "navset_tab",
    "navset_underline",
    "notification_show",
    "page_opts",
    "panel_absolute",
    "panel_conditional",
    "panel_title",
    "popover",
    "Progress",
    "remove_accordion_panel",
    "remove_ui",
    "sidebar",
    "TagList",
    "Theme",
    "tooltip",
    "update_accordion_panel",
    "update_accordion",
    "update_action_button",
    "update_action_link",
    "update_checkbox_group",
    "update_checkbox",
    "update_date_range",
    "update_date",
    "update_navs",
    "update_numeric",
    "update_popover",
    "update_radio_buttons",
    "update_select",
    "update_selectize",
    "update_sidebar",
    "update_slider",
    "update_text_area",
    "update_text",
    "update_tooltip",
    "value_box",
]

# Create the "components" folder
os.makedirs("components", exist_ok=True)

for item in items:
    # Create folder for each item
    item_folder = os.path.join("components", item)
    os.makedirs(item_folder, exist_ok=True)

    # Create "simple" and "comprehensive" folders
    simple_folder = os.path.join(item_folder, "simple")
    comprehensive_folder = os.path.join(item_folder, "comprehensive")
    os.makedirs(simple_folder, exist_ok=True)
    os.makedirs(comprehensive_folder, exist_ok=True)

    # Create "express" folder under "simple" and "comprehensive"
    simple_express_folder = os.path.join(simple_folder, "express")
    comprehensive_express_folder = os.path.join(comprehensive_folder, "express")
    os.makedirs(simple_express_folder, exist_ok=True)
    os.makedirs(comprehensive_express_folder, exist_ok=True)

    # Create PROMPT.md files
    simple_prompt_path = os.path.join(simple_express_folder, "PROMPT.md")
    comprehensive_prompt_path = os.path.join(comprehensive_express_folder, "PROMPT.md")

    with open(simple_prompt_path, "w") as f:
        f.write(
            f"write a really simple shiny for python app that shows the use of {item} using express mode"
        )

    with open(comprehensive_prompt_path, "w") as f:
        f.write(
            f"can you make a shiny for python app that uses all the possible parameters of the {item} using express mode"
        )

print("Folder structure and files created successfully!")
