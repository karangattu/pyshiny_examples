from shiny import reactive
from shiny.express import input, ui, render
import pandas as pd

ui.page_opts(title="File Upload Demo", fillable=True)

with ui.layout_columns():
    # Basic file input with single file
    with ui.card():
        ui.card_header("Basic File Upload")
        ui.input_file(
            "file1",
            "Choose CSV File",
            accept=[".csv"],
            multiple=False,
            button_label="Browse...",
            placeholder="No file selected",
        )

    # Multiple file input with various file types
    with ui.card():
        ui.card_header("Multiple File Types")
        ui.input_file(
            "file2",
            "Choose Multiple Files",
            accept=[".csv", ".txt", ".xlsx"],
            multiple=True,
            button_label="Select Files",
            placeholder="Upload multiple files",
        )

    # File input with camera capture
    with ui.card():
        ui.card_header("Camera Capture")
        ui.input_file(
            "file3",
            "Take Photo",
            accept=["image/*"],
            capture="user",
            button_label="Open Camera",
            placeholder="No photo taken",
        )

    # File input with custom width
    with ui.card():
        ui.card_header("Custom Width")
        ui.input_file(
            "file4",
            "Wide File Input",
            accept=[".csv"],
            width="100%",
            button_label="Select File",
            placeholder="Choose a file",
        )

# Display uploaded file information
with ui.layout_columns():
    with ui.card():
        ui.card_header("File 1 Info")

        @render.data_frame
        def file1_info():
            if not input.file1():
                # Create empty DataFrame if no file is uploaded
                return pd.DataFrame(columns=["Info", "Value"])

            file = input.file1()[0]
            data = {
                "Info": ["Name", "Size (bytes)", "Type"],
                "Value": [file["name"], file["size"], file["type"]],
            }
            return pd.DataFrame(data)

    with ui.card():
        ui.card_header("Multiple Files Info")

        @render.data_frame
        def file2_info():
            if not input.file2():
                return pd.DataFrame(columns=["Name", "Size", "Type"])

            files = input.file2()
            data = {
                "Name": [f["name"] for f in files],
                "Size": [f["size"] for f in files],
                "Type": [f["type"] for f in files],
            }
            return pd.DataFrame(data)

    with ui.card():
        ui.card_header("Camera Photo Info")

        @render.data_frame
        def file3_info():
            if not input.file3():
                return pd.DataFrame(columns=["Info", "Value"])

            file = input.file3()[0]
            data = {
                "Info": ["Name", "Size (bytes)", "Type"],
                "Value": [file["name"], file["size"], file["type"]],
            }
            return pd.DataFrame(data)

    with ui.card():
        ui.card_header("Wide Input File Info")

        @render.data_frame
        def file4_info():
            if not input.file4():
                return pd.DataFrame(columns=["Info", "Value"])

            file = input.file4()[0]
            data = {
                "Info": ["Name", "Size (bytes)", "Type"],
                "Value": [file["name"], file["size"], file["type"]],
            }
            return pd.DataFrame(data)
