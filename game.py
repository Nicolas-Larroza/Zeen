from engine.characters.player import player, Player
import random
import engine.logic.inventory as inv
from engine.logic.combat import combat
from items import player_inventory
def explore():
    print("you venture deeper...")
    if random.random() < 0.90:
        combat()
    else:
        print('seems quiet... you rest and replenish your health.')
        player.health = player.max_health
#I'll use depth at some point... probably :p
depth = 0
print("you wake up, disoriented. you examine your surroundings. you appear to be in some sort of dungeon, with no way out. near you, there appears to be the remnants of \na past adventurer. you take his rusty gear, and venture deeper.")
while player.is_alive():
    if player.health > player.max_health:
        player.health = player.max_health
    print("what will you do?")
    print(f"health: {player.health}")
    print("[1] Continue")
    print("[2] View stats")
    print("[3] View inventory")
    print('[4] Quit')
        
    choice = input(">")
    if choice == '1':
        depth += 1
        explore()
    elif choice == '2':
        print(player.see_stats())
    elif choice == '3':
        player_inventory.see_inventory()
        print("[1] Equip/use Item")
        print("[2] Unequip Item")
        print('[3] See item information')
        print('[4] Go back')
        inv_choice = input(">")
        if inv_choice == '1':
            print('Which item do you want to equip/use?')
            item_equip_choice = int(input(">"))
            if isinstance(player_inventory.items[item_equip_choice], inv.EquippableItem):
                player.equip_item(player_inventory.items[item_equip_choice])
            elif isinstance(player_inventory.items[item_equip_choice], inv.Consumable):
                player_inventory.items[item_equip_choice].use(player)
                player_inventory.remove_item(player_inventory.items[item_equip_choice])
        elif inv_choice == '2':
            print('Which item do you want to unequip?')
            item_equip_choice = int(input(">"))
            player.unequip_item(player_inventory.items[item_equip_choice])
        elif inv_choice == '3':
            print("which item do you want to learn about?")
            item_choice = int(input(">"))
            print(player_inventory.items[item_choice].see_information())
        elif inv_choice == '4':
            continue
    elif choice == '4':
        print(f"you made it to depth {depth}!")
        break
        
