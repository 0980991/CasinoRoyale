from multiprocessing.sharedctypes import Value
import helperfunctions as hf
from asciiDice import AsciiDice
from Dice import Dice

class Yahtzee:
    def __init__(self, dice, opponent_amt):
        self.dice = Dice(6)
        self.opponent_amt = opponent_amt
        self.nr_yahtzee_cols = 0
        self.ad = AsciiDice()

    def start(self):

        if not self.setNrYahtzeeCols():
            return

        quitting = False
        round = 0
        while not quitting and round < (13 * self.nr_yahtzee_cols):
            self.playerTurn()
            round += 1

    def playerTurn(self):
        turn_active = True
        roll_nr = 0
        while roll_nr < 3 and turn_active:
            if roll_nr == 0:
                self.rollDice(5)

    def rollDice(self, nr_of_dice):
        results = []
        for die in nr_of_dice:
            results.append(self.dice.roll())
        return results

    def setNrYahtzeeCols(self):
        while self.nr_yahtzee_cols <= 0:
            print('How many columns would you like your game to be?\n')
            nr_yahtzee_cols = input('Your must enter a value greater than 0:\n')
            if nr_yahtzee_cols == 'b':
                return False
            try:
                self.nr_yahtzee_cols = int(nr_yahtzee_cols)
            except ValueError:
                print(f'You must enter an integer value greater than 0:')
        return True
