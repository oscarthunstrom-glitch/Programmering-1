def rakna_tecken(text):
    antal = 0
    for _ in text:
        antal += 1
    return antal 

text = "Hej"
resultat = rakna_tecken(text)
print(f"Antal tecken i \"{text}\": {resultat}")