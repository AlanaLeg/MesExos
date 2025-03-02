# Créé par aleguay1, le 04/11/2024 en Python 3.7

from random import randint

class Carte:
    def __init__(self, val, forme):
        self.valeur = val
        self.forme = forme

    def __str__(self):
        if self.valeur == 14:
            return "As" + " de " + self.forme
        elif self.valeur == 11:
            return "Valet" + " de " + self.forme
        elif self.valeur == 12:
            return "Dame" + " de " + self.forme
        elif self.valeur == 13:
            return "Roi" + " de " + self.forme
        else:
            return str(self.valeur) + " de " + self.forme

    def est_egal(self, carte):
        return self.valeur == carte.valeur

    def domine(self, carte):
        return self.valeur > carte.valeur


c1= Carte(8, "Pique")
c2= Carte(11, "Carreau")
c3= Carte(8, "Carreau")

class Paquet:
    def __init__(self, liste):
        #self.carte = carte
        #self.forme = forme
        self.liste_de_cartes = liste

    def creer_paquet(self, entier):
        if entier == 32:
        #paquet = Paquet(P=[ ])
            for i in range(7,15):
                for j in ["Carreau","Coeur","Pique","Trèfle"]:
                    c_i = Carte(i, j)
                    self.liste_de_cartes.append(c_i)

        if entier == 52:
        #paquet = Paquet(P=[ ])
            for i in range(2,15):
                for j in ["Carreau","Coeur","Pique","Trèfle"]:
                    c_i = Carte(i, j)
                    self.liste_de_cartes.append(c_i)


    def nombre_cartes(self):
        return len(self.liste_de_cartes)

    def nombre_as(self, p):
        compte= 0
        for i in p.liste_de_cartes:
            if i == p.listes_de_cartes[14] :
                compte += 1
        return compte

    def est_vide(self, p):
        return len(p.listes_de_cartes) == 0

    def melanger(self):
        liste = [ ]
        for i in range(len(self.liste_de_cartes)):
            liste.append(self.liste_de_cartes.pop(randint(0, len(self.liste_de_cartes)-1))
        self.liste_de_cartes = liste


    def distribuer(self, p):
        paquet_1 = Paquet([ ])
        for i in range(len(p.listes_de_cartes) / 2):
            paquet_1.listes_de_cartes.append(i)
        return p, paquet_1

    def tirer_first(self):
        return self.liste_de_cartes.pop()

    def tirer_random(self):
        tirer = randint(len(self.liste_de_cartes))
        return self.liste_de_cartes.pop(tirer)

    def ramasse(self, p):
        self.liste_de_cartes = self.liste_de_cartes + p.liste_de_cartes



p1=Paquet([])
p1.creer_paquet(52)
#print(p1.liste_de_cartes[0])

def tour_jeu():
    #joueur1= Paquet([ ])
    #joueur2= Paquet([ ])
    print("joueur1 : " + str(len(joueur1.liste_de_cartes)) + "cartes" + " | " + "joueur2 : " + str(len(joueur2.liste_de_cartes)) + "cartes")

    carte = joueur1.tirer_first()
    carte_2 = joueur2.tirer_first()

    print("joueur1 joue: " + str(carte) + " | " "joueur2 joue: " + str(carte_2))
    if carte.domine(carte_2) == True:
        joueur1.ramasse(carte)
        joueur1.ramasse(carte_2)
        print("joueur1 gagne et ramasse 2 cartes")
    elif carte_2.domine(carte) == True:
        joueur2.ramasse(carte)
        joueur2.ramasse(carte_2)
        print("joueur2 gagne et ramasse 2 cartes")
    elif carte.est_egal(carte_2) == True:
        while carte.est_egal(carte_2) == True:
            print("Bataille !")

            carte_cache = [ ]
            carte_cache.append(joueur1.tirer_random())

            carte_2_cache = [ ]
            carte_2_cache.append(joueur2.tirer_random())
            print("joueur1 cache: " + str(carte_cache) + " | " + "joueur2 cache: " + str(carte_2_cache))

            new_carte = joueur1.tirer_first()
            new_carte_2 = joueur2.tirer_first()
            print("joueur1 joue: " + new_carte + " | " "joueur2 joue: " + new_carte_2)
            carte_cache.append(new_carte)
            carte_2_cache.append(new_carte_2)
            if new_carte.domine(new_carte_2) == True:
                joueur1.ramasse(carte_cache)
                joueur1.ramasse(carte_2_cache)
                print("joueur1 gagne et ramasse " + str(len(carte_cache)+len(carte_2_cache)) + " cartes")
            elif new_carte_2.domine(new_carte) == True:
                joueur2.ramasse(carte_cache)
                joueur2.ramasse(carte_2_cache)
                print("joueur2 gagne et ramasse " + str(len(carte_cache)+len(carte_2_cache)) + " cartes")






