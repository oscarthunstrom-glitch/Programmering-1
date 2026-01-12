import random

class Monster:
    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.strength = strength
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
    
    def is_alive(self):
        return self.hp > 0
    
    def attack(self,player):
        print(f"{self.name} attackerar {player.name} och gör {self.strength} skada!")
        player.take_damage(self.strength)
        
    

ALLA_MONSTER = [
    {"name": "GURGLE GOBLIN", "hp": 50, "strength": 30},
    {"name": "PÅLRICK MUMIEN", "hp": 70, "strength": 40},
    {"name": "DIDRICK DEN DEMONISKA HÄSTEN", "hp": 90, "strength": 50},
    {"name": "FLERICK DEN GIGANTISKA FLADDERMUSEN", "hp": 60, "strength": 30},
    {"name": "SIMHOPPAREN ALBERTO ZINGO", "hp": 70, "strength": 50},
    {"name": "ITALIAN BACH", "hp": 65, "strength": 60},
    {"name": "ANJO", "hp": 80, "strength": 20},
    {"name": "MEGIC MIKE", "hp": 100, "strength": 45},
    {"name": "LIL BUB", "hp": 55, "strength": 40},
    {"name": "ARVID ÖMAN", "hp": 80, "strength": 35},
]

def skapa_slumpmonster():
    monster_data = random.choice(ALLA_MONSTER)

    if random.random() < 0.08:
        print("\n" + "="*60)
        print("Ett stort läskigt monster dyker upp! 😱😱😱")
        print("="*60 + "\n")
        return Monster(
            name = monster_data["name"].upper() + " (Boss)",
            hp = monster_data["hp"] * 3,
            strength = monster_data["strength"] * 2
        )
            
    return Monster(
        name = monster_data["name"],
        hp = monster_data["hp"],
        strength = monster_data["strength"]
    )







