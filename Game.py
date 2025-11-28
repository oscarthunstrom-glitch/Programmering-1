import random 
from Player import Player
from Kista import Kista 
from Monster import *
import sys,time

def show_menu():
    print("\n" + "=" * 80)
    print("                 VAD VILL DU GÖRA?")
    print("=" * 80)
    print(" 1. öppna")

player = Player(Player.RAIDER)

print("Du hittade en stor mystisk kista!")
kista = Kista()
player.open_chest(kista)
player.show_status()


typing_speed = 50 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ("")



print("hejsan")
slow_type("hejsan")



karaktär = input("Välj en karaktär:")













