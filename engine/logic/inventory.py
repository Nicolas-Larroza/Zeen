class Item:
    def __init__(self, id, name, description, ):
        self.id = id
        self.name = name
        self.description = description
    
    def see_information(self):
        return f"{self.description}"
        
    def __str__(self):
        return f"{self.name}"


class EquippableItem(Item):
    def __init__(self, id, name, description,damage, defense, equippable=True, equipped=False):
        super().__init__(id, name, description,)
        self.equippable = equippable
        self.equipped = equipped
        self.damage = damage
        self.defense = defense
    def see_information(self):
        return f"{self.description} damage: {self.damage}, defense: {self.defense}"
    def __str__(self):
        return f"{self.name}"

class Consumable(Item):
    def __init__(self, id, name, description, effect_amount):
        super().__init__(id, name, description)
        self.effect_amount = effect_amount

class Weapon(EquippableItem):
    pass
        
class Armor(EquippableItem):
    pass
        
    
class Inventory:
    def __init__(self):
        self.items = []
        
    
    def add_item(self, item : Item, notify=False):
        self.items.append(item)
        if notify:
            print(f'{item.name} added to inventory')
        
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
    def see_inventory(self):
        if not self.items:
            print('inventory is empty.')
        else:
            print('inventory:')
            for idx, item in enumerate(self.items, start=0):
                print(f"{idx}. {item}")


class Potion(Consumable):
    def __init__(self, id, name, description, effect_amount):
        super().__init__(id, name, description, effect_amount)
    def use(self, target):
        if "Heal" in self.name:
            target.health += self.effect_amount
            print(f"{target.name} used {self.name} and recovered {self.effect_amount} HP!")
        
        
        

