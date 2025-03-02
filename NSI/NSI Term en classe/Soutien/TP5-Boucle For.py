#TP python N°5


maliste=[11, 12, 13]
#for i in range(3):
    #print(maliste[i])

#ex1

def somme_all(L):
    total = 0
    for i in range(len(L)):
        total += L[i]
    return total

#print(somme_all(maliste))

#ex2

def moyenne(L):
    m = 0
    for i in L:
        m += i
    return m/len(L)

#print(moyenne([10, 13]))
#print(moyenne([5, 5, 10]))

#ex3

def compte(L):
    c = 0
    for i in L:
        c += 1
    return c

print(compte([1, 12, 14, 5]))
print(compte([2, 4, 6]))

#ex4

def sumimpair(L):
    som = 0
    for i in L:
        if i%2 != 0:
            som += 1
    return som