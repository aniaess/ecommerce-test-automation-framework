import json
from pathlib import Path

# Path to project root
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

def load_json(filename: str):
    """
    Loads JSON data from the data directory.

    Args:
        filename (str): JSON filename.

    Returns:
        dict: Loaded JSON data.
    """
    file_path = DATA_DIR / filename

    with open(file_path, encoding="utf-8") as file:
        return json.load(file)

def _get_data(filename: str, key: str):
    """
    Returns a specific dataset from a JSON file.

    Args:
        filename (str): JSON file name.
        key (str): Dataset key.

    Returns:
        dict | list: Requested data.
    """
    return load_json(filename)[key]

def get_user_login_data(user_key: str):
    return _get_data("users.json", user_key)

def get_products(products_key: str):
    return _get_data("products.json", products_key)

def get_checkout_data(user_key: str):
    return _get_data("checkout_data.json", user_key)

