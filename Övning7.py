pris_järn = 200
pris_silver = 500
pris_guld = 1000

budget = int(input("Ange din budget:"))

if(budget >= 1000):
    print("Din budget räcker till ett guldsmycke!")
elif(budget >= 500):
    print("Din budget räcker till ett silversmycke")
elif(budget >= 200):
    print("Din budget räcker till ett järnsmycke!")
else:
    print("Du har tyvärr inte råd med något smycke!")

print("Programmet avslutas")