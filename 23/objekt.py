class Zamestnanec: # trida
    def __init__(self, jmeno, pozice): # tady je init je to picovina ale funguje | smazano dovolena a zkusebni doba bo spatny zadani
        self.jmeno = jmeno
        self.pozice = pozice
        self.dovolena = 25 #Sem proste jebes ty objekty
        #self.zkusebni_doba = zkusebni_doba

    def cerpani_dovolene(self, dny): # funkce
        if self.dovolena >= dny: # podminka na dovolenou
            self.dovolena -= dny # odecita dovolenou
            return f"Muzes jit"
        else:
            return f"Nemas tolik volnych dnu, zbyva ti: {self.dovolena}"

    def vypis_informace(self): # self lol
        return f"{self.jmeno} pracuje na pozici {self.pozice} a ma {self.dovolena} dnu dovolene" # return hoven

    def __str__(self):
        x = bool(1)
        y = bool(0)
        return f"{self.jmeno} pracuje na pozici {self.pozice} a ma {self.dovolena} dnu dovolene"
        """if self.zkusebni_doba == x:
            return f"{self.vypis_informace()} je na zkusebni dobe"
        else:
            return f"{self.vypis_informace()} neni na zkusebni dobe" """

class Manazer(Zamestnanec):
    def __init__(self, jmeno, pozice, pocet_podrizenych):
        super().__init__(jmeno, pozice)
        self.pocet_podrizenych = pocet_podrizenych
        self.dovolena = 30

    def __str__(self):
        return f"{self.jmeno}, pracuje na pozici {self.pozice}. Má  {self.pocet_podrizenych} podřízených."

michal = Zamestnanec("Michal Buchta", "Sef") # objekt
kokr = Manazer("Filip Dohnal", "Manazer", 70)
marian = Manazer("Marian Přísný", "vedoucí konstrukčního oddělení", 5)

#print(michal.vypis_informace()) #print
#michal.cerpani_dovolene(3) #volani funkce
#michal.cerpani_dovolene(23) # bacha more u te funkce na return a print pak se meni volani a nebo print xd
print(michal)
print(kokr)

