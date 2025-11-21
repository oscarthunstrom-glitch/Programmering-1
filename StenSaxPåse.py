import os

print("Välkommen till sten, sax, påse spel. ")

namn1 = input("Spelare 1, skriv in ditt namn: ")
namn2 = input("Spelare 2, skriv in ditt namn: ")

val1 = input(f"{namn1}, välj sten, sax eller påse: "). lower()
os.system("cls")
val2 = input(f"{namn2}, välj sten sax eller påse: "). lower()


if val1 == val2:
    print(f"Oavgjort! Båda valde {val1}")


elif val1 == "sten":
    if val2 == "sax":
        print(f"{namn1} vinner! {namn1}'s sten krossar {namn2}'s sax!")
    elif val2 == "påse":
        print(f"{namn2} vinner! {namn2}'s påse täcker {namn1}'s sten!")
    else: 
        print(f"{namn2} gjorde ett ogiltigt val.")

elif val1 == "sax":
    if val2 == "påse":
        print(f"{namn1} vinner! {namn1}'s sax klipper sönder {namn2}'s påse!")
    elif val2 == "sten":
        print(f"{namn2} vinner! {namn2}'s sten krossar {namn1}'s sax!")
    else:
        print(f"{namn2} gjorde ett ogiltigt val.")

elif val1 == "påse":
    if val2 == "sten":
        print(f"{namn1} vinner! {namn1}'s påse täcker {namn2}'s sten!")
    elif val2 == "sax":
        print(f"{namn2} vinner! {namn2}s sax klipper sönder {namn1}s påse!")
    else:
        print(f"{namn2} gjorde ett ogiltigt val.")

else:
    print(f"{namn1} gjorde ett ogiltigt val.")