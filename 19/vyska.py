vyska = {
    "Kokr" : 178,
    "Bucheda" : 179,
    "Jadn" : 180,
    "Bedna" : 310,
    "Safrys" : 110,
    "Bambara" : 115,
    "Barteckos" : 180,
    "Adam" : 178,
    "kub" : 170,
    "Neger" : 185,
    "Chary" : 200,
    "Kuba" : 173,
}

setrizeny = sorted(vyska.keys())

def prumer(vysky):
    numbers = tuple(vyska.values())
    prumer = sum(numbers) / len(numbers)
    return prumer

def vypis(vysky):
    prumer_vysky = prumer(vysky)
    for jmeno in setrizeny:
        x = vyska[jmeno]
        if int(x) == int(prumer_vysky):
            print(jmeno, vyska[jmeno], "prumer")
        elif int(vyska[jmeno]) > int(prumer_vysky):
            print(jmeno, vyska[jmeno], "nadprumer")
        else:
            print(jmeno, vyska[jmeno], "podprumer")

vypis(vyska)

def od_do(vysky, od, do):
    novy_slovnik = {}
    for jmeno, vyska in vysky.items():
        if od <= vyska <= do:
            novy_slovnik[jmeno] = vyska
    return novy_slovnik
vysky_od_do = od_do(vyska, 170, 179)
print(vysky_od_do)

def prevrat(vysky, hledana_vyska):
    prevraceny_slovnik = {}
    for jmeno, vyska in vysky.items():
        if vyska == hledana_vyska:
            if vyska in prevraceny_slovnik:
                prevraceny_slovnik[vyska].append(jmeno)
            else:
                prevraceny_slovnik[vyska] = [jmeno]
    return prevraceny_slovnik
prevraceny = prevrat(vyska, 170)
print(prevraceny)