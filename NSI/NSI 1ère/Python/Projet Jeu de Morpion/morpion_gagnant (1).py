# Créé par passage, le 12/02/2024 en Python 3.7

from morpionest_terminer import est_terminer

g1= {"A1": "o", "A2":"o", "A3": "o", "B1":"x", "B2":"o", "B3":"x", "C1": "o", "C2":"x", "C3":"x"}
g2= {"A1": "x", "A2":"x", "A3": "o", "B1":"x", "B2":"o", "B3":"o", "C1": "x", "C2":"x", "C3":"o"}
g3= {"A1": "o", "A2":"o", "A3": "x", "B1":"o", "B2":"x", "B3":"x", "C1": "x", "C2":"o", "C3":"x"}
g4= {"A1": "x", "A2":"x", "A3": "o", "B1":"o", "B2":"o", "B3":"x", "C1": "x", "C2":"o", "C3":"x"}


def gagnant(grille):
    # joueur a gagné
    if  grille["A1"]== grille["A2"]==grille["A3"]== "x":
        return "Vous êtes le gagnant"
    elif grille["B1"]== grille["B2"]==grille["B3"]== "x":
        return "Vous êtes le gagnant"
    elif grille["C1"]== grille["C2"]==grille["C3"]== "x":
        return "Vous êtes le gagnant"
    elif grille["A1"]== grille["B1"]==grille["C1"]== "x":
        return "Vous êtes le gagnant"
    elif grille["A2"]== grille["B2"]==grille["C2"]== "x":
        return "Vous êtes le gagnant"
    elif grille["A3"]== grille["B3"]==grille["C3"]== "x":
        return "Vous êtes le gagnant"
    elif grille["A1"]== grille["B2"]==grille["C3"]== "x":
        return "Vous êtes le gagnant"
    elif grille["C1"]== grille["B2"]==grille["A3"]== "x":
        return "Vous êtes le gagnant"
    #machine a gagné
    elif grille["B1"]==grille["B2"]==grille["B3"]== "o":
        return "La machine a gagné"
    elif grille["A1"]==grille["A2"]==grille["A3"]== "o":
        return "La machine a gagné"
    elif grille["C1"]==grille["C2"]==grille["C3"]== "o":
        return "La machine a gagné"
    elif grille["A1"]==grille["B1"]==grille["C1"]== "o":
        return "La machine a gagné"
    elif grille["A2"]==grille["B2"]==grille["C2"]== "o":
        return "La machine a gagné"
    elif grille["A3"]==grille["B3"]==grille["C3"]== "o":
        return "La machine a gagné"
    elif grille["A1"]==grille["B2"]==grille["C3"]== "o":
        return "La machine a gagné"
    elif grille["C1"]==grille["A2"]==grille["B3"]== "o":
        return "La machine a gagné"
    elif " " not in grille.values():
        return "match nul"
