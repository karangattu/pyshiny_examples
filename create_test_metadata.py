from shiny_test_generator import ShinyTestGenerator
from pathlib import Path
from itertools import islice


def generate_shiny_tests(
    apps_dir: str | Path = "evaluation_apps", max_tests: int = 10
) -> dict[str, str]:
    """
    Generate Shiny tests for apps in the specified directory.

    Args:
        apps_dir: Directory containing Shiny apps
        max_tests: Maximum number of tests to generate

    Returns:
        Dictionary mapping test names to test code
    """
    generator = ShinyTestGenerator()
    apps_dir = Path(apps_dir)

    app_files = islice(apps_dir.glob("*/app*.py"), max_tests)

    test_codes = {}

    for app_path in app_files:
        print(f"Generating test for: {app_path}")
        try:
            test_code, test_file_path = generator.generate_test_from_file(str(app_path))
            print(f"Test code generated at: {test_file_path}")

            # Create meaningful key based on app path
            test_name = f"test_{app_path.parent.name}_{app_path.stem}"
            test_codes[test_name] = test_code

        except Exception as e:
            print(f"Error generating test for {app_path}: {e}")
            continue

    return test_codes


if __name__ == "__main__":
    # Generate tests
    test_codes = generate_shiny_tests()

    print(f"\nGenerated {len(test_codes)} test(s)")
    print("Available tests:", list(test_codes.keys()))

    # # Example usage: Access specific test code
    # for test_name, test_code in test_codes.items():
    #     print(f"\n{test_name}:")
    #     print(f"  Code length: {len(test_code)} characters")
    #     # You can now use test_code directly or save to files

    # # Industry standard: Save test codes to files for later use
    # output_dir = Path("generated_tests")
    # output_dir.mkdir(exist_ok=True)

    # for test_name, test_code in test_codes.items():
    #     test_file = output_dir / f"{test_name}.py"
    #     test_file.write_text(test_code, encoding="utf-8")
    #     print(f"Saved test to: {test_file}")
