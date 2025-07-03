import subprocess
import tempfile
from pathlib import Path

from inspect_ai import Scorer, score


@score
class PytestScorer(Scorer):
    def __init__(self):
        pass

    def __call__(self, state, target, **kwargs):
        with tempfile.NamedTemporaryFile(
            mode="w+", suffix=".py", delete=False
        ) as temp_file:
            temp_file.write(state.completed)
            temp_file_path = Path(temp_file.name)

        try:
            # Install playwright browsers
            subprocess.run(["playwright", "install"], check=True, capture_output=True, text=True)
            result = subprocess.run(
                ["pytest", str(temp_file_path)],
                check=True,
                capture_output=True,
                text=True,
            )
            passed = True
            output = result.stdout
        except subprocess.CalledProcessError as e:
            passed = False
            output = e.stderr
        finally:
            temp_file_path.unlink()

        return {"passed": passed, "output": output}
