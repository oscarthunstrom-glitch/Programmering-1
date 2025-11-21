mening = input("Skiv en mening: ")
vokaler = "aeiouyåäöAEIOUYÅÄÖ"
antal = 0

for tecken in mening: 
    if tecken in vokaler:
        antal += 1

print("Antal vokaler:", antal)