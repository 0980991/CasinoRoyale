import helperfunctions as hf
from AsciiDice import AsciiDice
from Dice import Dice
class DiceToss:

    def start(self, dice, opponentamt):
        self.dice = dice                            # Dice object
        self.opponents = []                         # List of opponent scores/Index+1 is the opponent number
        self.resultplayer1 = self.dice.roll()       # The point rolled by the player
        self.ad = AsciiDice()                       # Ascii Dice object -- Controls visual aspects of the dice

        # Prevents 1v1 games to be a tie/acts as a base case when all except for 1 opponent is eliminated with tie games
        if opponentamt == 1:
            self.opponents.append(self.dice.roll())
            while self.resultplayer1 == self.opponents[0]:
                self.opponents[0] = self.dice.roll()

        else:
            # Fill opponents list with points
            for i in range(opponentamt):
                self.opponents.append(self.dice.roll())


        # Print player results
        print(f'You have rolled:\n{self.ad.getDice(self.resultplayer1)}')
        hf.enterToContinue()

        # Print opponent results
        for i in range(len(self.opponents)):
            print(f'Opponent {i+1} has rolled:\n{self.ad.getDice(self.opponents[i])}')
            hf.enterToContinue()

            # Immediately terminate the round if an opponent has a higher score
            if self.opponents[i] > self.resultplayer1:
                return self.compareRolls()

        return self.compareRolls()

    def compareRolls(self):
        # Are player results greater than the max
        if self.resultplayer1 > max(self.opponents):
            hf.prettyPrint('YOU WIN!!!! CONGRATULATIONS')
            return [True, hf.playAgain()]

        elif self.resultplayer1 < max(self.opponents):
            hf.prettyPrint('YOU LOSE!!! better luck next time')
            return [False, hf.playAgain()]

        else:
            nrties = self.opponents.count(max(self.opponents))
            return self.start(self.dice, nrties)


#DiceToss().start(Dice(10), 20)