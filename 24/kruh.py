import math
class Kruh:

    def __init__(self, polomer):
        self.polomer = polomer
    
    def obsah(self):
        return math.pi * self.polomer ** 2 # tady pouzivam init hovna

    def obvod(self):
        return 2 * math.pi * self.polomer

    def __str__(self):
        return f"Obvod je {self.obsah()} a Obsah je {self.obvod()}" # tady returnim ty funkce

parametry = Kruh(20)
print(parametry)
