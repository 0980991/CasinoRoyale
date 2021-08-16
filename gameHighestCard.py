
from InputFunctions import enterToContinue, prettyPrint
import InputFunctions as inf
import time
class HighestCard:

    def start(self, deck):
        results = []
        playercard   = deck.pullRandomCard()
        opponentcard = deck.pullRandomCard()
        while playercard[0] is opponentcard[0]:
            opponentcard = deck.pullRandomCard()


        inf.enterToContinue(f'Your hand is {deck.valueToRank(playercard[0])} of {playercard[1]}')

        inf.enterToContinue(f'Your opponent\'s card is {deck.valueToRank(opponentcard[0])} of {opponentcard[1]}')

        if playercard[0] > opponentcard[0]:
            inf.prettyPrint('You win!')
            results.append(True)

        else:
            inf.prettyPrint('You lose!')
            results.append(False)
        inf.enterToContinue()

        if not inf.yesNoInput('Do you want to continue?'):
            results.append('quit')
        else:
            results.append('continue')
        return results