längd = int(input("Ange längden på rektangeln i centimeter: "))
bredd = int(input("Ange bredden på rektangeln i centimeter: "))

area = längd * bredd
if bredd == längd:
    print("Det är inte en rektangel utan en kvadrat, gör om och gör rätt")
elif bredd > längd:
    print("Bredden kan inte vara längre än längden, gör om och gör rätt")
else: 
    print(f"Rektangelns area är {area} kvadratcentimer")