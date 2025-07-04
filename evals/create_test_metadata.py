from shiny_test_generator import ShinyTestGenerator
from pathlib import Path
from itertools import islice
import json


def generate_shiny_test_metadata(
    apps_dir: str | Path = "evaluation_apps", max_tests: int = 10
) -> dict:
    """
    Generate Shiny tests and metadata for apps in the specified directory.

    Args:
        apps_dir: Directory containing Shiny apps
        max_tests: Maximum number of tests to generate

    Returns:
        Dictionary mapping test names to test metadata including code and app info
    """
    generator = ShinyTestGenerator()
    apps_dir = Path(apps_dir)

    app_files = islice(apps_dir.glob("*/app*.py"), max_tests)

    test_data = {}

    for app_path in app_files:
        print(f"Generating test for: {app_path}")
        try:
            test_code, test_file_path = generator.generate_test_from_file(str(app_path))
            print(f"Test code generated at: {test_file_path}")

            test_name = f"test_{app_path.parent.name}_{app_path.stem}"
            app_code = app_path.read_text(encoding="utf-8")

            test_data[test_name] = {
                "test_code": test_code,
                "app_code": app_code,
                "app_path": str(app_path),
                "test_file_path": test_file_path,
                "app_name": app_path.parent.name,
            }

        except Exception as e:
            print(f"Error generating test for {app_path}: {e}")
            continue

    return test_data


if __name__ == "__main__":
    test_data = generate_shiny_test_metadata()

    print(f"\nGenerated {len(test_data)} test(s)")
    print("Available tests:", list(test_data.keys()))

    output_dir = Path("generated_tests")
    output_dir.mkdir(exist_ok=True)

    for test_name, data in test_data.items():
        test_file = output_dir / f"{test_name}.py"
        test_file.write_text(data["test_code"], encoding="utf-8")
        print(f"Saved test to: {test_file}")

    metadata_file = output_dir / "test_metadata.json"
    with open(metadata_file, "w") as f:
        json.dump(test_data, f, indent=2)

    print(f"Saved test metadata to: {metadata_file}")