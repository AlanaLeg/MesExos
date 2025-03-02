# module complété par anya

import turtle
from couleurAleatoire import couleurAleatoire
from random import randint
from rdc import rdc
from etage import etage
from toit import toit


def immeuble(x, ySol):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
    Cette fonction dessine un immeuble Le nombre d'étage est compris aléatoirement entre 0 et 4
    La couleur de la façade et la couleur de la porte sont tirées au hasard
    '''
    turtle.speed(0)
     #Couleurs des éléments (aléatoire)
    turtle.colormode(255)
    col=couleurAleatoire()
    col2=couleurAleatoire()


    # Nombre d'étage (aléatoire)
    niveau= randint(1,5)


    # Dessin du RDC
    rdc(x, ySol, col, col2)

    # Dessin des étages

    if  niveau==2:
        etage(x, ySol+1*60, col,1)

    elif niveau==3:
         etage(x, ySol+1*60, col, 1)
         etage(x, ySol+2*60, col,2)
    elif niveau==4:
         etage(x, ySol+1*60, col,1)
         etage(x, ySol+2*60, col,2)
         etage(x, ySol+ 3*60, col,3)
    elif niveau==5:
        etage(x, ySol+1*60, col,1)
        etage(x, ySol+2*60, col,2)
        etage(x, ySol+3*60, col,3)
        etage(x, ySol+4*60, col,4)


    # Dessin du toit
    toit(x, ySol, niveau)



if __name__ == '__main__':
    immeuble(0,-100)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
