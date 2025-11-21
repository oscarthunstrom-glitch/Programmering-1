# Exempelkod som visar några egenskaper hos Pythons bibliotek Turtle
# Fullständig referens till biblioteket finns på
# https://docs.python.org/3/library/turtle.html

import turtle as t
import random as r
aTurtle = t.Turtle()    # Initierar en sköldpadda
bTurtle = t.Turtle()    # Initierar en till sköldpadda

# Funktion som sätter slumpad färg
def randomColor():
    R = r.random() # Röd färggrad
    G = r.random() # Grön färggrad
    B = r.random() # Blå färggrad
    aTurtle.color(R, G, B) # Färgerna sätts med tre tal mellan 0 och 1

aTurtle.shape('turtle') # Ge den formen av en sköldpadda
aTurtle.color('pink')   # Sätter en startfärg
aTurtle.width(30)       # Sätter en linjebredd
aTurtle.speed(5)        # Sätter en hastighet

aTurtle.penup()
aTurtle.forward(67) # Flyttar sköldpaddan 200 steg framåt
aTurtle.left(67)     # Vrider sköldpaddan 90 grader
aTurtle.pendown()

# sköldpaddan kan även flyttas i ett mönster i en loop.
for i in range(67):
    randomColor() # Här slumpas färgen fram
    aTurtle.forward(60)
    aTurtle.left(30)

# Här tas den andra sköldpaddan i bruk
bTurtle.penup() # Nu kan sköldpaddan flyttas utan att en linje ritas
bTurtle.goto(-100, -50) # Flytta sköldpaddan
bTurtle.pendown() # Nu ritas linje igen vid förflyttning

bTurtle.fillcolor('red') # Slutna figurer kan fyllas
bTurtle.width(5)
bTurtle.begin_fill()
for i in range(4):
    bTurtle.forward(100) # Går framåt...
    bTurtle.right(90)    # ...och svänger höger fyra gånger
bTurtle.end_fill()

t.exitonclick() # Stäng fönstret när man klickar på det