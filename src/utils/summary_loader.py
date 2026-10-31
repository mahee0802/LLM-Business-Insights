import json


def load_business_summary(file_path="data/processed/business_summary.json"):
    """
    Load the business summary JSON file.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)