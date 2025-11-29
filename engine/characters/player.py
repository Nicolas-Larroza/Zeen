import random
import math
import engine.logic.inventory as inv
from .character_framework import Npc

from items import player_inventory
class Player(Npc):
    def __init__(self, name='Player', health=10, max_health = 10, alive=True, damage = 5, exp = 0, lvl = 1, defense = 0):
        super().__init__(health, alive)
        self.damage = damage
        self.exp = exp
        self.lvl = lvl
        self.defense = defense
        self.name = name
        self.max_health = max_health
    def attack(self, target : Npc):
        minimum_damage = math.ceil(self.damage * 0.6)
        damage_dealt = max(0,random.randint(minimum_damage, self.damage) - target.defense)
        print(f"player attacks! you deal {damage_dealt} damage!")
        target.take_damage(damage_dealt)
           
    def level_up(self):
        self.lvl += 1
        self.max_health += 1 + self.lvl
        self.health = self.max_health
        self.damage += 1 + (int(self.lvl // 1.5))
        self.defense += 1
        print(f"You leveled up! your level is now {self.lvl}!")
        
    def experience_for_next_level(self):
        return 100 * self.lvl
    
    def check_for_possible_level_up(self):
        if self.exp >= self.experience_for_next_level():
            self.level_up()
            self.exp = 0
    
    def equip_item(self, item):
        if item in player_inventory.items and item.equippable and not item.equipped:
            item.equipped = True
            self.damage += item.damage
            self.defense += item.defense
            print(f'{item} equipped!')
        else:
            if not item.equippable:
                print("you can't equip that!")
            elif item.equipped:
                print("you already have that equipped!")
    def unequip_item(self, item: inv.EquippableItem):
        try:
            if item in player_inventory.items and item.equippable and item.equipped:
                item.equipped = False
                self.damage -= item.damage
                self.defense -= item.defense
                print(f'{item} unequipped!')
        except AttributeError:
            print("Dont do that!")
        
    def see_stats(self):
        return f'health: {self.health} damage: {self.damage}, defense: {self.defense}, level: {self.lvl} '
    
            
player = Player()

from items import starter_pack
starter_pack(player)