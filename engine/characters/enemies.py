import math
import random
from .character_framework import Npc
import engine.logic.inventory as inv
class Enemy(Npc):
    def __init__(self, health=20, alive=True, damage=1, defense=0, exp_give = 1, name ='dude'):
        super().__init__(health, alive)
        self.damage = damage
        self.defense = defense
        self.exp_give = exp_give
        self.name = name
    def attack(self, target : Npc):
       
        minimum_damage = math.ceil(self.damage * 0.6)
        #calculating damage dealt
        damage_dealt = max(0,random.randint(minimum_damage, self.damage) - target.defense)
        print(f"{self.name} attacks! It deals {damage_dealt} damage!")
        target.take_damage(damage_dealt)
    
    def give_exp(self, target):
        if not self.alive:
            target.exp += self.exp_give

class Goblin(Enemy):
    def __init__(self, health=10, alive=True, damage=3, defense = 1, exp_give=100, name = 'goblin'):
        super().__init__(health, alive, damage, defense, exp_give)
        self.name = name
class Zombie(Enemy):
    def __init__(self, health=20, alive=True, damage=6, defense = 3, exp_give=10, name = 'zombie'):
        super().__init__(health, alive, damage, defense, exp_give)
        self.name = name
        
def enemy_drop():
    if random.random() < 0.50:
        healing_potion = inv.HealingPotion('007', 'Healing potion', 'its a potion... that heals you... name is pretty self-explanatory.', 50)
        print("enemy dropped a Healing potion!")
        inv.player_inventory.add_item(healing_potion)
        
