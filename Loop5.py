x = -50

while x <= 50:
    y = -50
    while y <= 50:
        if 2*x + 3*y == 120:
            print(f"En lösning: (x, y) = ({x}, {y})")
        y += 1
    x += 1