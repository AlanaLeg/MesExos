# Créé par passage, le 08/02/2024 en Python 3.7


g3= {"A1": "o", "A2":"o", "A3": "x", "B1":"o", "B2":"x", "B3":"x", "C1": "x", "C2":"o", "C3":"x"}
g4= {"A1": "x", "A2":"o", "A3": "x", "B1":"o", "B2":"x", "B3":"o", "C1": "x", "C2":"o", "C3":"x"}

def affiche(grille):
    print("              ")
    print(grille["A1"],"","|", grille["B1"],"","|",grille["C1"])
    print("------------")
    print(grille["A2"],"","|", grille["B2"],"","|",grille["C2"])
    print("------------")
    print(grille["A3"],"","|", grille["B3"],"","|",grille["C3"])
    print("              ")
