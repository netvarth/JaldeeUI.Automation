import json
from pathlib import Path


def load_json_test_data(file_name):
    """
    Loads test data from the data folder.

    Example:
        load_json_test_data("appointment_test_data.json")
    """

    file_path = Path("data") / file_name

    if not file_path.exists():
        raise FileNotFoundError(f"Test data file not found: {file_path}")

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)