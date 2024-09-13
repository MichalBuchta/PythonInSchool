class Kouzelnik:
    def __init__(self, jmeno, zivoty, kouzlo, mana):
        self.jmeno = jmeno
        self.zivoty = zivoty
        self.kouzlo = kouzlo
        self.mana = mana


    def vylec_se(self):
        if self.zivoty == 100:
            return f"Nemuzes se vylecit"
        else:
            self.zivoty = 100
            return self.zivoty

    def dostan_uder(self):
        self.zivoty = self.zivoty - 10
        return self.zivoty

    def smritici_uder(self):
        self.zivoty = self.zivoty - 100
        return self.zivoty

    def nauc_se_kouzlo(self):
        self.kouzlo = abrakadabra
        return f"Kouzelnik se naucil nove kouzlo {self.kouzlo}"

    def utok(self):
        self.mana = self.mana - self.kouzlo.cena
        return f"Utokem dal {self.kouzlo.poskozeni} dmg a vzalo mu to {self.kouzlo.cena} many, nyni ma {self.mana} many"

    def __str__(self):
        if self.zivoty >= 1:
            print(self.jmeno, "je zivej")
            print("prave schytal uder a ma", self.dostan_uder() ,"zivotu")
            print("pouzil lecici lektvar a ma", self.vylec_se(), "zivotu")
            print("Kouzelnik dostal smrtici uder a ma ", self.smritici_uder(), "zivotu")
            print(self.nauc_se_kouzlo())
            print(self.jmeno, "utoci", self.utok())
            if self.zivoty >= 1:
                print(self.jmeno," je zivej s", self.zivoty ,"zivoty")
                return f"Bla"
            else:
                print(self.jmeno ,"je mrtvej")
                return f"Bla"
        else:
            return f"{self.jmeno} je mrtvej"

class Kouzlo:
    def __init__(self, jmenokouzla, poskozeni, cena):
        self.jmenokouzla = jmenokouzla
        self.poskozeni = poskozeni
        self.cena = cena

    def __str__(self):
        return f"{self.jmenokouzla} da {self.poskozeni} dmg a stoji {self.cena} many"

kouzelnik1 = Kouzelnik("Merlin", 100, 10, 50)
abrakadabra = Kouzlo("Abrakadabra", 7, 5)
print(kouzelnik1)
print(abrakadabra)