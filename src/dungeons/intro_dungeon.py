from utils import *

class IntroDungeon:
    def __init__(self):
        self.room_items = ["(s)eeds", "(w)ater", "(d)irt"]
        self.combinator_dict = {
            frozenset(["(d)irt", "(w)ater"]): "mud",
            frozenset(["(d)irt", "(s)eeds"]): "sprout",
            frozenset(["(s)eeds", "(w)ater"]): "watery seeds"
        }

    def enter(self, game_key):
        slow_print("You awaken on a riverbank...")
        pause(2)
        slow_print("You have no idea how you got here.")
        pause(2)
        clear()

        while True:
            print("*** MENU ***")
            print("1) Search area")
            print("2) Grab item")
            print("3) Combine items")
            print("4) Use item")
            action = input("> ")

            if action == '1':
                slow_print("You see some (s)eeds, a pile of (d)irt, and a pail of (w)ater.")

            elif action == '2':
                slow_print("What would you like to grab? (s/w/d)")
                item = input().lower()
                name_map = {"s": "(s)eeds", "w": "(w)ater", "d": "(d)irt"}
                name = name_map.get(item)
                if name and name in self.room_items:
                    self.room_items.remove(name)
                    game_key.player.add_to_backpack(name)
                else:
                    slow_print("That item isn't here.")

            elif action == '3':
                game_key.player.print_backpack()
                slow_print("Combine what first?")
                i1 = input().lower()
                slow_print("Combine with?")
                i2 = input().lower()

                name_map = {"s": "(s)eeds", "w": "(w)ater", "d": "(d)irt"}
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

            elif action == '4':
                slow_print("What would you like to use?")
                game_key.player.print_backpack()
                item = input().lower()

                if item in game_key.player.backpack:
                    if item == "(w)ater":
                        slow_print("You drink some of the water, you feel rejuvinated.")
                        pause(2.5)
                    elif item == "(d)irt":
                        slow_print("You feel hungry so you decide to create a cake out of the dirt.")
                        pause(2.5)
                    elif item == "(s)eeds":
                        slow_print("You toss some of the seeds into the river...")
                        pause(2.5)
                else:
                    print("You don't have that item.")
