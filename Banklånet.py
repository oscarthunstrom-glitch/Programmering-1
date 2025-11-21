ålder = int(input("Hur gammal är du?"))
månadsinkomst = int(input("Hur mycket tjänar du?"))

if(ålder>= 18 or månadsinkomst>= 18000):
    print("Du kan ta ett lån!")
else:
    print("Du kan tyvärr inte ta ett lån!")