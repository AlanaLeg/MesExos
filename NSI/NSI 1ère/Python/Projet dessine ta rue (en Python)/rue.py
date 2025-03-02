# module complété par anya
# programme principal (dessine une rue)


import turtle
from random import randint, shuffle
from sol import sol
from immeuble import immeuble
# ------------------------------
# ------------------------------
# ------------------------------

def main():
    turtle.setup(800, 600)
    turtle.speed(2)
    # On définit la hauteur du sol
    y_sol = -200
    # Dessin du sol de la rue
    sol(y_sol)

    # Dessin des 4 immeubles
    turtle.pensize(1)
    immeuble(-300,y_sol)
    turtle.pensize(1)
    turtle.penup()
    turtle.setposition(-100,y_sol)
    turtle.pendown()
    immeuble(-100, y_sol)
    turtle.pensize(1)
    turtle.penup()
    turtle.setposition(110,y_sol)
    turtle.pendown()
    immeuble(110,y_sol)
    turtle.pensize(1)
    turtle.penup()
    turtle.setposition(300,y_sol)
    turtle.pendown()
    immeuble(300,y_sol)


    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()

if __name__ == '__main__':
    main()



