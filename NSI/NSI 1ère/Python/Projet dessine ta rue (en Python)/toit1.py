# module complété par anya
# module toit1 (triangulaire)

import turtle
from trait import trait

def toit1(x, ySol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        ySol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit triangulaire noir de base 160 pixels
    et de hauteur centrale 40 pixels
    '''
    turtle.pencolor("black")
    turtle.penup()
    turtle.setposition(x,ySol+niveau*60)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("black")
    trait(x,ySol+niveau*60,x+160/2,ySol+niveau*60)
    trait(x+160/2,ySol+niveau*60,x,ySol+niveau*60+40)
    trait(x,ySol+niveau*60+40,x-160/2,ySol+niveau*60)
    trait(x-160/2,ySol+niveau*60,x+160/2,ySol+niveau*60)
    turtle.end_fill()

if __name__ == '__main__':
    toit1(25,20,1)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
