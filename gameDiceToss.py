import InputFunctions as inf
from asciiDice import asciiDice
from Dice import Dice
class DiceToss:
    def __init__(self):
        pass

    def start(self, dice, opponentamt):
        self.dice = None
        self.opponents = []
        self.resultplayer1 = 0
        self.outcome = None
        self.gameover = False
        self.ad = asciiDice()

        while not self.gameover:
            self.dice = dice
            self.resultplayer1 = self.dice.roll()
            self.resultplayer1 = 2

            if opponentamt == 1:
                self.opponents.append(self.dice.roll())
                while self.resultplayer1 == self.opponents[0]:
                    self.opponents[0] = self.dice.roll()

            else:
                for player in range(opponentamt):
                    self.opponents.append(self.dice.roll())

            print(f'You have rolled:\n{self.ad.getDice(self.resultplayer1)}')
            inf.enterToContinue()

            for i in range(len(self.opponents)):
                print(f'Player {i+2} has rolled:\n{self.ad.getDice(self.opponents[i])}')
                if self.opponents[i] > self.resultplayer1:
                    return self.compareRolls()
                inf.enterToContinue()

            return self.compareRolls()
        #return self.outcome

    def compareRolls(self):

        highestflag = True

        if self.resultplayer1 > max(self.opponents):
            inf.prettyPrint('YOU WIN!!!! CONGRATULATIONS')
            return [True, inf.playAgain()]
        elif self.resultplayer1 < max(self.opponents):
            inf.prettyPrint('YOU LOSE!!! better luck next time')
            return [False, inf.playAgain()]
        else:
            nrties = self.opponents.count(max(self.opponents))
            return self.start(self.dice, nrties)
        self.gameover = True


#DiceToss().start(Dice(10), 20)