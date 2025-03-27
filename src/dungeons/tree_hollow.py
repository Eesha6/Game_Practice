from utils import *


class TreeHollow:
    def __init__(self):
        self.room_items = ("leaves", "berries", "ferns")

    def enter(self, game_key):
        slow_print("You have entered into tree hollow")
        pause(1.5)
        slow_print("There is very little light- you can barely see your hands.")
        pause(2.5)