from engine.characters.enemies import Goblin, Zombie, enemy_drop, Dragon
from engine.characters.player import player
import time

def pick_enemy():
    if 0 <= player.lvl < 3 :
        enemy = Goblin()
        return enemy
    elif 3 <= player.lvl <6:
        enemy = Zombie()
        return enemy
    else:
        return Dragon()

def combat():
    enemy = pick_enemy()
    
    while player.is_alive() and enemy.is_alive(): 
        
        player.attack(enemy)
        time.sleep(0.5)
        if not enemy.is_alive():
            print(f'{enemy.name} is dead! {enemy.exp_give} experience awarded!')
            enemy.give_exp(player)
            player.check_for_possible_level_up()
            enemy_drop()
    
            if isinstance(enemy, Dragon):
                print("you defeated the dragon! you finished the game! you're still stuck in the dungeon though.")
                exit()
            break   
        else:
            enemy.attack(player)
            time.sleep(0.5)
   
        if not player.is_alive():
            print("you died!")
            break



        


