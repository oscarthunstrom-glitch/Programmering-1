import random 
from Player import *
from Monster import *
import sys,time

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













