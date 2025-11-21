import math

def addera (a,b):
    svar = a + b
    return svar
"""
Adderar tal   
"""

def subtrahera (a,b):
    svar = a - b
    return svar
"""
Subtraherar tal
"""

def dividera (a,b):
    svar = a / b
    return svar
"""
Dividerar tal
"""

def multiplicera (a,b):
    svar =  a * b
    return svar
"""
Multiplicerar tal
"""

def nollställen (a,b,c):
    p=b/a
    q=c/a
    x1=-p/2 + math.sqrt((p/2)**2 - q)
    x2=-p/2 - math.sqrt((p/2)**2 - q)
    svar = [x1, x2]
    return svar
"""
Tar reda på nollställerna
"""


val = ""
while val!= "q":
    print(
        """
            Välkommen till calc!(kort för calculator)
           1. Addera           2. Subrtahera
           3. Dividera         4. multiplicera
           5. Hitta nollställen  6. derivera
           q. Avsluta
        """
    )

val = input("Välj ett av alternativen nedan:")

if val == "1":
    tal1 = int(input("Välj det första talet att addera ->"))
    tal2 = int(input("Välj det andra talet att addera -> "))
    svar = addera(tal1,tal2)
    print(f"Summan är {svar}")

elif val == "2":
    tal1 = int(input("Välj det första talet att subtrahera ->"))
    tal2 = int(input("Välj det andra talet att subrtrahera ->"))
    svar = subtrahera(tal1,tal2)
    print(f"Differensen är {svar}")

elif val == "3":
    tal1 = int(input("Välj det första talet att dividera ->"))
    tal2 = int(input("Välj det andra talet att dividera ->"))
    svar = dividera(tal1,tal2)
    print(f"Kvoten är {svar}")

elif val == "4":
    tal1 = int(input("Välj det första talet att multiplicera"))
    tal2 = int(input("Välj det andra talet att multiplicera"))
    svar = multiplicera(tal1,tal2)
    print(f"Produkten är {svar}")

elif val == "5":
    a = int(input("Ge koefficienten framför x^2 ->"))
    b = int(input("Ge koefficienten framför x ->"))
    c = int(input("Ge konstanttermen ->"))
    svar = nollställen()
    print(f"Nolställena är {svar[0]} och {svar[1]}")


print("Programmet avslutas")