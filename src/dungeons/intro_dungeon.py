
from utils import *

backpack = []
action_menu = "***  MENU  ***\n1) search area\n2) grab item\n3) combine items\n4) use item\n"
combining_list = []

class IntroDungeon:
    def __init__(self):
        self.room_items = ["(s)eeds", "(d)irt" , "pail of (w)ater"]
        self.combinator_dict = {
            "(d)irt+(w)ater": "mud",
            "(d)irt+(s)eeds": "sprout",
            "(s)eeds+(w)ater": "watery seeds"

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
                intro_3 = "Near a tree, you see some (s)eeds- like some apple seeds."
                slow_print(intro_3)
                pause(2.5)
                slow_print("You see a pail of (w)ater; also, there is (d)irt everywhere...")
                pause(3.5)
                clear()
                continue
        
            elif action == '2':
                slow_print("What would you like to grab?")
                item = input()
                if item == "s":
                    if "(s)eeds" in self.room_items: 
                        slow_print("You grabbed the seeds")
                        pause(1)
                        self.room_items.remove("(s)eeds")
                        game_key.player.game_add_to_backpack("(s)eeds")
                    else:
                        slow_print("The seeds are no longer here.")

                elif item == "w":
                    if "pail of (w)ater" in self.room_items:
                        slow_print("You grabbed the pail of water")
                        pause(1)
                        self.room_items.remove("pail of (w)ater")
                        game_key.player.game_add_to_backpack("pail of (w)ater")
                    else:
                        slow_print("The pail of water is no longer here.")
                elif item == "d":
                    if "(d)irt" in self.room_items:
                        slow_print("You grabbed the dirt...")
                        pause(1)
                        self.room_items.remove("(d)irt")
                        game_key.player.game_add_to_backpack("(d)irt")
                    else:
                        slow_print("The dirt is no longer here.")

                    
            
                

            elif action == '3':
                combining_1 = ""
                combining_2 = ""
                combined_list = []

                slow_print("You have the following items: ")
                print(backpack)
                slow_print("What would you like to combine first?")
                combining_1 = input()
                slow_print(f"What would you like to combine with {combining_1}?")  # Corrected f-string formatting
                combining_2 = input()
                combined_list.append(combining_1)
                combined_list.append(combining_2)
                combined_list.sort()
                combined_string = "+".join(combined_list)
                
                if combined_string in self.combinator_dict:
                    slow_print(f"You have created {self.combinator_dict[combined_string]}")
                    backpack.append(self.combinator_dict[combined_string])
                    slow_print(f"The {self.combinator_dict[combined_string]} has been placed in your backpack")
                else:
                    slow_print("You can't combine these items.")

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
    