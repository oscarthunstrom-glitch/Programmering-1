a = int(input("Hur lång är sida a?"))
b = int(input("Hur lång är sida b?"))
c = int(input("Hur lång är sida c?"))

if(a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
    print(f"Sidorna {a}, {b} och {c} kan bilda en rätvinlig triangel!")
elif(a +b > c) and (a + c> b) and (b +c > a):
    print(f"Sidorna {a}, {b} och {c} kan bilda en triangel som inte är rätvinklig!")
else:
    print(f"Sidorna {a}, {b} och {c} kan inte bilda en triangel!")
    