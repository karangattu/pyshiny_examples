import pytest


@pytest.fixture(autouse=True)
def test_stats():
    yield
    passed = getattr(pytest, "_passed", 0)
    total = getattr(pytest, "_total", 0)
    if total:
        percentage = (passed / total) * 100
        print(f"\nPassing percentage: {percentage:.2f}%")


def pytest_runtest_call():
    pytest._total = getattr(pytest, "_total", 0) + 1


def pytest_runtest_logreport(report):
    if report.when == "call" and report.outcome == "passed":
        pytest._passed = getattr(pytest, "_passed", 0) + 1
