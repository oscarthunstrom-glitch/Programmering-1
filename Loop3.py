import random as rand
i = 1
print(f"{'Match nr':>10}. {'Resultat' :>11}")
print("====================")
while i <= 13:
    res = rand.randint(1,3)
    if res ==1: 
        res = "1"
    elif res ==2:
        res = "x"
    else:
        res = "2"
    print(f"{i:6.0f} {res:>12}")
    print("-------------------")
    i+=1