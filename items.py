import json
from paths import ITEM_PATH
from engine.logic.inventory import Weapon, Armor, Potion, Inventory

with open(ITEM_PATH) as json_items:
    items = json.load(json_items)


objects = {}

for key, data in items.items():
    if "damage" in data and data["damage"] > 0:
        obj = Weapon(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            damage=data["damage"],
            defense=data['defense']
        )

    elif "defense" in data and data["defense"] > 0:
        obj = Armor(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            damage= data['damage'],
            defense=data["defense"]
        )

    elif "effect_amount" in data:
        obj = Potion(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            effect_amount=data["effect_amount"],
        )

    else:
        raise ValueError(f"Unknown item type: {key}")

    objects[key] = obj

player_inventory = Inventory()
def starter_pack(player):
    for objt in list(objects.values())[:5]:

        player_inventory.add_item(objt, notify=False)
        player.equip_item(objt)

    



    