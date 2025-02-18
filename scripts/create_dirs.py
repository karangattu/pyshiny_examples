import os
from pathlib import Path

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

# Create the "AIprentice" folder
aiprentice_dir = Path("AIprentice")
os.makedirs(aiprentice_dir, exist_ok=True)

for item in items:
    # Create folder for each item under AIprentice
    item_folder = aiprentice_dir / item
    os.makedirs(item_folder, exist_ok=True)

    # Create app.py file (if it doesn't exist)
    app_file = item_folder / "app.py"
    if not app_file.exists():
        app_file.touch()

    # Create PROMPT.md file (if it doesn't exist)
    prompt_file = item_folder / "PROMPT.md"
    if not prompt_file.exists():
        prompt_file.touch()

    # Create DESCRIPTION.md file (if it doesn't exist)
    description_file = item_folder / "DESCRIPTION.md"
    if not description_file.exists():
        description_file.touch()

    # Create requirements.txt file (if it doesn't exist)
    requirements_file = item_folder / "requirements.txt"
    if not requirements_file.exists():
        requirements_file.touch()

print("Folder structure and files created successfully!")
