import os
import sys

# Append the src directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

# Import necessary modules
from game.player import Player
from dungeons.cell_hallway import CellHallway

class GameKeyMaker:
    def __init__(self, intro_dungeon, player):
        self.player = player
        self.dungeon_dict = {
            "intro": intro_dungeon, # intro dungeon gets loaded
            "cell block 3": CellHallway()
        }

    def turn(self):
        self.dungeon_dict["intro"].enter(self)  # Pulls up dungeon screen

    def change_screen(self, new_screen):
        self.current_screen = self.dungeon_dict[new_screen]
        self.current_screen.enter(self)

    def game_add_to_backpack(self, item):
        #self.player.add_to_backpack(item)
        backpack.append(item)  # Ensure this is adding items correctly
        print(f"Current Backpack: {backpack}")  # Print the current contents of the backpack
        slow_print(f"Added {item} to your backpack.")

    def game_take_from_backpack(self, item):
        self.player.remove_from_backpack(item)


