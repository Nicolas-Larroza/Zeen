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
        return f"{self.name} Equipped: {self.equipped}"

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

player_inventory = Inventory()

class HealingPotion(Consumable):
    def __init__(self, id, name, description, effect_amount):
        super().__init__(id, name, description, effect_amount)
    def use(self, target):
        target.health += self.effect_amount
        print(f"{target.name} used {self.name} and recovered {self.effect_amount} HP!")
        
        


bronze_sword = Weapon('001', 'Bronze Sword', 'a basic ass sword you can cut with.', 4, 0)
steel_sword = Weapon('002', "Steel Sword", ")", 10, 0)
bronze_helmet = Armor('003', 'Bronze helmet', 'a basic helmet to protect that brain of yours.',0, 1)
bronze_chestplate = Armor('004', 'Bronze chestplate', 'a basic chestplate to hide those nasty chest hairs.', 0, 4)
bronze_pants = Armor('005', 'Bronze pants', 'you can wear these!',0, 2)
bronze_feet = Armor('006', 'Bronze boots', 'to stop your socks from getting wet',0, 1 )
    
            

def starter_pack():
    player_inventory.add_item(bronze_sword)
    player_inventory.add_item(bronze_helmet)
    player_inventory.add_item(bronze_chestplate)
    player_inventory.add_item(bronze_pants)
    player_inventory.add_item(bronze_feet)

starter_pack()

