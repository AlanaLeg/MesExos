#Projet NSi: Le mot Mystère

from random import randint
import pandas
datamot=pandas.read_csv("liste_francais_22k.txt")
import re
datamot2 = datamot.loc[ (datamot.mot.str.contains('!', regex=True)== False) ]
datamot3 = datamot2.loc[ (datamot2.mot.str.contains('^[a-z]', regex=True)== True) ]
datamot4 = datamot3.loc[ (datamot3.mot.apply(len))>4 ]


#Fonction de contruction du jeux

L0 = ["pomme", "poire","banane", "epinard", "haricot"]


def choix_mot(L):
    mot = ""
    c = randint(0, len(L)-1)
    mot += L[c]
    return mot

def choix_mot2(data):
    c = randint(0, len(data.loc[:, "mot"])-1)
    return data.loc[c, "mot"]

print("--Test choix_mot2--")
print(choix_mot2(datamot2))


def mot_mystere(mot):
    mot_m= ""
    for i in range(len(mot)):
        if mot[i] == "-":
            mot_m += "-"
        elif i == -1:
            mot_m += "_"
        else:
            mot_m += "_ "
    return mot_m

print("--Test mot_mystere--")
a = "croc-en-jambe"
#print(a)
#print(mot_mystere(a))


def verification(lettre, mot):
    return lettre in mot


def completer_mot(lettre, mot, myst):
    my= ""
    for i in range(len(mot)):
        if mot[i] == lettre:
            my = my + lettre + " "
        else:
            my = my + myst[i*2] + " "
    return my[:-1]

def rating(mot):
    p = 0 #p est le nombre de points qu'on soustrait
    note = 0
    list = []
    for i in mot:
        if i in "easitn":
            p += -5
        if i in "rulod":
            p += -2
        elif i in "cmpvq":
            p += 6
        elif i in "fbghjxy":
            p += 7
        if i == "-":
            p += 5
        if i in list :
            p += -10
        else:
            p += 10
        list.append(i)
    if len(list) >= 6:
        p += 5
    if len(mot) < 6:
        p += -5
    note = ((100 + p)/10)//2
    #if note > 10:
    #    note = 10
    #print ("Le mot "+ mot + " un niveau de difficulté évalué à : " + str(note) + " sur 10.")
    return note


def rating_max(data):
    max = ""
    for mot in data.loc[:, "mot"]:
        n = rating(mot)
        if n == 10:
            max = mot
    return max

def rating_min(data):
    min = ""
    for mot in data.loc[:, "mot"]:
        n = rating(mot)
        if n == 0:
            min = mot
    return min

#le rating max est atteint avec : zygomatique 10
#le rating min est : interministerielle 0


print("--Test rating--")
#mot_z = choix_mot2(datamot4)
#print(mot_z)
#print(rating(mot_z))
#print(rating("bob"))
#print("--Test rating_2--")
#print(rating_max(datamot))
#print(rating_min(datamot))


#Programme du Jeu Mot Mystère

def jeu():
    mot = ""
    m = ""
    T = 0
    N_present = []
    niv = input ("Choisir un niveau de difficulté : 1 (pour le niveau facile), 2 (pour le niveau normal) et 3 (pour le niveau difficile) : ")
    if niv == "1":
        Ti = T + 14
        mot = choix_mot2(datamot4)
        m = mot_mystere(mot)
    elif niv == "2":
        Ti = T + 10
        mot = choix_mot2(datamot3)
        m = mot_mystere(mot)
    elif niv == "3":
        Ti = T + 7
        c = randint(0, len(datamot.loc[:, "mot"])-1)
        if rating(datamot.loc[c, "mot"]) >= 5:
            mot = datamot.loc[c, "mot"]
            m = mot_mystere(mot)
    print("Nombre de tentative(s) restante(s) :" + str(Ti) + ". Niveau de difficulté choisi: " + niv + ".")
    print(m)
    Tf = Ti
    while "_" in m and Tf > 0:
        lettre = input ("Choisir une lettre:")
        if verification(lettre, mot) == True :
            m = completer_mot(lettre, mot, m)
            print(m)
        if len(lettre) > 1:
                print("L'élément choisi doit contenir qu'une seule chaîne de caratère.")
        elif lettre in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                print("L'élément choisi n'est pas une chaîne de caratères.")

        elif verification(lettre, mot) != True and lettre not in N_present:

            Tf = Tf-1
            N_present.append(lettre)
            print("La lettre '" + lettre + "' n'est pas dans le mot mystere.")
            print("lettre(s) non présente(s): " + str(N_present))
            print("Nombre de tentative(s) restante(s) :" + str(Tf))
            print(m)
        elif verification(lettre, mot) != True and lettre in N_present:
            print("La lettre " + lettre + " a déjà été choisie et n'est pas dans le mot")

    if Tf == 0 and "_" in m:
        print("Perdu. Le mot était " + mot + ".")
    else:
        print("Bravo, vous avez gagné en " + str(Ti - Tf) + " tentative(s)! Le mot était bien '" + mot + "'.")
print("--Test Jeu--")
jeu()