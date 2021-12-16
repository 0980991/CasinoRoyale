import helperfunctions as hf

class HighestCard:

    def start(self, deck, opponentamt):
        results      = []
        opponents    = []
        playercard   = deck.pullRandomCard()
        opponentcard = deck.pullRandomCard()

        while playercard[0] is opponentcard[0]:
            opponentcard = deck.pullRandomCard()

        hf.prettyPrint(f'Your hand is {deck.valueToRank(playercard[0])} of {playercard[1]}')
        hf.enterToContinue()

        hf.prettyPrint(f'Your opponent\'s card is {deck.valueToRank(opponentcard[0])} of {opponentcard[1]}')
        hf.enterToContinue()

        if playercard[0] > opponentcard[0]:
            hf.prettyPrint('You win!')
            results.append(True)

        else:
            hf.prettyPrint('You lose!')
            results.append(False)

        if not hf.yesNoInput('Do you want to continue?'):
            results.append('quit')
        else:
            results.append('continue')
        return results
