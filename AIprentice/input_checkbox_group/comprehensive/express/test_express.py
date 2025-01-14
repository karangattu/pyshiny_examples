from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_checkbox_groups(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test cards
    card1 = controller.Card(page, "card1")
    card1.expect_header("Basic Checkbox Group")
    card1.expect_full_screen_available(True)

    card2 = controller.Card(page, "card2")
    card2.expect_header("Inline Checkbox Group")
    card2.expect_full_screen_available(True)

    card3 = controller.Card(page, "card3")
    card3.expect_header("Custom Width Checkbox Group")
    card3.expect_full_screen_available(True)

    summary_card = controller.Card(page, "summary_card")
    summary_card.expect_header("Summary of All Selections")

    # Test basic checkbox group
    basic_group = controller.InputCheckboxGroup(page, "basic_group")
    basic_group.expect_label("Choose colors:")
    basic_group.expect_choices(["red", "blue", "green", "purple"])
    basic_group.expect_selected(["red", "blue"])  # Test initial selection

    # Test basic group output
    basic_output = controller.OutputText(page, "basic_output")
    basic_output.expect_value("You selected: ('red', 'blue')")

    # Test inline checkbox group
    inline_group = controller.InputCheckboxGroup(page, "inline_group")
    inline_group.expect_label("Choose colors (inline):")
    inline_group.expect_choices(["red", "blue", "green", "purple"])
    inline_group.expect_selected(["green"])  # Test initial selection
    inline_group.expect_inline(True)

    # Test inline group output
    inline_output = controller.OutputText(page, "inline_output")
    inline_output.expect_value("You selected: ('green',)")

    # Test width checkbox group
    width_group = controller.InputCheckboxGroup(page, "width_group")
    width_group.expect_label("Choose colors (wider):")
    width_group.expect_choices(["red", "blue", "green", "purple"])
    width_group.expect_selected([])  # Test initial selection (empty)
    width_group.expect_width("400px")

    # Test width group output
    width_output = controller.OutputText(page, "width_output")
    width_output.expect_value("You selected: ()")

    # Test interactions
    # Change selections and verify outputs update
    basic_group.set(["red"])
    basic_output.expect_value("You selected: ('red',)")

    inline_group.set(["blue", "purple"])
    inline_output.expect_value("You selected: ('blue', 'purple')")

    width_group.set(["green"])
    width_output.expect_value("You selected: ('green',)")
