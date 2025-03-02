# module complété par Alana

import turtle
from rectangle import rectangle

def facade(x, ySol, couleur, niveau):
    '''
    Paramètres :
        x : abcisse du centre de la façade
        ySol : ordonnée du sol du la rue
        couleur : couleur de la façade
        niveau : num du niveau (0 pour les rdc, ...)
    remarque :
        Facade dessine une facade sans les élements interieurs
    '''

    turtle.color(couleur)
    turtle.pencolor("black")
    turtle.begin_fill()
    rectangle(x, ySol, 150, 60)
    turtle.end_fill()





if __name__ == '__main__':
    facade(0,0,"red",0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
