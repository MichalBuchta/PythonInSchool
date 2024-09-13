seznam = []
kladna = []
zaporna = []
def roztridit(seznam):
    """Funkce roztridit vezme seznam a celý ho projde. Jestliže je v seznamu nula vypíše nula = ano a naopak.
       Funkce roztridi seznam na kladne a zaporne cisla pomoci for loopu a podminek.
       Vypise vysledek
    """
    for n in seznam:
        if n > 0:
            kladna.append(n)
        elif n < 0:
            zaporna.append(n)
    if 0 in seznam:
        print("Nula = ANO")
    else:
        print("Nula = NE")
roztridit([0,1,2,3,4,5,6,-1,-2])
print(kladna)
print(zaporna)