# Créé par passage, le 08/02/2024 en Python 3.7
from random import choice
from random import randint
from morpionest_terminer import est_terminer
from morpionaffiche import affiche
from script import machine
from morpion_gagnant import gagnant
from time import sleep

g1= {"A1": " ", "A2":" ", "A3": " ", "B1":" ", "B2":" ", "B3":" ", "C1": " ", "C2":" ", "C3":" "}
g2= {"A1": "x", "A2":" ", "A3": "o", "B1":" ", "B2":"o", "B3":" ", "C1": " ", "C2":"x", "C3":" "}
g3= {"A1": "o", "A2":"o", "A3": "x", "B1":"o", "B2":"x", "B3":"x", "C1": "x", "C2":"o", "C3":"x"}

def morpion():
    g0={"A1": " ", "A2":" ", "A3": " ", "B1":" ", "B2":" ", "B3":" ", "C1": " ", "C2":" ", "C3":" "}

    j=randint(1,2)
    if j==1:
        case_m=machine(g0)
        g0[case_m]="o"
        affiche(g0)
        sleep(1)
    case_h=input("choisit un case de la grille entre A1 et C3: ")
    g0[case_h]="x"
    affiche(g0)
    sleep(1)


    while est_terminer(g0)== False:
        case_m=machine(g0)
        g0[case_m]="o"
        affiche(g0)
        sleep(1)
        if est_terminer(g0)== False:
            case_h=input("choisit une case de la grille entre A1 et C3: ")
            g0[case_h]="x"
            affiche(g0)
            sleep(1)
    print(gagnant(g0))










