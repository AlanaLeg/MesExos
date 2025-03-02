
def bintodec(nb_bin):
    if len(nb_bin) == 1:
        if nb_bin == "0":
            return 0
        else:
            return 1
    else:
        if nb_bin[-1] == "0":
            bit_droit = 0
        else:
            bit_droit = 1
    return 2 * bintodec(nb_bin[:-1]) + bit_droit

print(bintodec("011"))
print(bintodec("1010"))

def dectobin(nb):
    q = nb // 2
    r = nb % 2
    if q == 0 :
        return str(r)
    else:
        return dectobin(q) + str(r)

print(dectobin(3))

def convIPbin(ipdec):
    l = ipdec.split(".")
    for i in l:
        bin = [ ]
        bin.append(dectobin(int(i)))
    return bin





print(convIPbin("90.98.100.3"))