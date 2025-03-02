# module complété par anya


import turtle
from trait import trait
from rectangle import rectangle


def fenetreBalcon(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    Remarque:
        Dessine une porte-fenetre avec balcon en 2 temps: la porte fenetre de 30 pixels de large par 50 pixels de hauteur
        puis le balcon
    '''
    # porte-fenetre
    turtle.pencolor("black")
    turtle.begin_fill()
    turtle.fillcolor("light blue")
    rectangle(x,y,30,50)
    turtle.end_fill()


    # balcon
    turtle.pencolor("black")
    turtle.pensize(1.48)
    rectangle(x,y,40,26)
    trait(x+3,y,x+3,y+27)
    trait(x+6,y,x+6,y+27)
    trait(x+9,y,x+9,y+27)
    trait(x+11.5,y,x+11.5,y+27)
    trait(x+17.5,y,x+17.5,y+27)
    trait(x+0,y,x+0,y+27)
    trait(x+-3,y,x+-3,y+27)
    trait(x+-6,y,x+-6,y+27)
    trait(x+-9,y,x+-9,y+27)
    trait(x+-12.5,y,x+-12.5,y+27)
    trait(x+-17.7,y,x+-17.7,y+27)



if __name__ == '__main__':
    fenetreBalcon(290,140)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
