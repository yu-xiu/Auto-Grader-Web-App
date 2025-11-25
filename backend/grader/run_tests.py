import subprocess
import time
import pytest
import os
from pathlib import Path

TEST_FILE = "grader/test_knight_attack.py"
SUBMISSION = "grader/student_submission.py"

def run_test(test_name: str):
    """
    Runs a single pytest test function by name.
    Returns: dict {test, status, time_ms}
    """

    start = time.perf_counter()

    try:
        # subprocess isolates execution from server environment
        result = subprocess.run(
            ["pytest", TEST_FILE, "-q", "-k", test_name],
            capture_output=True,
            text=True,
            timeout=2  # 2-second timeout per test
        )

        elapsed = int((time.perf_counter() - start) * 1000)

        if result.returncode == 0:
            return {"test": test_name, "status": "PASS", "time_ms": elapsed}
        else:
            return {"test": test_name, "status": "FAIL", "time_ms": elapsed, "output": result.stderr}

    except subprocess.TimeoutExpired:
        return {"test": test_name, "status": "TIMEOUT (>2s)", "time_ms": 2000}


def run_all_tests():
    """
    Run all tests in test_knight_attack.py one by one.
    Stop and give 0 if submission has syntax errors.
    """

    # First: quick syntax check
    syntax_check = subprocess.run(
        ["python3", "-m", "py_compile", SUBMISSION],
        capture_output=True,
        text=True
    )
    if syntax_check.returncode != 0:
        return [{
            "test": "syntax_check",
            "status": "SYNTAX ERROR",
            "message": syntax_check.stderr
        }]

    # List of test_xx names
    tests = [
        "test_01",
        "test_02",
        "test_03",
        "test_04",
        "test_05",
        "test_06",
        "test_07",
        "test_08",
    ]

    results = []

    for test in tests:
        r = run_test(test)
        results.append(r)

    return results
