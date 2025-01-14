from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_file_input_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test file input component
    file_input = controller.InputFile(page, "file1")

    # Test initial state
    file_input.expect_label("Upload File")
    file_input.expect_multiple(True)
    file_input.expect_accept(
        [".csv", ".txt", "text/plain", "application/pdf", "image/*"]
    )
    file_input.expect_button_label("Choose Files...")
    file_input.expect_width("400px")
    file_input.expect_capture("user")

    # Test data frame output initial state
    file_table = controller.OutputDataFrame(page, "file_table")
    file_table.expect_column_labels(["Name", "Size (bytes)", "Type"])
    file_table.expect_nrow(0)
    file_table.expect_ncol(3)

    # Test file upload
    # Note: You'll need to create a temporary test file for this
    file_input.set("test.csv")
    file_input.expect_complete()

    # After upload, check if table is updated
    file_table.expect_nrow(1)  # Should show one row for the uploaded file
    file_table.expect_ncol(3)  # Should still have 3 columns
