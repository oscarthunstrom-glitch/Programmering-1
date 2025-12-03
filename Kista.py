import random
from Player import *

class Kista: 
    def __init__(self):
        pass
        
    def open_chest(self):
        outcomes = ["weapon", "armour", "healt potion"]
        result = random.choice(outcomes)

        if result ==  "armour":
            self.max_hp += 30
            self.hp += 30
            print("Du fick en rustning i kistan! \n +30 i hp")

        elif result == "weapon":
            new_weapon = random.choice(["sword", "axe", "arrow", "dagger"])
            self.add_weapon(new_weapon)
            if random.random() < 0.4:
                self.equip_weapon(new_weapon)
                print(f"Du fick en ny{new_weapon} \n ")

        else: 
            self.heal(40)
            print("Du hittade en health potion! \n +40 i hp")
        