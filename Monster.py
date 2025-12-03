# import random
# from Player import *

# class Monster:
#     def __init__(self, name, hp, strength):
#         self.name = name
#         self.hp = hp
#         self.max_hp = hp
#         self.strength = strength
    
#     def take_damage(self, damage):
#         self.hp -= damage
#         if self.hp < 0:
#             self.hp = 0
#         print(f"{self.name} tog {damage} skada. HP: {self.hp}/{self.max_hp}")
    
#     def is_alive(self):
#         return self.hp > 0
    
#     def attack(self, player):
#         player.take_damage(self.strength)
#         print(f"{self.name} attackerade {player.name} för {self.strength} skada!")


# ALLA_MONSTER = [
#     Monster("Gurgle Goblin", 50, 5),
#     Monster("Palrick mumien", 75, 7),
#     Monster("Didrick den demoniska hästen", 60, 10 ),
#     Monster("Flerick den gigantiska fladdermusen", 80, 11 ),
# ]
# monster = random.choice(ALLA_MONSTER)
# monster_name = monster["name"]
# monster_strength = monster["strength"]
# monster_hp = monster["hp"]

# monster = ["Gurgle_Goblin", "Palrick_Mumien", "Didrick_den_demoniska_hästen", "Flerick_den_gigantiska_fladdermusen"]

# monster = random.choice(ALLA_MONSTER)
# print("Gor dig redo for en episk strid!")
# print("======== Monster =======\n")
# print(f"Monster:  {monster_name}")
# print(f"Hp:  {monster_hp}")
# print(f"Styrka:  {monster_strength}")
# print("======================")



# def slumpmonster():
#     return random.choice(ALLA_MONSTER)
# print("Gor dig redo for en episk strid!")
# print("========Monster=======")
# print(f"Monster:  {monster_name}")
# print(f"Hp:  {monster_hp}")
# print(f"Styrka:  {monster_strength}")
# print("======================")



