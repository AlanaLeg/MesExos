# Créé par aleguay1, le 15/10/2024 en Python 3.7

#ex5
def milieu(cdc):
    n=len(cdc)
    i = (n/2)-0.5
    #print(i)
    return cdc[int(i)]

#ex6
def nb_lettres(prenom, nom):
    return len(prenom) + len(nom)

def nb_lettres_2(p, n):
    nb= len(p) + len(n)
    return nb

#ex7
def samelong(cdc, mot):
    if len(cdc) == len(mot):
        return True
    else:
        return False

def samelong_2(cdc, mot):
    return len(cdc) == len(mot)

#ex8
def nsi1(cdc):
    for i in cdc:
        if i == "n" or "s" or "i":
            return True
        else:
            return False
    return False

