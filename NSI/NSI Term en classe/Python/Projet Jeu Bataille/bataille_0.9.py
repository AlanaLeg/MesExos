#jeu classique
from random import randint
from random import shuffle

class Carte:
    def __init__(self, val, couleur):
        self.valeur = val
        self.couleur = couleur

    def __str__(self):
        if self.valeur == 14:
            return "as" + " de " + self.couleur
        elif self.valeur == 11:
            return "valet" + " de " + self.couleur
        elif self.valeur == 12:
            return "dame" + " de " + self.couleur
        elif self.valeur == 13:
            return "roi" + " de " + self.couleur
        else:
            return str(self.valeur) + " de " + self.couleur

    def est_egal(self, carte):
        return self.valeur == carte.valeur

    def domine(self, carte):
        return self.valeur > carte.valeur


class Paquet:
    def __init__(self,L):
        self.L = L

    def nbr_cartes(self):
        return len(self.L)

    def nbr_as(self):
        nombres_as = 0
        for i in self.L:
            if i.valeur == 14:
                nombres_as += 1
        return nombres_as

    def est_vide(self):
        return len(self.L) == 0

    def melanger(self):
        new_list = []
        for i in range(self.nbr_cartes()):
            new_list.append(self.L.pop(randint(0,len(self.L)-1)))
        self.L = new_list

    def distribuer(self):
        new_list = []
        for i in range(self.nbr_cartes()//2):
            new_list.append(self.L.pop(randint(0,len(self.L)-1)))
            p2 = Paquet(new_list)
        return self, p2

    def tirer_first(self):
        return self.L.pop(0)

    def tirer_random(self):
        return self.L.pop(randint(0,len(self.L)-1))

    def ramasse(self, liste_de_cartes):
        shuffle(liste_de_cartes)
        for i in liste_de_cartes:
            self.L.append(i)


def creer_paquet(format):
    L=[]
#format 32 cartes
    if format == 32:
        for i in ["pique","trefle","carreau","coeur"]:
            for j in range(8):
                L.append(Carte(j+7, i))
#format 52 cartes
    elif format == 52:
        for i in ["pique","trefle","carreau","coeur"]:
            for j in range(13):
                L.append(Carte(j+2, i))
    p0 = Paquet(L)
    return p0


def tour_jeu(joueur1, joueur2):
    print('')
    print("joueur1 : " + str(len(joueur1.L)) + "cartes" + " | " + "joueur2 : " + str(len(joueur2.L)) + "cartes")
    carte_a_recup=[]
    carte = joueur1.tirer_first()
    carte_2 = joueur2.tirer_first()
    print("joueur1 joue: " + str(carte) + " | " "joueur2 joue: " + str(carte_2))

    if carte.domine(carte_2) == True:
        print("joueur1 gagne et ramasse 2 cartes")
        carte_a_recup += (carte, carte_2)
        joueur1.ramasse(carte_a_recup)

    elif carte_2.domine(carte) == True:
        print("joueur2 gagne et ramasse 2 cartes")
        carte_a_recup += (carte, carte_2)
        joueur2.ramasse(carte_a_recup)

    #dans le cas d'une bataile
    elif carte.est_egal(carte_2) == True:
        while carte.est_egal(carte_2):
            print("Bataille !")
            #derniere chance
            if len(joueur1.L) < 3 or len(joueur2.L) < 3:
                if len(joueur1.L) < 3:
                    print("dernière chance pour le joueur1")
                    joueur1.L.append(joueur2.tirer_random())
                    joueur1.L.append(joueur2.tirer_random())
                else:
                    print("dernière chance pour le joueur2")
                    joueur2.L.append(joueur1.tirer_random())
                    joueur2.L.append(joueur1.tirer_random())

            carte_cache, carte_2_cache = joueur1.tirer_random(), joueur2.tirer_random()
            print("joueur1 cache: " + str(carte_cache) + " | " + "joueur2 cache: " + str(carte_2_cache))
            new_carte, new_carte_2 = joueur1.tirer_first(), joueur2.tirer_first()

            #pour eviter de rajouter plusieurs fois la meme carte
            if len(carte_a_recup) > 0:
                carte_a_recup += (carte_cache, carte_2_cache, new_carte, new_carte_2)
            else:
                carte_a_recup += (carte, carte_2, carte_cache, carte_2_cache, new_carte, new_carte_2)

            print("joueur1 joue: " + str(new_carte) + " | " "joueur2 joue: " + str(new_carte_2))
            if new_carte.domine(new_carte_2) == True:
                joueur1.ramasse(carte_a_recup)
                print("joueur1 gagne et ramasse " + str(len(carte_a_recup)) + " cartes")
                break
            else:
                joueur2.ramasse(carte_a_recup)
                print("joueur2 gagne et ramasse " + str(len(carte_a_recup)) + " cartes")
                break
    return joueur1, joueur2


def jeu(taille_jeu):
    assert taille_jeu != 52 and taille_jeu != 32, "le nombre de cartes choisi est indisponible"
    nbr_tr = 0
    p0 = creer_paquet(taille_jeu)
    p1, p2 = p0.distribuer()
    while p1.L != [] and p2.L != []:
        tour_jeu(p1, p2)
        nbr_tr +=1
        #affichage
        print("tour n°"+str(nbr_tr))
    if p1.L == []:
        print("joueur2 a gagné après " + str(nbr_tr) + " tours" )
    else:
        print("joueur1 a gagné après " + str(nbr_tr) + " tours" )

'''cette instruction  lance le programme classique de bataille avec un paquet de
longueur donnée en argument (seulement 52 et 32 sont disponibles)'''
print(jeu(52))


#statistiques___________________________________________________________________
'''tour_jeu_mute() est le meme que tour_jeu mais sans les annonces consoles'''
def tour_jeu_mute(joueur1, joueur2):
    carte_a_recup=[]
    carte = joueur1.tirer_first()
    carte_2 = joueur2.tirer_first()
    if carte.domine(carte_2) == True:
        carte_a_recup += (carte, carte_2)
        joueur1.ramasse(carte_a_recup)
    elif carte_2.domine(carte) == True:
        carte_a_recup += (carte, carte_2)
        joueur2.ramasse(carte_a_recup)
    elif carte.est_egal(carte_2) == True:
        while carte.est_egal(carte_2):
            if len(joueur1.L) < 3 or len(joueur2.L) < 3:
                if len(joueur1.L) < 3:
                    joueur1.L.append(joueur2.tirer_random())
                    joueur1.L.append(joueur2.tirer_random())
                else:
                    joueur2.L.append(joueur1.tirer_random())
                    joueur2.L.append(joueur1.tirer_random())
            carte_cache, carte_2_cache = joueur1.tirer_random(), joueur2.tirer_random()
            new_carte, new_carte_2 = joueur1.tirer_first(), joueur2.tirer_first()
            if len(carte_a_recup) > 0:
                carte_a_recup += (carte_cache, carte_2_cache, new_carte, new_carte_2)
            else:
                carte_a_recup += (carte, carte_2, carte_cache, carte_2_cache, new_carte, new_carte_2)
            if new_carte.domine(new_carte_2) == True:
                joueur1.ramasse(carte_a_recup)
                break
            else:
                joueur2.ramasse(carte_a_recup)
                break
    return joueur1, joueur2


def stat_as(nbr_diteration, taille_jeu):
    assert taille_jeu != 52 and taille_jeu != 32, "le nombre de cartes choisi est indisponible"
    as0, as1, as2, as3, as4 = 0, 0, 0 ,0, 0
    all_as0, all_as1, all_as2, all_as3, all_as4 = 0, 0, 0 ,0, 0
    for i in range(nbr_diteration):
        p0, as_dans_p1, as_dans_p2 = creer_paquet(taille_jeu), 0, 0
        p1, p2 = p0.distribuer()

        #determination du nbr d'as dans les paquets
        for i in p1.L:
            if i.valeur == 14:
                as_dans_p1 += 1
        for i in p2.L:
            if i.valeur == 14:
                as_dans_p2 += 1

        #qui gagne ?
        while p1.L != [] and p2.L != []:
            tour_jeu_mute(p1, p2)

        #nbr de fois que ... as est genere
        if as_dans_p1 == 0:
            all_as0 += 1
        elif as_dans_p1 == 1:
            all_as1 += 1
        elif as_dans_p1 == 2:
            all_as2 += 1
        elif as_dans_p1 == 3:
            all_as3 += 1
        else:
            all_as4 += 1

        if as_dans_p2 == 0:
            all_as0 += 1
        elif as_dans_p2 == 1:
            all_as1 += 1
        elif as_dans_p2 == 2:
            all_as2 += 1
        elif as_dans_p2 == 3:
            all_as3 += 1
        else:
            all_as4 += 1

        #nbr de fois que ... as gagne
        if p1.L != []:
            if as_dans_p1 == 0:
                as0 += 1
            if as_dans_p1 == 1:
                as1 += 1
            if as_dans_p1 == 2:
                as2 += 1
            if as_dans_p1 == 3:
                as3 += 1
            if as_dans_p1 == 4:
                as4 += 1
        else:
            if as_dans_p2 == 0:
                as0 += 1
            if as_dans_p2 == 1:
                as1 += 1
            if as_dans_p2 == 2:
                as2 += 1
            if as_dans_p2 == 3:
                as3 += 1
            if as_dans_p2 == 4:
                as4 += 1

    #annonce des pourcentage
    print(str(round((as0 / all_as0)*100,2)) + " % de chance de victoire avec 0 as en debut de partie")
    print(str(round((as1 / all_as1)*100,2)) + " % de chance de victoire avec 1 as en debut de partie")
    print(str(round((as2 / all_as2)*100,2)) + " % de chance de victoire avec 2 as en debut de partie")
    print(str(round((as3 / all_as3)*100,2)) + " % de chance de victoire avec 3 as en debut de partie")
    print(str(round((as4 / all_as4)*100,2)) + " % de chance de victoire avec 4 as en debut de partie")


'''la valeur en argument est le nombre de partie que le programme va jouer pour
determiner les pourcentages'''
#print(stat_as(1000, 52))


