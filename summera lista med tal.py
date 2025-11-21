antal = int(input("Hur många tal vill du skriva in? "))
tal_lista = []

for i in range(antal):
    tal = int(input(f"Skriv tal {i+1}: "))
    tal_lista.append(tal)

print("Summan av talen är:", sum(tal_lista))