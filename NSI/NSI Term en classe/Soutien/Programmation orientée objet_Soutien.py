
#Classes au Lycée
class Classe_de_lycee:
    def __init__(self, niveau, numéro, eleve):
        self.niveau = niveau
        self.numéro = numéro
        self.eleves = eleve

    def new_eleve(self, eleve):
        self.eleves.append(eleve)

    #les Accesseurs
    def get_niveau(self):
        return self.niveau

    def get_numéro(self):
        return self.numéro

    def get_eleves(self):
        return self.eleves

    #Les Mutateurs
    def set_niveau(self, new_niveau):
        self.niveau = new_niveau

    def set_numéro(self, new_numéro):
        self.numéro = new_numéro

    def set_eleves(self, new_eleve):
        self.eleves = new_eleve



#Les classes

classe1 = Classe_de_lycee("Seconde", 1, ["Bob", "Samuel", "Alice"])
classe2 = Classe_de_lycee("Première", 2, ["Camille", "Nicole", "Denis"])
classe3 = Classe_de_lycee("Terminale", 3, ["Zoé", "Willy", "Tiago"])

#Test de la classe Classe_de_lycee
#print(classe1.new_eleve("Lily"))
#print(classe1.eleves)
#print(classe2.new_eleve("Emile"))
#print(classe2.eleves)
#print(classe3.new_eleve("Max"))
#print(classe3.eleves)

class Eleve:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prénom = prenom
        self.age = age

    #les Accesseurs
    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prénom

    def get_age(self):
        return self.age

    #Les Mutateurs
    def set_nom(self, new_nom):
        self.nom = new_nom

    def set_prénom(self, new_prénom):
        self.prénom = new_prénom

    def set_age(self, new_age):
        self.age = new_age

eleve1 = Eleve("Sam", "Emile", 17)
eleve2 = Eleve("Dupont", "Martin", 16)
eleve3 = Eleve("Valet", "Géralde", 17)
eleve4 = Eleve("Vincelot", "Clara", 17)

classe4 = Classe_de_lycee("Terminal", 2, [eleve1, eleve2, eleve3, eleve4])
print(classe4.get_eleves())

#Jeu de rôle
class Personnage:
    def __init__(self, sorts, nom, role):
        self.sorts = sorts
        self.identité = nom
        self.rôle = role

    #les Accesseurs
    def get_identité(self):
        return self.identité

    def get_rôle(self):
        return self.rôle

    def get_sorts(self):
        return self.sorts

    #Les Mutateurs
    def set_identité(self, new_nom):
        self.identité = new_nom

    def set_rôle(self, new_role):
        self.rôle = new_role

    def set_sorts(self, new_sorts):
        self.sorts = new_sorts

class Sort:
    def __init__(self, nom, efficacité, type):
        self.nom_du_sort = nom
        self.efficacité = efficacité
        self.type = type

    #les Accesseurs
    def get_nom_du_sort(self):
        return self.nom_du_sort

    def get_efficacité(self):
        return self.efficacité

    def get_type(self):
        return self.type

    #Les Mutateurs
    def set_nom_du_sort(self, new_nom):
        self.nom = new_nom

    def set_prénom(self, new_efficacité):
        self.efficacité = new_efficacité

    def set_type(self, new_type):
        self.type = new_type

sortF = Sort("Flamme", 8, "Feu")
sortF_2 = Sort("Lame de feu", 10, "Feu")
personnage1 = Personnage([sortF, sortF_2], "Sorcière de feu", "Personnage neutre")

