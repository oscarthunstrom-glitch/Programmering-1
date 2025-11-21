korrekt_lösenord = "bAnaN459"
försök = 0
max_försök = 3

while försök < max_försök:
    kollen = input("Ange lösenord:")
    if kollen == korrekt_lösenord:
        print("Välkommen!")
    else:
        print("Fel lösenord, försök igen:")
        försök += 1

if försök == max_försök:
    print("För många försök. Programmet avslutas.")