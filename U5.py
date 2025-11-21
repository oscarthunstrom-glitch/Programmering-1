import random

# antal rader och kolumner
rows = 10
cols = 10

for _ in range(rows):
    rad = ""
    for _ in range(cols):
        rad += random.choice(["*", "-"])
    print(rad)
