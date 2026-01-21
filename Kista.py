import random    

class Kista:    
    def __init__(self):
        pass

    def open_chest(self, player):    
        outcomes = ["weapon", "armour", "health potion"]
        result = random.choice(outcomes)

        if result == "armour":
            player.max_hp += 30
            player.hp += 30
            if player.hp > player.max_hp:
                player.hp = player.max_hp
            print(" Du fick en rustning i kistan! \n Det ger dig +30 i hp!")

        elif result == "weapon":
            new_weapon = random.choice(["sword", "axe", "arrow", "dagger"])
            player.add_weapon(new_weapon)
            if random.random() < 1.0:     #lite onödigt
                player.equip_weapon(new_weapon)
               

        else:
            player.heal(40)
            print("Du hittade en health potion! \n +40 i hp")
