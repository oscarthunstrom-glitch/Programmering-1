tal_lista = []

for i in range(5):
    tal = int(input(f"Ange tal {i+1}: "))
    tal_lista.append(tal)

största = max(tal_lista)
print("Det största talet i listan är:", största)