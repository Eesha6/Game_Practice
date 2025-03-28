from utils import *

from game.player import Player
backpack = []
action_menu = "***  MENU  ***\n1) search area\n2) grab item\n3) combine items\n4) use item\n5) plant\n"
combining_list = []

class TreeHollow:
    def __init__(self):
        self.room_items = ("shovel", "berries")
        self.combinator_dict = {
            frozenset(["(s)hovel", "(s)prout"]): "willow wish tree",
            frozenset(["(s)hovel", "(b)erries"]): "berry bush",
            frozenset(["(b)erries", "(s)prout"]): "smoothie",
        }

    def enter(self, game_key):
        slow_print("You're transported to tree hollow and are surrounded by thousands of fireflies. ")
        pause(1.5)
        slow_print("You spin around, fascinated by the beauty around you.")
        pause(2.5)

        intro_1 = "You realize you light leaped!"
        intro_2 = "It takes a second for your eyes to adjust."
        clear()
        pause(2)

        slow_print(intro_1)
        pause(2)
        clear()
        slow_print(intro_2)
        pause(2)
        clear()
    

        while True:
            action = input(action_menu)

            if action == '1':
                intro_3 = "You walk around and suddenly stumble. Discovering a (s)hovel"
                slow_print(intro_3)
                pause(2.5)
                slow_print("You spot a bush of (b)erries.")
                pause(3.5)
                clear()
                continue
        
            elif action == '2':
                slow_print("What would you like to grab? (sh/b)")
                item = input().lower()
                name_map_dict = {"s": "(sh)ovel", "b": "(b)erries"}
                name = name_map_dict.get(item)
                if name and name in self.room_items:
                    self.room_items.remove(name)
                    game_key.player.add_to_backpack(name)
                else:
                    slow_print("That item isn't here.")


               
            elif action == '3':
                game_key.player.print_backpack()
                slow_print("Combine what first? (sh/b/s or full name)")
                name_map_dict = {"sh": "(sh)hovel", "b": "(b)erries", "s": "(s)prout"}
                item1_key = input().lower()
                slow_print("Combine with? (sh/b/s or full name)")
                item2_key = input().lower()

                i1 = name_map_dict.get(item1_key, item1_key)
                i2 = name_map_dict.get(item2_key, item2_key)


                key = frozenset([i1, i2])
                if key in self.combinator_dict:
                    result = self.combinator_dict[key]
                    if i1 in game_key.player.backpack and i2 in game_key.player.backpack:
                        game_key.player.remove_from_backpack(i1)
                        game_key.player.remove_from_backpack(i2)
                        game_key.player.add_to_backpack(result)
                        slow_print("You created: " + result)
                    else:
                        slow_print("You're missing something.")
                else:
                    slow_print("That didn't work.")

            elif action == '4':
                slow_print("What would you like to use?")
                for item in game_key.player.backpack:
                    slow_print(item)
                item = input().strip()
                if item == "(sh)ovel" and "(sh)ovel" in game_key.player.backpack:
                    slow_print("You dig a hole for fun.")
                    pause(2.5)
                elif item == "(b)erries" and "(b)erries" in game_key.player.backpack:
                    slow_print("You pluck a handful of berries and eat them. Enjoying the soury sweetness")
                    pause(2.5)
                elif item == "(s)prout" and "(s)prout" in game_key.player.backpack:
                    slow_print("You feel the urge to eat the sprout but you just can't make yourself do it.")
                    pause(2.5)
                else:
                    print("You don't have that item.")
            elif action == '5':
                if "willow wish tree" in game_key.player.backpack:
                    slow_print("You plant the willow wish tree!")
                    slow_print("It grows rapidly into a fine willow!")
                    game_key.game_over = True
                    return None
                else:
                    slow_print("Your wish to escape cannot come true yet. Maybe you need to grow something first?")
            else:
                print("Choose a valid option!")

                
