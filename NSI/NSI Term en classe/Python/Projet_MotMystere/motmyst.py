from random import randint
import pandas
import re
datamot = pandas.read_csv("liste_francais_22k.txt")
datamot2 = datamot.loc[(datamot.mot.str.contains("!", regex = True) == False)]
datamot3 = datamot2.loc[(datamot2.mot.str.contains("^[a-z]", regex = True) == True)]
datamot4 = datamot3.loc[(datamot3.mot.apply(len))>4]
datalist = datamot4.mot.to_list()
L = ["banane", "chocolat", "chaise", "chat", "chien", "poulet", "texte", "ordinateur"]
def choix_mot(datalist):
    ind_myst = randint(0, len(datalist)-1)
    return datalist[ind_myst]

def mot_mystere(mot_myst):
    underscore = ""
    for i in range(len(mot_myst)):
        if mot_myst[i] =="-":
            underscore += "- "
        underscore += "_ "
        if i == len(mot_myst) - 2:
            underscore += "_"
            return underscore

def verification(lettre, mot):
    return lettre in mot

def completer_mot(lettre, mot, mot_myst):
    new_mot = ""
    for i in range(len(mot)):
        if mot[i] == lettre:
            new_mot += lettre + " "
        else:
            new_mot += mot_myst[i*2] + " "
    return new_mot[:-1]


def rating(mot):
    score = 100
    p = 0
    note = 0
    L = []
    for i in mot:
        if i in "easitn":
            p += -5
        if i in "rulod":
            p = (-2)
        elif i in "cmpvq":
            p += 2
        elif i == "fbghjxy":
            p += 7
        if i in L:
            p += -10
        else:
            p += 10
        L.append(i)
    if len(L) >= 6:
        p += -10

    note = (score + p)/10
    if note > 10:
        note = 10
    return note



def niveau(note):
    niv = ""
    if note < 8:
        niv = "difficile"
    if note < 8:
        niv = "difficile"
    if note < 8:
        niv = "difficile"







def jeu():
    mot_non_presents = []
    tentatives = int(input("Donnez votre nombre de tentatives: "))
    cm = choix_mot(datalist)
    myst = mot_mystere(cm)
    while "_" in myst and tentatives > 0:
        print(myst)
        devine = input("Choisir une lettre: ")
        if type(devine) == int:
            devine = input("Choisissez une lettre et non un chiffre")
        if len(devine) == str and len(devine) > 1:
            devine = input("Choisissez une seule lettre")
        if verification(devine, cm):
            myst = completer_mot(devine, cm, myst)
        else:
            tentatives -= 1
            if devine in mot_non_presents:
                pass
            if type(devine) != str and len(devine) != 1:
                pass
            else:
                mot_non_presents.append(devine)
        if tentatives == 0:
            print("Perdu ! Le mot était: " + cm)
            break
        if "_" not in myst:
            print("Bravo, vous avez gagné!")
            print(myst)
            break
        print("Nombre de tentatives restantes: " + str(tentatives))
        print("Lettres non présentes: " + str(mot_non_presents))