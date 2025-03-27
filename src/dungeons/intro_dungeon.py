
from utils import *

backpack = []
action_menu = "***  MENU  ***\n1) search area\n2) grab item\n3) combine items\n4) use item\n"
combining_list = []



class IntroDungeon:
    def __init__(self):
        self.room_items = ["(s)eeds", "(w)ater","(d)irt"]
        self.combinator_dict = {
            frozenset(["(d)irt", "(w)ater"]): "mud",
            frozenset(["(d)irt", "(s)eeds"]): "sprout",
            frozenset(["(s)eeds", "(w)ater"]): "watery seeds"
        }

    def enter(self, game_key):
        intro_1 = "You awaken on a riverbank..."
        intro_2 = "You have no idea how you got here."
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
                intro_3 = "Near a tree, you see some (s)eeds..."
                slow_print(intro_3)
                pause(2.5)
                slow_print("You see a pail of (w)ater; also, there is (d)irt everywhere...")
                pause(3.5)
                clear()
                continue
        
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

                if "sprout" in game_key.player.backpack:
                    slow_print("The sprout starts shaking in your backpack...")
                    pause(2)
                    game_key.change_screen("tree_hollow")

               
            elif action == '3':
                game_key.player.print_backpack()
                slow_print("Combine what first? (s/w/d or full name)")
                name_map = {"s": "(s)eeds", "w": "(w)ater", "d": "(d)irt"}
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
                if item == "(w)ater" and "(w)ater" in game_key.player.backpack:
                    slow_print("The water is gross- you drink as much as you can stand...")
                    pause(2.5)
                elif item == "(d)irt" and "(d)irt" in game_key.player.backpack:
                    slow_print("You grab the dirt and pour it into your hair- have you gone crazy?")
                    pause(2.5)
                elif item == "(s)eeds" and "(s)eeds" in game_key.player.backpack:
                    slow_print("You toss the seeds into the river, they could have been useful...")
                    pause(2.5)
                elif item == "(s)hiny ring":
                    slow_print("A guard comes to check on you...")
                    pause(1)
                    slow_print("Wait! I recognize that...")

