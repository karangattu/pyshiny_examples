from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_selectize_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test the selectize input
    state_select = controller.InputSelectize(page, "state")
    selection_output = controller.OutputText(page, "selection")

    # Test initial state
    state_select.expect_label("Choose state(s):")
    state_select.expect_multiple(True)
    state_select.expect_selected(["NY", "CA"])

    # Test choices structure
    state_select.expect_choice_groups(["East Coast", "West Coast", "Midwest"])
    state_select.expect_choice_labels(
        [
            "New York",
            "New Jersey",
            "Connecticut",
            "Washington",
            "Oregon",
            "California",
            "Minnesota",
            "Wisconsin",
            "Iowa",
        ]
    )
    state_select.expect_choices(["NY", "NJ", "CT", "WA", "OR", "CA", "MN", "WI", "IA"])

    # Test initial output
    selection_output.expect_value("You selected: NY, CA")

    # Test changing selection
    state_select.set(["MN", "WI"])
    selection_output.expect_value("You selected: MN, WI")

    # Test clearing selection
    state_select.loc.locator("..").locator(
        "> div.plugin-clear_button > a.clear"
    ).click()  # Clear all selections
    state_select.expect_selected([])
    selection_output.expect_value("No states selected")

    # Test selecting a single state
    state_select.set(["WA"])
    selection_output.expect_value("You selected: WA")
