import random

hemligt_tal = random.randint(1, 100)
gissning = 0

while gissning != hemligt_tal: 
    gissning = int(input("Gissa talet mellan 1-100: "))
    if gissning < hemligt_tal:
        print("För lågt!")
    elif gissning > hemligt_tal:
        print("För högt!")
    else: 
        print("Rätt gissat:")