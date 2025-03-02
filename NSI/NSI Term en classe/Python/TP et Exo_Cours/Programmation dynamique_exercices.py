# ex 1. Escalier(nombre de façons de monter des marches)

def esc(n):
    assert isinstance(n, int) and n>=0, "n est un entier positif"

    if n <= 1:
        return 1

    count=[0, 1, 2]

    for i in range(3, n + 1):
        count.append(count[i - 1] + count[i - 2])

    return count[n]

# ex 2. Problème du rendu de monnaie

#r.append(L[i])
#r.append(L[i-1])

def rendu(L, s):
    r= []
    calcul = 0
    for i in range(len(L)):
        if i == s:
            r.append(i)
        elif i != s:
            while calcul != s:
                if L[i]/s == 2:
                    r.append(L[i])
                else:
                    r.append(L[i+1])

    return r


def rendudyn(L, s):
    r= [0,1]
    for i in range(2, s+1):
        L=[ ]
        for c in L:
            L.append(r[s-c]+1)
        r[i] = min(L)
    return r(s)


