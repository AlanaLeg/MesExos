#TP python N°4

#ex8
def nsi1(cdc):
    if "n" in cdc:
        return True
    if "s" in cdc:
        return True
    if "i" in cdc:
        return True
    else:
        return False


def nsi1(cdc):
    if ("n" in cdc)  or  ("s" in cdc) or  ("i" in cdc):
        return True
    else:
        return False

print("test exo8")
print(nsi1("numérique"))
print(nsi1("science"))
print(nsi1("Marche"))

#ex9
def nsiall(mot):
    return "n" in mot and "s" in mot and "i" in mot

print("test exo9")
print(nsiall(""))
print(nsiall("Marche"))

#ex 10
def nsicount(mot):
    n_count = 0
    s_count = 0
    i_count = 0
    total= 0
    for i in mot:
        if i == "n":
            n_count += 1
            if n_count == 1:
                total += 1

        if i == "s":
            s_count += 1
            if s_count == 1:
                total += 1

        if i == "i":
            i_count += 1
            if i_count == 1:
                total += 1
    return total


print("test exo10")
print(nsicount("Bob"))
print(nsicount("nono"))
print(nsicount("nasa"))
print(nsicount("sinus"))
