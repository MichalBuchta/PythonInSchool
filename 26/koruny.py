class CzechCrown:
    def __init__(self, rate):
        self.rate = rate

    def exchangeEur(self, czk):
        euro = czk / self.rate
        return f"Dostanu {euro} eur"

    def exchangeCzk(self, euro):
        czk = euro * self.rate
        return f"Dostanu {czk} kč"

crown = CzechCrown(23.26)
print(crown.exchangeEur(1000)) # 1000 korun je 40 zhruba
print(crown.exchangeCzk(50)) # 50 e je zhruba 1100czk
