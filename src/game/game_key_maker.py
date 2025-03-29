import os
import sys

# Append the src directory to sys.path
SRC_PATH = os.path.abspath(os.path.dirname(__file__))
if SRC_PATH not in sys.path:
    sys.path.append(SRC_PATH)

# Import necessary modules
from player import Player
from dungeons.intro_dungeon import IntroDungeon
from dungeons.tree_hollow import TreeHollow

class GameKeyMaker:
    def __init__(self, intro_dungeon, player):
        self.player = player()
        self.game_over = False
        
        self.dungeon_dict = {
            "intro": intro_dungeon(), # intro dungeon gets loaded
            "tree_hollow": TreeHollow()
        }
        self.current_screen = "intro"

    def turn(self):
        while not self.game_over and self.current_screen:
            current_dungeon = self.dungeon_dict[self.current_screen]  # Pulls up dungeon screen
            next_screen = current_dungeon.enter(self)

            if next_screen in self.dungeon_dict:
                self.current_screen = next_screen
            elif next_screen is None:
                self.game_over = True

    def change_screen(self, new_screen):
        if new_screen in self.dungeon_dict:
             self.current_screen = new_screen
        else:
            print("That place doesn't exist.")
       
       

    def game_add_to_backpack(self, item):
        self.player.add_to_backpack(item)

    def game_take_from_backpack(self, item):
        self.player.remove_from_backpack(item)


