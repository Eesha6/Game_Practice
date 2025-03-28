from utils import slow_print

class Player:
    def __init__(self):
        self.backpack = []


    def add_to_backpack(self, item):
        self.backpack.append(item)
        slow_print(f"You have following items: {self.backpack}")
        slow_print(f"Added {item} to your backpack.")
        
        for item in self.backpack:
            print(item)


    def remove_from_backpack(self, item):
        if item in self.backpack:
            self.backpack.remove(item)
            slow_print("You have following items:")
            for item in self.backpack:
                print(item)
        else:
            slow_print(f"{item} not in your backpack.")
            
    def print_backpack(self):
        """Prints all items in the backpack."""
        if self.backpack:
            slow_print("Your backpack contains:")
            for item in self.backpack:
                slow_print(item)
        else:
            slow_print("Your backpack is empty.")
            
    