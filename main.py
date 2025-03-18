from src.game_key_maker import GameKeyMaker
from src.dungeons.intro_dungeon import IntroDungeon
from src.player import Player
import os

def add_project_root():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    while current_dir != os.path.dirname(current_dir):
        if "main.py" in os.listdir(current_dir):
            sys.path.append(current_dir)
            break 
def main():
    game_key = GameKeyMaker(IntroDungeon, Player)
    game_key.turn()





if __name__ == "__main__":
    main()