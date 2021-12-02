import random as r

class Dice:
    def __init__(self, sides):
        self.sides = int(sides)

    def roll(self):
        output = r.randint(1, self.sides)
        return output


