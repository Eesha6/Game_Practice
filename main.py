import os
import sys

# Add src to system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.game.game_key_maker import GameKeyMaker
from src.dungeons.intro_dungeon import IntroDungeon
from src.game.player import Player

def main():
    game = GameKeyMaker(IntroDungeon, Player)
    game.turn()

if __name__ == "__main__":
    main()

    