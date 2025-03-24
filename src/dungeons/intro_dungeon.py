
from utils import *

backpack = []
action_menu = "***  MENU  ***\n1) search area\n2) grab item\n3) combine items\n4) use item\n"
combining_list = []

class IntroDungeon:
    def __init__(self):
        self.room_items = ["(r)ing", "(d)irt" , "bowl of (w)ater"]
        self.combinator_dict = {
            "(d)irt+(w)ater": "mud",
            "(d)irt+(r)ing": "dirty ring",
            "(r)ing+(w)ater": "shiny ring"

        }



   # def __init__(self, player):
     #   self.player = player


   #def enter(self, game_key):
        #print("You awaken...")  
        #print("You realize you're in a dungeon")
        #rint("It smells like dung.")







    def enter(self, game_key):
        intro_1 = "You awaken on a riverbank... "
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
                intro_3 = "In a corner of your cell, you see a (r)ing- like a wedding ring."
                slow_print(intro_3)
                pause(2.5)
                slow_print("You see a bowl of gross (water); also, there is (d)irt everywhere...")
                pause(3.5)
                clear()
                continue
        
            elif action == '2':
                slow_print("What would you like to grab?")
                item = input()
                if item == "r":
                    slow_print("You grabbed the ring")
                    pause(1)
                    self.room_items.remove("(r)ing")
                    game_key.game_add_to_backpack("(r)ing")

                elif item == "w":
                    slow_print("You grabbed the bowl of water")
                    pause(1)
                    self.room_items.remove("(w)ater")
                    game_key.game_add_to_backpack("(w)ater")

                elif item == "d":
                    slow_print("You grabbed the dirt...")
                    pause(1)
                    self.room_items.remove("(d)irt")
                    game_key.game_add_to_backpack("(d)irt")

                
           
               

            elif action == '3':
                combining_1 = ""
                combining_2 = ""
                combined_list = []

                slow_print("You have the following items: ")
                print(backpack)
                slow_print("What would you like to combine first?")
                combining_1 = input()
                slow_print("What would you like to combine with {combining_1}?")
                combining_2 = input()
                combined_list.append(combining_1)
                combined_list.append(combining_2)
                combined_list.sort()
                combined_string = "+".join(combined_list)
                self.combinator_dict[combined_string]
                slow_print(f"You have created {self.combinator_dict[combined_string]}")
                pause(1)
                backpack.append(self.combinator_dict[combined_string])
                slow_print(f"The {self.combinator_dict[combined_string]} has been placed in your backpack")

            elif action == '4':
                slow_print("What would you like to use?")
                for item in backpack:
                    slow_print(item)
                item = input()
                if item == "(w)ater" and "(w)ater" in backpack:
                    slow_print("The water is gross- you drink as much as you can stand...")
                    pause(2.5)
                elif item == "(d)irt" and "water" in backpack:
                    slow_print("You grab the dirt and pour it into your hair- have you gone crazy?")
                    pause(2.5)
                elif item == "(r)ing" and "ring" in backpack:
                    slow_print("You toss the ring out of the cell... that could have been useful")
                    pause(2.5)
                elif item == "(s)hiny ring":
                    slow_print("A guard comes to check on you...")
                    pause(1)
                    slow_print("Wait! I recognize that...")
    