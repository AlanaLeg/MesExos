# Exercice: Somme maximale des éléments d'une pyramide

p = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]

# 1) Fonction is-pyra()

def is_pyra(L):
    if len(L) == 4:
        return True
    else:
        return False

#print(is_pyra(p))

# 2) Fonctions pyra_g() et pyra_d()

def pyra_g(L):
    l=[ ]
    d=[ ]
    for i in range(len(L)):
        if i > 0:
            for j in range(len(i)):
                if len(i) == 2:
                    l.append(i[0])
                elif len(i) > 2:
                    l.append(i[:-1])
    return l


def pyra_d(L):
    pass
print(pyra_g(p))