from utils import *


class CellHallway:
    def __init__(self):
        self.room_items = ("flashlight", "batteries")

    def enter(self, game_key):
        slow_print("You have walked into the cell hallway...")
        pause(1.5)
        slow_print("There is very little light- you can barely see your hands.")
        pause(2.5)