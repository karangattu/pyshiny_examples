from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_layout_column_wrap_demo(page: Page, local_app: ShinyAppProc) -> None:
    page.goto(local_app.url)

    # Test each card
    for i in range(6):
        card = controller.Card(page, f"card_{i+1}")

        # Test card header
        card.expect_header(f"Card {i+1}")

        # Test card height (all cards should have same height due to heights_equal="all")
        card.expect_height("500px")  # This matches the layout height

        # Test card body exists
        if i % 2 == 0:
            # Even numbered cards have shorter content
            card.expect_body(
                "This is card number " + str(i + 1) + " with some basic content."
            )
        else:
            # Odd numbered cards have longer content
            expected_text = (
                f"This is card number {i+1} with more content to demonstrate "
                "how the layout handles different content lengths. "
                "The layout_column_wrap component will ensure all cards have "
                'equal heights when heights_equal="all" is set. '
                "This helps maintain a consistent look across all columns."
            )
            card.expect_body(expected_text)

        # Test sliders in each card
        slider = controller.InputSlider(page, f"slider_{i+1}")
        slider.expect_label(f"Slider {i+1}")
        slider.expect_min("0")
        slider.expect_max("100")
        slider.expect_value("50")  # Default value

        # Test setting new slider values
        slider.set("75")
        slider.expect_value("75")
