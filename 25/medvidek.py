class Medvidek:
    def __init__(self, jmeno, hlad, zizen, unava):
        self.jmeno = jmeno
        self.hlad = 0
        self.zizen = 0
        self.unava = 0

    def jist(self):
        if self.hlad > 10 or self.zizen > 10:
            print("Medvidek nic nevykona")
        else:
            if self.hlad < 10 and self.zizen < 10:
                self.hlad = self.hlad - 2
                self.zizen = self.zizen - 1

    def pit(self):
        if self.hlad > 10 or self.zizen > 10:
            print("Medvidek nic nevykona")
        else:
            if self.zizen < 10:
                self.zizen = self.zizen - 3

    def chuze(self):
        if self.hlad > 10 or self.zizen > 10:
            print("Medvidek nic nevykona")
        else:
            self.zizen = self.zizen + 7
            self.hlad = self.hlad + 5
            self.unava = self.unava + 5

    def spanek(self):
        if self.hlad > 10 or self.zizen > 10:
            return f"Medvidek nic nevykona"
        else:
            self.hlad = self.hlad + 3
            self.zizen = self.zizen + 3
            self.unava = self.unava - 8

    def __str__(self):
        return f"Zluty medvidek {self.jmeno} ma {self.hlad} hladu a {self.zizen} hladu a je {self.unava} unaveny"

medvidek = Medvidek("Pů", 0, 0, 0)
print(medvidek)
medvidek.chuze()
print(medvidek)
medvidek.spanek()
print(medvidek)
medvidek.pit()
medvidek.jist()
medvidek.spanek()
print(medvidek)

