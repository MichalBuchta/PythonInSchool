class Door:
    def __init__(self, accessCode):
        self.accessCode = accessCode
        self.open = False

    def openDoor(self, card):
        if self.accessCode % card.code == 0:
            self.open = True
            return f"Dveře jsou odemčené"
        else:
            self.open = False
            return f"Dveře jsou zamčené"

class Card:
    def __init__(self, code):
        self.code = code

dvere = Door(24)
kartaA = Card(7)
kartaB = Card(8)

print(dvere.openDoor(kartaA))
print(dvere.openDoor(kartaB))


