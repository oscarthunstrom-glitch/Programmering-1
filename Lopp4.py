import random as rand

hemligt_tal = rand.randint(1, 10)
antal_gissningar = 0

while True:
    gissning = int(input("Gissa ett tal mellan 1 och 10 ->"))
    antal_gissningar += 1
    if gissning > hemligt_tal:
        print(f"Talet {gissning} är för stort.")
    elif gissning < hemligt_tal:
        print(f"Talet {gissning} är för litet.")
    else:
        print("RÄTT GISSAT!")
        break
print(f"Du klarade spelet på gissning nr. {antal_gissningar}.")