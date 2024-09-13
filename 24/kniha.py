class Kniha:
    def __init__(self, nazev, autor, rokvydani, precteno):
        self.nazev = nazev
        self.autor = autor
        self.rokvydani = rokvydani
        self.precteno = precteno

    def precti(self):
        if self.precteno == True:
            return "mam"
        else:
            return "nemam"

    def __str__(self):
        return f"{self.nazev} od {self.autor} vydano {self.rokvydani} {self.precti()} precteno"

kniha = Kniha("Borys", "Karel", "1920", True)
print(kniha)