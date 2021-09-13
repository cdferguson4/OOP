import random

class Insect:

    def __init__(self):
        self.legs = 4
        self.wings = 2
        self.distance = 0

    def fly(self):
        self.distance = random.randint(1,10)

    def getflight(self):
        return self.distance