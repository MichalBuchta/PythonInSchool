#Vytvořte funkci hodnoceni(vysvedceni),která jako argument přijme
#slovník hodnocení na vysvědčení. Ten obsahuje klíče (chování, předměty,
#absence) a jejich hodnoty (známky, počet hodin).

#Výstup  bude obsahovat:

## Průměr známek na vysvědčení

## Počet předmětů, že kterých byl student klasifikován/neklasifikován
## Bude vytvořen nový slovník, který bude jako klíče obsahovat známky
## a jejich hodnota bude seznam předmětů, které byly tímto stupněm
## ohodnoceny, tento slovník se také vypíše po zavolání funkce
## ve formátu:
## Hodnocení: [seznam, predmetu, hodnocenych, touto, znamkou]

## Informace o tom, zda  student/kastudoval/a s vyznamenáním
## nebo bez (průměr do 1.5, pouze jedničky a dvojky,
## všechno klasifikováno)





vysvedceni = {
    "Chování": "velmi dobré",
    "Fiktivní firma": "chvalitebný",
    "Technická angličtina": "dobrý",
    "Německý jazyk": "neklasifikováno",
    "Matematika": "výborný",
    "Český jazyk a literatura": "výborný",
    "Občanská nauka": "výborný",
    "Operační systémy": "chvalitebný",
    "Programování": "dobrý",
    "Anglický jazyk": "dobrý",
    "Právo a normy": "výborný",
    "Informační sítě": "chvalitebný",
    "Kybernetická bezpečnost": "výborný",
    "Ekonomika": "dostatečný",
    "Tělesná výchova": "dobrý",
    "Absence": 137
    }
vysvedceni2 = {
    "Chování": "velmi dobré",
    "Fiktivní firma": "výborný",
    "Technická angličtina": "výborný",
    "Německý jazyk": "výborný",
    "Matematika": "výborný",
    "Český jazyk a literatura": "výborný",
    "Občanská nauka": "výborný",
    "Operační systémy": "výborný",
    "Programování": "výborný",
    "Anglický jazyk": "výborný",
    "Právo a normy": "výborný",
    "Informační sítě": "výborný",
    "Kybernetická bezpečnost": "výborný",
    "Ekonomika": "výborný",
    "Tělesná výchova": "výborný",
    "Absence": 137
    }

setpredmety = sorted(vysvedceni.keys())
setpredemty2 = sorted(vysvedceni2.keys())

def hodnoceni(vysvedceni):
    pru = 0
    z = len(vysvedceni.values())
    for predmet in setpredmety:
        x = vysvedceni[predmet]
        print(x)
        if x == "výborný":
            pru = pru + 1
        elif x == "chvalitebný":
            pru = pru + 2
        elif x == "dobrý":
            pru = pru + 3
        elif x == "dostatečný":
            pru = pru + 4
        elif x == "neodstatečný":
            pru = pru + 5
    if "Chování" in setpredmety:
        z = z - 1

    print(pru)
    print(z)
    prumer = pru / z
    print(prumer)
    for predmet2 in setpredmety:
        y = vysvedceni[predmet]
        if prumer <= 1.5 and x != "dobrý" and x != "dostatečný" and x != "nedostatečný" and x != "neklasifikováno":
            print("Student má vyznamenání a byl ze všeho klasifikován")
            pass
        elif y == "neklasifikováno" or y == "nedostatečný":
            print("Student nebyl klasifikován")
        else:
            print("Student byl klasifikován")
hodnoceni(vysvedceni)