def prevodnik():
    """Zadejte menu v czk na vyber mate
    eur, dollar, rubl, pesos, funkce slouzi k prevodu penez na jinou menu"""
    koruny = float(input("Zadejte měnu, kterou chcete převést v aktuálním kurzu: "))
    print("CZK: ",koruny)
    prevody = input("Vyberte měnu na kterou to chcete převést: \n EUR - 1\n Dollar - 2\n Rubl - 3 \n Pesos - 4\n: ")
    eur1 = float(0.041)
    dollar1 = float(0.040)
    rubl1 = float(2.46)
    pesos1 = float(0.78)
    a = 1
    b = 2
    c = 3
    d = 4
    if (prevody) == "1":
        eur = koruny*eur1
        print("dostanete ",round(eur, 2),"€")
    elif (prevody) == "2":
        dollar = koruny*dollar1
        print("dostanete ",round(dollar, 2),"$")
    elif (prevody) == "3":
        rubl = koruny*rubl1
        print("dostanete ",round(rubl, 2),"Rublu")
    elif (prevody) == "4":
        pesos = koruny*pesos1
        print("dostanete ",round(pesos, 2),"pesos")
    else:
        print("spatne zadane cislo")

prevodnik()