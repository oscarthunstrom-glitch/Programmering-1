hemligt_tal = 67
gissning = None

while gissning != hemligt_tal:
    gissning = int(input("Gissa talet: "))
    if gissning > hemligt_tal:
        print("För högt!")
    elif gissning < hemligt_tal:
        print("För lågt!")
    else: 
        print("Rätt gissat!!!")