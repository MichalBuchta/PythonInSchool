def porovnej(x, y):
    """Funkce porovnává číslo x s číslem y a následně vypíše zda je číslo větší, menší nebo rovno a kolik je rozdíl
        Zadavejte ve formátu:
        Když si porovnáme obě čísla bez ohledu na znaménka tak záporné číslo, které je větší než kladné dáme na pozici y a naopak"""
    if x and y == x:
        print("cisla se rovnaji")
    elif x > y:
        z = y - x
        z = z * (-1)
        print("cislo ",x, "je vetsi o ", z, "nez cislo ", y)
    elif y > x:
        z = x - y
        z = z * (-1)
        print("cislo ",x, "je mensi o ", z)



porovnej(2, -6)