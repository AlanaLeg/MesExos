# module complété par Alana
# module toit2 (plat)

import turtle
from trait import trait

def toit2(x, ySol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        ySol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit plat d'épaisseur 10 pixels et mesurant 140 pixels de large
    '''
    turtle.pensize(10)
    trait(x-2-140/2, ySol+niveau*60, x+140/2+2,ySol+niveau*60)



if __name__ == '__main__':
    toit2(0,0,3)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
