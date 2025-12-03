import random 
from Player import *
from Kista import *
from Monster import *
from Fälla import *

def show_title():
    print("""
______________ ______________ ___________.___ _______      _____  .____      __________ ________    _________ _________
\__    ___/   |   \_   _____/ \_   _____/|   |\      \    /  _  \ |    |     \______   \\_____  \  /   _____//   _____/
  |    | /    ~    \    __)_   |    __)  |   |/   |   \  /  /_\  \|    |      |    |  _/ /   |   \ \_____  \ \_____  \ 
  |    | \    Y    /        \  |     \   |   /    |    \/    |    \    |___   |    |   \/    |    \/        \/        \
  |____|  \___|_  /_______  /  \___  /   |___\____|__  /\____|__  /_______ \  |______  /\_______  /_______  /_______  /
                \/        \/       \/                \/         \/        \/         \/         \/        \/        \/  
          
          """)

show_title()










def show_menu():
    print("\n" + "=" * 80)
    print("                 VAD VILL DU GÖRA?")
    print("=" * 80)
    print(" 1. Öppna dörr 1     2. Öppna dörr 2     3. Öppna dörr 3")
    print("4. Visa status       5. Visa inventory   q. Avluta")
    print("=" * 80)

print("Välkommen till THE FINAL BOSS!\n")
print("Du står i en enorm, mörk grotta. Framför dig har du tre mystiska dörrar...\n")

print("Välj din karaktär:")
print("1. Giant  (Stark men långsam💪)")
print("2. Wizard (Magisk men skör🪄)")
print("3. Raider (Balanserad⚖️)")
      
while True:
    val = input("Skriv in 1,2 eller 3 för att välja din karaktär!")
    if val == "1":
        player = Player(Player.Giant)
        print(f"\nDu valde GIANT!")
        break
    elif val == "2":
        Player(Player.Wizard)
        print(f"\nDu valde Wizard!")
        break
    elif val == "3":
        Player(Player.Raider)
        print(f"\nDu valde Raider")
        break
    else:
        print("Välj 1,2 eller 3 tack!\n")

player.show_status()

#KISTAN

print("Du hittade en stor mystisk kista!")
kista = Kista()
player.open_chest(kista)
player.show_status()

#VALEN OCH SPELETS GÅNG
while player.is_alive():
    show_menu()
    val = input("\nDitt val:").strip().lower()

    if val in ["1", "2", "3"]:
        print(f"\nDu närmar dig dörr {val}...")
        input("Tryck på Enter-knappen för att öppna dörren...")
        #print("Dörren öppnas och ***")

        encounter = random.choice(["monster", "kista", "fälla"])
        
        if encounter == "kista":
            print("Du hittade en kista!")
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
                    damage_to_monster = player.strength + Player.WEAPONS[player.equipped]["strength"]
                    monster.hp -= damage_to_monster
                    print(f"\nDu attackerade {monster.name} och gjorde {damage_to_monster} skada! {monster.name} har nu {max(monster.hp, 0)} HP kvar.\n")

                    if monster.hp > 0:
                        player.take_damage(monster.strength)
                    else:
                        print(f"\n🎉 Du besegrade {monster.name}! 🎉")
                        player.level_up()
                elif action == "r":
                    print(f"\nDu rymde från striden mot {monster.name}!")
                    break
                else:
                    print("Ogiltigt val, försök igen.")
        else:
            print("\nEn dold fälla aktiverades!")
            fälla = Fälla()
            fälla.aktivera(player)

    elif val == 4:
        player.show_status()
    elif val == 5:
        player.show_inventory()
    elif val in ["q", "quit", "avsluta"]:
        print("\nDu väljer att inte fortsätta spelet eftersom du blev för rädd för fladdermössen i taket...")
        print("Tack för att du spelade THE FINAL BOSS!")
        break
    else: 
        print("⚠️Ogiltigt val⚠️ - försök igen!!!")

    input("\nTryck på Enter-knappen för att fortsätta...")

    if not player.is_alive():
        print("\nDu har dött - GAME OVER")
        break

#FÄLLAN 
    fälla = Fälla()
    fälla.aktivera(player)
    player.show_status()
    if not player.is_alive():
        print("\nDu har dött - GAME OVER")
        break