import random
from Player import Player

class Monster:

    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.strength = strength


monster_liste = [
    Monster("Gurgle Govlin", 50, 5),
    Monster("Pålrick mumien", 75, 7),
    Monster("Didrick den demoniska hästen", )

monster = random.choice(monsters)
monster_name = monster["name"]
monster_strength = monster["strength"]
monster_hp = monster["hp"]



