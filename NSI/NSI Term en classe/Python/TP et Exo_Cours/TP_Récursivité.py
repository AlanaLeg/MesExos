# Créé par aleguay1, le 17/10/2024 en Python 3.7

#print(fact(4))
#print(fact(3))
#print(fact_rec(3))
#print(fact_rec(4))

#print(fibo(6))
#print(puissx(3, 0))
#print(long("numerique"))
#print(retourne_recursive("abcde"))

#ex1
def fact (n):
    p = 1
    for i in range(1, n+1):
        p=p*i
    return p

def fact_rec(n):
    if n == 0:
        return 1
    else:
        return n * fact_rec(n-1)

#ex2
def puiss2(n):
    if n==0:
        return 1
    else:
        return 2 * puiss2(n-1)

#ex3
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

#ex4
def puissx(x, n):
    if n==0:
        return 1
    else:
        return x * puissx(x, n-1)

#ex5
def long(mot):
    return len(mot)

#ex6
def retourne(mot):
    r= "mot: "
    for i in range(len(mot)):
        if i == -1:
            r= r + mot[i]

    return r

def retourne_recursive(mot):
    if len(mot) == 0:
        return ""
    return mot[-1] + retourne_recursive(mot[:-1])

#ex7
def ishere(L, e):
    if e in L:
        return True
    else:
        return False

def ishere_2(L, e):
    if len(L) == 0:
        return False
    v= L.pop(0)
    if v == e:
        return True
        return ishere_2(L, e)
    else:
        return False

#ex8
def esttrie(L):
    if len(L) == 0:
        return False
    #while len(L) != 0:
    v= L.pop(0)
    return esttrie(L[1:]) < v
    #return esttrie(L[1:]) < v

#ex9: Les Tours De Hanoï

plateau= [ [3,2,1], [ ], [ ]]

def p_depile(pile):
    pile.pop()

def p_empile(pile, e):
    n= pile.append(e)
    return n

def hanoi(n, a, b):
    # n est le nombre de disques
    # a est le numéro de la tour de départ(0 ou 1 ou 2)
    # b est le numéro de la tour  d'arrivée (0 ou 1 ou 2)
    if n > 0:
        # c correspond au numéro de la tour interméiaire (ni a ou b)
        c = ...
        # déplacer n-1 disques de la tour a vers la tour ...
        hanoi(..., ..., ...)
        # déplacer le disque restant de la tour a vers la tour b
        v= p_depile(a)
        p_empile(b, v)
        # affiche l'état du plateau
        print (plateau)
        # déplacer ... disques de la tour ... vers la tour ...


#TESTS

L0= [4, 5, 7, 10, 17]
L1= [2, 6, 8, 14, 18]
L2= [2, 1, 3, 8, 1]
Lvide= [ ]

#print(ishere(L0, 3))
#print(ishere_2(L1, 3))
print(esttrie(L1))
print(esttrie(L0))