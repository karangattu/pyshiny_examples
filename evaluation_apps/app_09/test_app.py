from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.pytest import create_app_fixture
from shiny.run import ShinyAppProc

app = create_app_fixture(["app.py"])


def test_select_and_output(page: Page, app: ShinyAppProc) -> None:
    page.goto(app.url)

    # Test input select
    select_input = controller.InputSelect(page, "select")
    select_input.expect_label("Select an option")
    select_input.expect_choices(["A", "B"])
    select_input.expect_choice_labels(["Option A", "Option B"])
    select_input.expect_selected(["A"])

    # Test output text initial state
    output_text = controller.OutputText(page, "selected_option")
    output_text.expect_value("You selected: A")

    # Test selecting option B
    select_input.set("B")
    select_input.expect_selected(["B"])
    output_text.expect_value("You selected: B")

    # Test selecting option A again
    select_input.set("A")
    select_input.expect_selected(["A"])
    output_text.expect_value("You selected: A")
