


class GameKeyMaker():
    def __init__(self, intro_dungeon, player):
        self.player = player() 
        self.dungeon_dict = {
            "intro": intro_dungeon(self.player), #intro dungeon gets loaded
            "cell block 3": CellBlock3()
        }
       

    def turn(self):
        self.dungeon_dict["intro"].enter(self) #pulls up dungeon screen
