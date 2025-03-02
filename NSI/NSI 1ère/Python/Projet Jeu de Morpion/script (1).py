
from random import choice
from morpionaffiche import affiche
from morpionest_terminer import est_terminer
Humain='x'
Machine= 'o'
g1= {"A1": " ", "A2":" ", "A3": " ", "B1":" ", "B2":" ", "B3":" ", "C1": " ", "C2":" ", "C3":" "}
g2= {"A1": "x", "A2":" ", "A3": "o", "B1":" ", "B2":"o", "B3":" ", "C1": " ", "C2":"x", "C3":" "}
g3= {"A1": "o", "A2":"o", "A3": "x", "B1":"o", "B2":"x", "B3":"x", "C1": "x", "C2":"o", "C3":"x"}



def machine(grille):
    assert " " in grille.values(), 'la grille doit comporter au moins une case vide'
    case_m=choice(["A1","A2","A3","B1","B2","B3","C1","C2","C3"])
    while grille[case_m] !=" ":
        case_m=choice(["A1","A2","A3","B1","B2","B3","C1","C2","C3"])
    return case_m






