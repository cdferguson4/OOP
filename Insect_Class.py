import random

class Insect:

    def __init__(self,w,l):
        self.legs = l
        self.wings = w
        self.distance = 0

    def fly(self):
        self.distance = random.randint(1,10)

    def getflight(self):
        return self.distance