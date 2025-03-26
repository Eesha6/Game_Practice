from utils import slow_print

class Player:
    def __init__(self):
        self.backpack = []


    def add_to_backpack(self, item):
        self.backpack.append(item)
        slow_print("You have following items:")
        
        for item in self.backpack:
            print(item)


    def remove_from_backpack(self, item):
        self.backpack.remove(item)
        slow_print("You have following items:")
        for item in self.backpack:
            print(item)
    