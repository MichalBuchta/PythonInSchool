def cela_cisla():
    cislo = int(input("Zadej cislo: "))

    if (cislo) == 0:
        nula = "nula"
        print(nula)
    elif (cislo) != 0:
        nula = "neni nula"
        print(nula)
    if (cislo % 2) == 0:
        lichy = "je sudy"
        print(lichy)
    elif (cislo % 2) != 0:
        lichy = "je lichy"
        print(lichy)
    if (cislo) < 0:
        zapor = "cislo je zaporny"
        print(zapor)
    elif (cislo) > 0:
        zapor = "cislo je kladny"
        print(zapor)

cela_cisla()