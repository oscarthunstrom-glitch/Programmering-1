import random

monsters = [
    {"name": "Gurgle Goblin", "hp": 50, "strenght": 10},
    {"name": "Pålrick mumien", "hp": 70, "strenght": 12},
    {"name": "Didrick den demoniska hästen", "hp": 60, "strenght": 20},
    {"name": "Flerik den gigantiska fladdermusen", "hp": 65, "strenght": 15}]

monster = random.choice(monsters)
monster_hp = monster["hp"]
monster_strength = monster["strength"]

def encounter_monster(playerSTR):
    monster = random.choice(monsters)
    monster_strenght = monster["strength"] + random.randit(0,2)
    print(f"Du möter" {monster["name"]}"! med en trolig styrka på"{monster["strength"]}"!")

    

