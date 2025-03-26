import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.game.game_key_maker import GameKeyMaker
from src.dungeons.intro_dungeon import IntroDungeon
from src.game.player import Player




def add_project_root():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    while current_dir != os.path.dirname(current_dir):
        if "main.py" in os.listdir(current_dir):
            sys.path.append(current_dir)
            break 
        current_dir = os.path.dirname(current_dir)
add_project_root()

def main():
    intro_dungeon = IntroDungeon()
    player = Player()
    game_key = GameKeyMaker(intro_dungeon, player)
    game_key.turn()
    



if __name__ == "__main__":
    main()  