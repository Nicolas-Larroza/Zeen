import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to items.json (adjust "../data" as needed)
ITEM_PATH = os.path.join(BASE_DIR, "..", "data", "items.json")
print(BASE_DIR)