import random
from Kista import Kista 

class Player():
    Giant = {"namn": "Giant", "hp": 120, "strength": 10}
    Wizard = {"namn": "Wizard", "hp": 80, "strength": 8}
    Raider = {"namn": "Raider", "hp": 100, "strength": 12}

    ALL_CHARCTERS = [Giant, Wizard, Raider]

    WEAPONS = {
        "hands":  {"name": "bara händerna", "strength": 2},
        "sword":  {"name": "svärd",         "strength": 8},
        "dagger": {"name": "dolk",          "strength": 6},
        "arrow":  {"name": "pil",           "strength": 8},
        "axe":    {"name": "yxa",           "strength": 12},
    }

    def __init__(self, character_type):
        self.name = character_type["name"]
        self.max_hp = character_type["hp"]
        self.hp = character_type["hp"]
        self.strength = character_type["strength"]
        self.level = 1
        
        self.inventory = ["hands"]
        self.equipped = "hands"

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} tog {self.damage} skada. HP: {self.hp}/{self.hp_max}")

    def heal(self, amount):
        self.hp += amount 
        if self.hp > self.max_hp:
            self.hp =  self.max_hp 
        print(f"{self.name} healade {amount} HP -> {self.hp}/{self.hp_max}")

    def is_alive(self):
        return self.hp > 0
    
    def level_up(self):
        self.level += 1
        self.max_hp += 25
        self.hp = self.max_hp
        self.base_strength += 4

        print(f"\n 🌟🌟🌟{self.name} GICK UPP EN LEVEL!🌟🌟🌟")
        print(f"-> Level {self.level} --- +25 HP --- +4 grundstyrka")
    
    def add_weapon(self, weapon_key):
        if weapon_key in Player.WEAPONS and weapon_key not in self.inventory:
            self.inventory.append(weapon_key)
            print(f"Du hittade ett {Player.WEAPONS[weapon_key]['name']}!")
        elif weapon_key in self.inventory:
            print("Du har redan det vapnet.")

    def equip_weapon(self, weapon_key):
        if weapon_key in self.inventory:
            self.equipped = weapon_key
            print(f"Du fick {Player.WEAPONS[weapon_key]['name']}!")
        else:
            print("Du har inte det vapnet!")

    def show_inventory(self):
        print("\n" + "=" * 30)
        print(" INVENTORY")
        for w in self.inventory:
            name = Player.WEAPONS[w]["name"]
            dmg = Player.WEAPONS[w]["strength"]
            mark = "<- UTRUSTAD" if w == self.equipped else ""
            print(f"    * {name} (+{dmg} skada){mark}")
        print("=" * 30 + "\n")

    def open_chest(self, kista):
        kista.open(self)
    
    def show_status(self):
        print("\n" + "=" * 40)
        print(f"    Level: {self.level}")
        print(f"    HP: {self.hp}/{self.max_hp}")
        print(f"    Styrka: {self.base_strength} + {Player.WEAPONS[self.equipped]['damage']} = {self.get_strength()}")
        print(f"    Vapen: {Player.WEAPONS[self.equipped]['name']}")
        print("=" * 40 + "\n") 