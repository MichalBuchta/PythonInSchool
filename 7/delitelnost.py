def delitelnost():
    index = int(input("zadej cislo ktery chces delit druhym cislem: "))
    index2 = int(input("zadej druhy cislo: "))
    if (index2) == 0:
        print("FUUJ 0 se nedeli")
    else:
        if (index % index2) == 0:
            print("cislo je delitelne druhym")
        else:
            print("neni delitnelne")
delitelnost()