class Balik:
    def __init__(self, cislo, adresa, hmotnost, doruceno=False):
        self.cislo = cislo
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.doruceno = doruceno

    def byldorucenbalik(self):
        if self.doruceno == False:
            return f"čeká na doručení"
        else:
            return f"byl doručen"

    def __str__(self):
        return f"Balík číslo {self.cislo} {self.byldorucenbalik()} na adresu {self.adresa}."

class Cenny_Balik(Balik):
    def __init__(self, cislo, adresa, hmotnost, hodnota, doruceno=False):
        super().__init__(cislo, adresa, hmotnost, doruceno)
        self.hodnota = hodnota

class Dorucovatel:
    def __init__(self, cislo_zamestnance, jmeno, kapacita):
        self.cislo_zamestnance = cislo_zamestnance
        self.jmeno = jmeno
        self.kapacita = kapacita

    def nalozit(self, Balik):
        if Balik.hodnota > 100000:
            if self.kapacita < Balik.hmotnost:
                return f"Nemáš dostatek kapacity na naložení balíku"
            else:
                self.kapacita = self.kapacita - Balik.hmotnost
                return f"Balík číslo {Balik.cislo} byl naložen a doručovateli {self.jmeno} zbyva {self.kapacita} kapacity gramů."
        else:
            return f"Balík má příliš vysokou hodnotu"

    def dorucit(self, Balik):
        Balik.doruceno = True
        self.kapacita = self.kapacita + Balik.hmotnost
        return f"Balík {Balik.cislo} byl doručen na {Balik.adresa} řidičem {self.jmeno}."


class Ridic(Dorucovatel):
    def __init__(self, cislo_zamestnance, jmeno):
        super().__init__(cislo_zamestnance, jmeno, kapacita=500000)

balik1 = Balik(1, "Brno", 150)
cennybalik1 = Cenny_Balik(2, "Praha", 10000, 130000)
pesidorucovatel = Dorucovatel(1, "Kokr", 30000)
ridicdorucovatel = Ridic(2, "Eda")

print(ridicdorucovatel.nalozit(cennybalik1))
print(ridicdorucovatel.dorucit(cennybalik1))
print("-----------------------------------------")
print(cennybalik1)
print(balik1)
