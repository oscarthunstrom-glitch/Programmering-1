namn = input("Skriv ditt namn:")

vokaler = "aeiouyåäöAEIOUYÅÄÖ"

for v in vokaler:
    namn = namn.replace(v, "")

print(f"Ditt namn utan vokaler är {namn}")