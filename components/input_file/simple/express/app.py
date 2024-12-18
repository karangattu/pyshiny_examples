import pandas as pd
import numpy as np
from shiny import reactive
from shiny.express import input, ui, render
from shiny.types import FileInfo

# Page setup
ui.page_opts(title="File Upload Demo")

# Sidebar with file upload
with ui.sidebar():
    ui.input_file(
        "file1",
        "Choose CSV File",
        accept=[".csv"],
        multiple=False,
        button_label="Browse...",
        placeholder="No file selected",
    )

    ui.input_checkbox_group(
        "stats",
        "Summary Stats",
        choices=["Row Count", "Column Count", "Column Names", "Data Preview"],
        selected=["Row Count", "Column Count", "Column Names", "Data Preview"],
    )


# Function to generate synthetic data
def generate_synthetic_data():
    """Generate a sample DataFrame for demonstration."""
    np.random.seed(42)
    data = {
        "Name": [f"Person_{i}" for i in range(100)],
        "Age": np.random.randint(18, 80, 100),
        "Income": np.random.normal(50000, 15000, 100).round(2),
        "Education": np.random.choice(
            ["High School", "Bachelor", "Master", "PhD"], 100
        ),
    }
    return pd.DataFrame(data)


# Reactive calculation for parsed file
@reactive.calc
def parsed_file():
    file: list[FileInfo] | None = input.file1()

    # If no file uploaded, return synthetic data
    if file is None:
        return generate_synthetic_data()

    # If a file is uploaded, read the CSV
    return pd.read_csv(file[0]["datapath"])


# Render summary table based on selected stats
@render.table
def summary():
    df = parsed_file()

    # Get the selected stats
    selected_stats = input.stats()

    # Create a summary DataFrame based on selected stats
    info_df = pd.DataFrame()

    if "Row Count" in selected_stats:
        info_df["Row Count"] = [df.shape[0]]

    if "Column Count" in selected_stats:
        info_df["Column Count"] = [df.shape[1]]

    if "Column Names" in selected_stats:
        info_df["Column Names"] = [", ".join(df.columns.tolist())]

    if "Data Preview" in selected_stats:
        info_df["First 5 Rows"] = [df.head().to_string()]

    return info_df


# Render the full data table
@render.data_frame
def full_table():
    return render.DataGrid(
        parsed_file(), height=300, width="100%", selection_mode="row"
    )
