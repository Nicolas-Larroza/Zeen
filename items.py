import json
from paths import ITEM_PATH
with open(ITEM_PATH) as json_items:
    items = json.load(json_items)
    
    