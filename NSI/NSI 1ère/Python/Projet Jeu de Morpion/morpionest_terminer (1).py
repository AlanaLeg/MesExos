# Créé par passage, le 08/02/2024 en Python 3.7

dico={"A1":"o","A2":"x","A3":"o","B1":"x","B2":"o","B3":"o","C1":"x","C2":"o","C3":"x"}

from morpionaffiche import affiche

def est_terminer(grille):
    if grille["A1"]== grille["A2"]==grille["A3"]== "x" or grille["A1"]==grille["A2"]==grille["A3"]== "o":
        return True
    elif grille["B1"]== grille["B2"]==grille["B3"]== "x" or grille["B1"]==grille["B2"]==grille["B3"]== "o":
        return True
    elif grille["C1"]== grille["C2"]==grille["C3"]== "x" or grille["C1"]==grille["C2"]==grille["C3"]== "o":
        return True
    elif grille["A1"]== grille["B1"]==grille["C1"]== "x" or grille["A1"]==grille["B1"]==grille["C1"]== "o":
        return True
    elif grille["A2"]== grille["B2"]==grille["C2"]== "x" or grille["A2"]==grille["B2"]==grille["C2"]== "o":
        return True
    elif grille["A3"]== grille["B3"]==grille["C3"]== "x" or grille["A3"]==grille["B3"]==grille["C3"]== "o":
        return True
    elif grille["A1"]== grille["B2"]==grille["C3"]== "x" or grille["A1"]==grille["B2"]==grille["C3"]== "o":
        return True
    elif grille["C1"]== grille["B2"]==grille["A3"]== "x" or grille["C1"]==grille["A2"]==grille["B3"]== "o":
        return True
    elif " " not in grille.values():
        return True
    else:
        return False
