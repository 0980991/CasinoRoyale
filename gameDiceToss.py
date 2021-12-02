from Dice import Dice
import InputFunctions as inf
from asciiDice import asciiDice
class DiceToss:
    def __init__(self):
        pass

    def start(self, dice):
        self.dice = None
        self.resultplayer1 = 0
        self.resultplayer2 = 0
        self.outcome = None
        self.gameover = False
        self.ad = asciiDice()
        while not self.gameover:
            self.dice = dice
            self.resultplayer1 = self.dice.roll()
            self.resultplayer2 = self.dice.roll()

            while self.resultplayer1 == self.resultplayer2:
                self.resultplayer2 = self.dice.roll()

            print(f'Player 1 has rolled:\n{self.ad.getDice(self.resultplayer1)}')
            inf.enterToContinue()

            print(f'Player 2 has rolled:\n{self.ad.getDice(self.resultplayer2)}')
            inf.enterToContinue()

            self.compareRolls()
        return self.outcome

    def compareRolls(self):

        if self.resultplayer1 > self.resultplayer2:
            inf.prettyPrint('YOU WIN!!!! CONGRATULATIONS')
            self.outcome = [True, inf.playAgain()]
        elif self.resultplayer1 < self.resultplayer2:
            inf.prettyPrint('YOU LOSE!!! better luck next time')
            self.outcome = [False, inf.playAgain()]
        else:
            pass
        self.gameover = True

# DiceToss().start(Dice(1000))