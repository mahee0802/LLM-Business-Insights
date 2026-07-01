import json
def load_business_summary(file_path="outputs/business_summary.json"):
    """
    Load the business summary JSON file.
    """

    with open(file_path, "r") as file:
        business_summary = json.load(file)

    return business_summary