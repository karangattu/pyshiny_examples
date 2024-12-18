import pandas as pd

from shiny import reactive
from shiny.express import input, render, ui
from shiny.types import FileInfo

ui.page_opts(title="File Upload Demo", fillable=True)

with ui.layout_sidebar():
    with ui.sidebar():
        ui.input_file("file1", "Upload CSV File", accept=[".csv"], multiple=False)
        ui.input_checkbox_group(
            "stats",
            "Choose Statistics to Display",
            choices=["Row Count", "Column Count", "Column Names", "Data Preview"],
            selected=["Row Count", "Column Count"],
        )

    @render.data_frame
    def file_stats():
        # Create empty DataFrame if no file uploaded
        if not input.file1():
            return pd.DataFrame(
                {"Statistic": ["Please upload a file to see statistics"], "Value": [""]}
            )

        # Get file info
        file: list[FileInfo] = input.file1()

        # Create sample data since we're not reading actual files
        sample_data = pd.DataFrame(
            {
                "Name": ["John", "Alice", "Bob", "Carol"],
                "Age": [25, 30, 35, 28],
                "City": ["New York", "London", "Paris", "Tokyo"],
                "Salary": [50000, 60000, 75000, 65000],
            }
        )

        # Initialize stats dictionary
        stats = {}
        selected_stats = input.stats()

        if "Row Count" in selected_stats:
            stats["Row Count"] = len(sample_data)

        if "Column Count" in selected_stats:
            stats["Column Count"] = len(sample_data.columns)

        if "Column Names" in selected_stats:
            stats["Column Names"] = ", ".join(sample_data.columns)

        # Convert stats to DataFrame for display
        stats_df = pd.DataFrame({"Statistic": stats.keys(), "Value": stats.values()})

        return stats_df

    # Show data preview if selected
    @render.data_frame
    def data_preview():
        if not input.file1() or "Data Preview" not in input.stats():
            return pd.DataFrame()

        # Create sample data
        sample_data = pd.DataFrame(
            {
                "Name": ["John", "Alice", "Bob", "Carol"],
                "Age": [25, 30, 35, 28],
                "City": ["New York", "London", "Paris", "Tokyo"],
                "Salary": [50000, 60000, 75000, 65000],
            }
        )

        return sample_data
