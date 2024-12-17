import pandas as pd
import numpy as np
from datetime import datetime
from shiny import reactive
from shiny.express import input, ui, render


# Generate synthetic data for demonstration
def generate_synthetic_data(file_type):
    """Generate synthetic data based on file type."""
    if file_type == ".csv":
        return pd.DataFrame(
            {
                "Name": ["Alice", "Bob", "Charlie", "David"],
                "Age": [25, 30, 35, 40],
                "Salary": [50000, 60000, 75000, 90000],
            }
        )
    elif file_type == ".json":
        return {
            "employees": [
                {"name": "Alice", "role": "Developer"},
                {"name": "Bob", "role": "Manager"},
                {"name": "Charlie", "role": "Designer"},
            ]
        }
    elif file_type == ".txt":
        return "Sample text file content\nWith multiple lines\nDemonstrating text file upload"
    else:
        return None


# Page setup with full width and title
ui.page_opts(title="File Input Showcase", full_width=True)

# Add Font Awesome for icons
ui.head_content(
    ui.HTML(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">'
    )
)

# Sidebar with file input configuration
with ui.sidebar():
    # Comprehensive file input with multiple parameters
    ui.input_file(
        "file_upload",  # id
        "Upload File",  # label
        multiple=True,  # Allow multiple file uploads
        accept=[".csv", ".json", ".txt"],  # Accepted file types
        button_label="Browse Files",  # Custom button label
        placeholder="No file selected",  # Placeholder text
        width="100%",  # Full width input
    )

    # Additional configuration inputs
    ui.input_checkbox("show_details", "Show File Details", value=True)
    ui.input_radio_buttons(
        "display_mode", "Display Mode", ["Raw", "Formatted", "Preview"], selected="Raw"
    )

# Main content area with multiple rendering techniques
with ui.layout_columns():
    # File Information Card
    with ui.card(full_screen=True):
        ui.card_header("File Information")

        @render.text
        def file_info():
            file_list = input.file_upload()
            if not file_list:
                return "No files uploaded"

            info_text = []
            for file in file_list:
                info_text.append(f"Filename: {file['name']}")
                info_text.append(f"Size: {file['size']} bytes")
                info_text.append(f"Type: {file['type']}")

            return "\n".join(info_text)

    # File Content Display Card
    with ui.card(full_screen=True):
        ui.card_header("File Content")

        @render.text
        def file_content():
            file_list = input.file_upload()
            if not file_list:
                return "Upload a file to view content"

            # Only process the first file for demonstration
            file = file_list[0]
            file_type = file["name"].split(".")[-1]

            # Read file content based on display mode
            try:
                if input.display_mode() == "Raw":
                    with open(file["datapath"], "r") as f:
                        return f.read()

                data = generate_synthetic_data(f".{file_type}")

                if input.display_mode() == "Formatted":
                    return str(data)

                return "Preview mode not implemented"

            except Exception as e:
                return f"Error reading file: {str(e)}"

    # Conditional File Details Card
    with ui.card(full_screen=True):
        ui.card_header("File Details")

        @render.data_frame
        def file_details():
            if not input.show_details():
                return pd.DataFrame()

            file_list = input.file_upload()
            if not file_list:
                return pd.DataFrame()

            details = []
            for file in file_list:
                details.append(
                    {
                        "Name": file["name"],
                        "Size (bytes)": file["size"],
                        "Type": file["type"],
                        "Datapath": file["datapath"],
                    }
                )

            return pd.DataFrame(details)


# Footer with instructions
ui.markdown(
    """
### Instructions
1. Use the file input to upload CSV, JSON, or TXT files
2. Toggle file details visibility
3. Choose display mode for file content
4. Explore the different rendering options
"""
)
