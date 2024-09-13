class DeLorean:
    def __init__(self, speed, year):
        self.speed = 0
        self.year = 2023

    def increaseSpeed(self):
        self.speed = self.speed + 50

    def travelToFuture(self):
        if self.speed >= 141:
            self.year = self.year + 10
            self.speed = 0
            return f"Jsme v roce {self.year}"
        else:
            return f"Musis zvysit rychlost"

    def travelToPast(self):
        if self.speed >= 141:
            self.year = self.year - 10
            self.speed = 0
            return f"Jsme v roce {self.year}"
        else:
            return f"Musis zvysit rychlost"

timemachine = DeLorean(0, 2023)
print(timemachine.travelToFuture())
timemachine.increaseSpeed()
timemachine.increaseSpeed()
timemachine.increaseSpeed()
print(timemachine.travelToFuture())
timemachine.increaseSpeed()
timemachine.increaseSpeed()
timemachine.increaseSpeed()
print(timemachine.travelToPast())