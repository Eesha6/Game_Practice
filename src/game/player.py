
from utils import slow_print

class Player:
    def __init__(self):
        self.backpack = []

    def add_to_backpack(self, item):
        self.backpack.append(item)
        slow_print(f"Added {item} to your backpack.")

    def remove_from_backpack(self, item):
        if item in self.backpack:
            self.backpack.remove(item)
            slow_print(f"Removed {item} from your backpack.")
        else:
            slow_print(f"{item} not in your backpack.")

    def print_backpack(self):
        if self.backpack:
            slow_print("Your backpack contains:")
            for item in self.backpack:
                slow_print(item)
        else:
            slow_print("Your backpack is empty.")
    