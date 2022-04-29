import random as r
class Dice:
    def __init__(self, sides, roll_history=None, roll_history_len=5):
        self.sides = int(sides)
        self.r_h = [] if None else roll_history
        self.r_h_l = roll_history_len

    def roll(self):
        output = r.randint(1, self.sides)
        self.updateRollHistory(output)
        return output

    def updateRollHistory(self, roll):
        self.r_h.insert(0, roll)
        if len(self.r_h) > self.r_h_l:
            self.r_h.pop()

class DiceHand:
    def __init__(self, dice_amt, sides) -> None:
        self.dice = dice_amt
        self.current_values = []
        for i_die in range(dice_amt):
            self.dice.append(Dice(sides))

    def roll(self):
        for die in self.dice:
            die.roll()
        self.updateCurrentValues()

    def updateCurrentValues(self):
        for dice in self.dice:
            self.current_values.append(dice.r_h[0])

    def getCurrentValues(self):
        c_v = []
        [c_v.append(die.r_h[0]) for die in self.dice]
        return c_v

    def sumDice(self):
        total_sum = 0
        for die in self.dice:
            total_sum += die.previous_roll
        return total_sum


