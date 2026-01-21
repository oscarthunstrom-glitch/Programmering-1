import random 
from Player import *
from Kista import *
from Monster import *
from Fälla import *
from FINALBOSS import *
import sys,time,random


Giant = {"namn": "Giant", "hp": 120, "strength": 50}
Wizard = {"namn": "Wizard", "hp": 80, "strength": 30}
Raider = {"namn": "Raider", "hp": 100, "strength": 40}

ALL_CHARCTERS = [Giant, Wizard, Raider]

WEAPONS = {
    "hands":  {"name": "bara händerna", "strength": 2},
    "katana":  {"name": "katana",         "strength": 8},
    "dagger": {"name": "dolk",          "strength": 6},
    "arrow":  {"name": "pil",           "strength": 8},
    "axe":    {"name": "yxa",           "strength": 12},
}

MAX_level = 5


def show_title():
    print("""
______________ ______________  ___________._____    _____       _____    ____       __________    _____    _________________
\\__    ___/   |   \\_   _____/  \\_  _____/|   |  /     \\    /  _ \\   |   |    \\______   \\_ /     \\  / _____/  / _____/
  |    | /    ___  \\   __)_      |    __)  |   | /   |   \\  /  /_\\ \\ |   |      |    |  _/  /   |  \\ \\_____  \\\\_____\\ 
  |    | \\         /        \\   |     \\  |   |/    |    \\/    |    \\|   |___   |    |   \\/    |   \\/        \\/       \\
  |____|  \\___|_  /________ /   \\____ /   |___|\\___|____/\\____|____/ |______ |\\|________/\\_________/________ /________ /
                                                                                                                        
          
          """)

show_title()



def show_menu(): 
    print("\n" + "=" * 65)
    print("                 VAD VILL DU GÖRA?")
    print("=" * 65)
    print("1. Öppna dörr 1     2. Öppna dörr 2     3. Öppna dörr 3")
    print("4. Visa status       5. Visa inventory   q. Avsluta")
    print("=" * 65)


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

print_slow("Välkommen till THE FINAL BOSS!\n")
print_slow("Du står i en enorm, mörk grotta. Framför dig har du tre mystiska dörrar...\n")

print_slow("Men först, välj din karaktär:\n")
print("1. Giant  (Easy mode🟢)")
print("2. Raider (Normal mode🟡)")
print("3. Wizard (Hard mode🔴)")    
  
while True:
    val = input("Skriv in 1, 2 eller 3 för att välja din karaktär:").strip() 

    if val == "1":
        player = Player(Giant)
        print_slow(f"\nDu valde Giant!")
        break
    elif val == "2":
        player = Player(Raider)
        print_slow(f"\nDu valde Raider")
        break
    elif val == "3":
        player = Player(Wizard)
        print_slow(f"\nDu valde Wizard!")
        break
    else:
        print("Välj 1,2 eller 3 tack!\n")

player.show_status()

#VALEN OCH SPELETS GÅNG
while player.is_alive():
    show_menu()
    val = input("\nDitt val:").strip().lower()

    if val in ["1", "2", "3"]:
        print_slow(f"\nDu närmar dig dörr {val}...")
        input("\nTryck på Enter-knappen för att öppna dörren...")

        if player.level >= 5:
            encounter = "finalboss"
            print_slow("Ett mörkt vrål hörs från dörren... du har inget val...")
        else:
            encounter = random.choice(["monster", "kista", "fälla"])

        if encounter == "kista":
            print_slow("Du hittade en kista!")
            kista = Kista()
            player.open_chest(kista)

        elif encounter == "monster":
            print("\nEtt vilt monster dyker upp!")
            monster = skapa_slumpmonster()
            
            print(f"\n{monster.name} attackerar dig!")
            print(f"HP: {monster.hp} | Styrka: {monster.strength}\n")

            while monster.hp > 0 and player.is_alive():
                action = input("Vill du (a)ttaackera eller (r)ymma? ").strip().lower()
                if action == "a":
                    damage_to_monster = player.get_strength()
                    monster.hp -= damage_to_monster
                    print_slow(f"\nDu attackerade {monster.name} och gjorde {damage_to_monster} skada! {monster.name} har nu {max(monster.hp, 0)} HP kvar.\n")

                    if monster.hp > 0:
                        player.take_damage(monster.strength)
                    else:
                        print_slow(f"\n🎉 Du besegrade {monster.name}! 🎉")
                        player.level_up()
                elif action == "r":
                    print_slow(f"\nDu rymde från striden mot {monster.name}!")
                    break
                else:
                    print("⚠️ Ogiltigt val, försök igen ⚠️")
#THEFINALBOSS FIGHT                    
        elif encounter == "finalboss":
            boss = THEFINALBOSS()
            boss.show()
            print("Ett mörkt och mystiskt vrål kommer från alla tre dörrar...")
            print("...du har inget val...")

            # Final boss fight
            while boss.is_alive() and player.is_alive():
                action = input("Vill du (a)ttaackera eller (r)ymma? ").strip().lower()
                if action == "a":
                    dmg = player.get_strength()
                    boss.take_damage(dmg)

                    if boss.is_alive():
                        boss_dmg = boss.attack()
                        player.take_damage(boss_dmg)
                        if not player.is_alive():
                            print_slow("\nDu borde ha lyssnat på dina nerver... GAME OVER")
                            break
                    else:
                        print_slow(f"\n🎉 Du besegrade {boss.name}! 🎉")
                        print_slow("Du utförde det omöjliga och besegrade THEFINALBOSS!\nTHEFINALBOSS.....DEFEATED!")
                        sys.exit()

                elif action == "r":
                    if random.random() < 0.01:
                        print_slow("\nEmot alla odds flydde du...men alla dörra leder i slutändan till honom")
                        break
                    else:
                        print_slow("\nDu försökte fly men misslyckades! Bossen attackerar skrattandes!")
                        boss_dmg = boss.attack()
                        player.take_damage(boss_dmg)
                        if not player.is_alive():
                            print_slow("\nDu har dött i ditt försök att fly - GAME OVER")
                            break
                else:
                    print("⚠️Ogiltigt val, försök igen⚠️")

        else:
            print("\nEn dold fälla aktiverades!")
            falla = Fälla()
            falla.aktivera(player)

    elif val == "4":
        player.show_status()
    elif val == "5":
        player.show_inventory()
    elif val in ["q", "quit", "avsluta"]:
        print_slow("\nDu väljer att inte fortsätta spelet eftersom du blev för rädd för fladdermössen i taket...\n")
        print_slow("Nu har du äntligen spelat THE FINAL BOSS!")
        break
    else: 
        print("Ogiltigt val - försök igen!!!")

    input("\nTryck på Enter-knappen för att fortsätta...")

    if not player.is_alive():
        print_slow("\nDu har dött - GAME OVER")
        break
        
