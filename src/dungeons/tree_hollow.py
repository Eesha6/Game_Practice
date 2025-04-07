
from utils import *

class TreeHollow:
    def __init__(self):
        self.room_items = ["(sh)ovel", "(b)erries"]
        self.shovel_found = False
        self.combinator_dict = {
            frozenset(["(sh)ovel", "sprout"]): "tree",
            frozenset(["(sh)ovel", "(b)erries"]): "berry bush",
            frozenset(["(b)erries", "sprout"]): "fresh salad"
        }

    def enter(self, game_key):
        slow_print("You're surrounded by fireflies.")
        pause(1.5)
        slow_print("You realize you light leaped!")
        pause(2)
        clear()

        while True:
            print("*** TREE HOLLOW MENU ***")
            print("1) Search area")
            print("2) Grab item")
            print("3) Check backpack")
            print("4) Combine items")
            print("5) Use item")
            print("6) Escape")
            choice = input("> ")

            if choice == '1':
                if not self.shovel_found:
                    slow_print("You discover a rusty (sh)ovel among the roots. You also spot (b)erries hanging on a nearby bush.")
                    self.room_items.append("(s)hovel")
                    self.shovel_found = True
                else:
                    slow_print("You already searched here.")

            elif choice == '2':
                if not self.room_items:
                    slow_print("Nothing to grab.")
                else:
                    slow_print("What would you like to grab? (sh/b)")
                    item = input().lower()
                    name_map = {"sh": "(sh)ovel", "b": "(b)erries"}
                    name = name_map.get(item)
                    if name and name in self.room_items:
                        self.room_items.remove(name)
                        game_key.player.add_to_backpack(name)
                    else:
                        slow_print("That item isn't here.")
                  

            elif choice == '3':
                game_key.player.print_backpack()

            elif choice == '4':
                game_key.player.print_backpack()
                slow_print("Combine what first?")
                i1 = input().lower()
                slow_print("Combine with?")
                i2 = input().lower()

                name_map = {"sh": "(sh)ovel", "b": "(b)erries"}
                i1 = name_map.get(i1, i1)
                i2 = name_map.get(i2, i2)
                key = frozenset([i1, i2])
                if key in self.combinator_dict:
                    result = self.combinator_dict[key]
                    if i1 in game_key.player.backpack and i2 in game_key.player.backpack:
                        game_key.player.remove_from_backpack(i1)
                        game_key.player.remove_from_backpack(i2)
                        game_key.player.add_to_backpack(result)
                        slow_print("You created: " + result)


                        if result == "sprout":
                            slow_print("The clouds start to darken...")
                            slow_print("Suddenly you are whisked away to tree hollow!")
                            return "tree_hollow"
                        elif result == "watery seeds":
                            slow_print("You wasted your vital resources.")
                            slow_print("You can no longer escape.")
                        elif result == "mud":
                            slow_print("You wasted your vital resources.")
                            slow_print("You can no longer escape.")
                            #game_key.game_over = True
                            #return None
                    else:
                        slow_print("You're missing something.")
                else:
                    slow_print("That didn't work.")

            elif choice == '5':
                slow_print("What would you like to use?")
                game_key.player.print_backpack()
                item = input().lower()
                if item in game_key.player.backpack:
                    if item == "(s)hovel":
                        slow_print("You dig a hole and decide to dance around it.")
                        pause(2.5)
                    elif item == "(b)erries":
                        slow_print("You pluck some berries from the bush.")
                        pause(2.5)
                    else:
                        slow_print("You can't use that item.")



                    slow_print(f"You use the {item}. Nothing major happens.")
                else:
                    slow_print("You don't have that.")

            elif choice == '6':
                if "tree" in game_key.player.backpack:
                    slow_print("You plant the tree and it grows into a massive beanstalk. You climb to safety! You win!")
                    game_key.game_over = True
                    return None
                else:
                    slow_print("You can't escape yet. Maybe you need to plant something?")


                
