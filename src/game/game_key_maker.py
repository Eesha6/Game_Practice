import os
import sys

# Append the src directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

# Import necessary modules
from game.player import Player
from dungeons.intro_dungeon import IntroDungeon
from dungeons.tree_hollow import TreeHollow

class GameKeyMaker:
    def __init__(self, intro_dungeon, player):
        self.player = player()
        
        self.dungeon_dict = {
            "intro": intro_dungeon(), # intro dungeon gets loaded
            "tree_hollow": TreeHollow()
        }
        self.current_screen = self.dungeon_dict["intro"]

    def turn(self):
        while self.current_screen:
            self.dungeon_dict[self.current_screen].enter(self)  # Pulls up dungeon screen


    def change_screen(self, new_screen):
        self.current_screen = self.dungeon_dict[new_screen]
        self.current_screen.enter(self)

    def game_add_to_backpack(self, item):
        self.player.add_to_backpack(item)

    def game_take_from_backpack(self, item):
        self.player.remove_from_backpack(item)


