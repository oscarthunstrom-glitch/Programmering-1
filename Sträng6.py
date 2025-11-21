text = input("Skriv ex text som ska översättas till rövarspråket: ")

konsonanter = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

rovarsprak = ""

for bokstav in text:
    if bokstav in konsonanter:
        rovarsprak += bokstav + "o" + bokstav.lower()
    else:
        rovarsprak += bokstav

print("Rövarspråket blir:", rovarsprak)