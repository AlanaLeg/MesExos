# module complété par Alana

from facade import facade
from random import randint
from fenetre import fenetre
from fenetreBalcon import fenetreBalcon
import turtle

def etage(x, ySol, couleur, niveau):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        ySol : ordonnée du sol du la rue
        couleur : couleur de la façade de l'étage
        niveau : numéro de l'étage en partant de 0 pour le rdc
    Remarque
       Cette fonction dessine un étage d'un immeuble
    '''
    # dessin des murs
    facade(x, ySol, couleur, niveau)

    # dessin les 3 Eléments
    r=randint(0,7)
    if r==0:
        fenetre(x-40,ySol+20)
        fenetre(x, ySol+20)
        fenetreBalcon(x+40, ySol)
    elif r==1:
        fenetre(x-40, ySol+20)
        fenetreBalcon(x, ySol)
        fenetre(x+40,ySol+ 20)
    elif r==2:
        fenetreBalcon(x-40, ySol)
        fenetre(x, ySol+20)
        fenetreBalcon(x+40, ySol)
    elif r==3:
        fenetre(x-40,ySol+20)
        fenetre(x,ySol+20)
        fenetre(x+40,ySol+20)
    elif r==4:
        fenetre(x-40,ySol+20)
        fenetreBalcon(x,ySol)
        fenetreBalcon(x+40,ySol)
    elif r==5:
        fenetreBalcon(x-40,ySol)
        fenetre(x,ySol+20)
        fenetre(x+40,ySol+20)
    elif r==6:
        fenetreBalcon(x-40, ySol)
        fenetreBalcon(x,ySol)
        fenetre(x+40,ySol+20)
    elif r==7:
        fenetreBalcon(x-40,ySol)
        fenetreBalcon(x,ySol)
        fenetreBalcon(x+40,ySol)












if __name__ == '__main__':
    etage(0,0,"red",0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
