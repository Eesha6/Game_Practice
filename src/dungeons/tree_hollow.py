from utils import *

from game.player import Player
backpack = []
action_menu = "***  MENU  ***\n1) search area\n2) grab item\n3) combine items\n4) use item\n"
combining_list = []

class TreeHollow:
    def __init__(self, player):
        self.room_items = ("leaves", "berries", "ferns")
        self.combinator_dict = {
            frozenset(["(l)eaves", "(f)erns"]): "dry salad",
            frozenset(["(l)eaves", "(b)erries"]): "potion",
            frozenset(["(b)erries", "(f)erns"]): "bowl of rasberries"
        }

    def enter(self, game_key):
        slow_print("You're transported to tree hollow and are surrounded by thousands of fireflies. ")
        pause(1.5)
        slow_print("You spin around, fascinated by the beauty around you.")
        pause(2.5)

    def enter(self, game_key):
        intro_1 = "After you successfully light leaped away you enter tree hollow!"
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
                intro_3 = "You spot a small fox. You see some (f)erns growing freely..."
                slow_print(intro_3)
                pause(2.5)
                slow_print("You see a bush of (b)erries; also, there are (l)eaves everywhere...")
                pause(3.5)
                clear()
                continue
        
            elif action == '2':
                slow_print("What would you like to grab? (l/b/f)")
                item = input().lower()
                name_map = {"l": "(l)eaves", "b": "(b)erries", "f": "(f)erns"}
                name = name_map.get(item)
                if name and name in self.room_items:
                    self.room_items.remove(name)
                    game_key.player.add_to_backpack(name)
                else:
                    slow_print("That item isn't here.")

                if "bowl of raspberries" in game_key.player.backpack:
                    slow_print("You were successfully able to teleport away!")
                    slow_print("You win the game!")
                    break

               
            elif action == '3':
                game_key.player.print_backpack()
                slow_print("Combine what first? (l/b/f or full name)")
                name_map = {"l": "(l)eaves", "b": "(b)erries", "f": "(f)erns"}
                item1_key = input().lower()
                slow_print("Combine with? (s/w/d or full name)")
                item2_key = input().lower()

                i1 = name_map.get(item1_key, item1_key)
                i2 = name_map.get(item2_key, item2_key)


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
                if item == "(l)eaves" and "(l)eaves" in game_key.player.backpack:
                    slow_print("You roll around in the leaves")
                    pause(2.5)
                elif item == "(b)erries" and "(b)erries" in game_key.player.backpack:
                    slow_print("You pluck a handful of berries and eat them. Enjoying the soury sweetness")
                    pause(2.5)
                elif item == "(f)erns" and "(f)erns" in game_key.player.backpack:
                    slow_print("You make a necklace out of the ferns")
                    pause(2.5)
                elif item == "(s)hiny ring":
                    slow_print("A guard comes to check on you...")
                    pause(1)
                    slow_print("Wait! I recognize that...")

