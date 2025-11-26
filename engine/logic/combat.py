from engine.characters.enemies import Goblin, Zombie, enemy_drop
from engine.characters.player import player
import time
def pick_enemy():
    if 0 <= player.lvl < 3 :
        enemy = Goblin()
        return enemy
    elif 3 <= player.lvl <6:
        enemy = Zombie()
        return enemy

def combat():
    enemy = pick_enemy()
    
    while player.is_alive() and enemy.is_alive():
        
        
        player.attack(enemy)
        time.sleep(1.3)
        if not enemy.is_alive():
            print(f'{enemy.name} is dead! {enemy.exp_give} experience awarded!')
            enemy.give_exp(player)
            player.check_for_possible_level_up()
            enemy_drop()
            break #end the encounter
            
        else:
            enemy.attack(player)
            time.sleep(1.3)
        if not player.is_alive():
            print("you died!")
            break # end the encounter



        


