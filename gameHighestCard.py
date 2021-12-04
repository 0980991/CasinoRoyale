import miscfunctions as mf

class HighestCard:

    def start(self, deck, opponentamt):
        results      = []
        opponents    = []
        playercard   = deck.pullRandomCard()
        opponentcard = deck.pullRandomCard()

        while playercard[0] is opponentcard[0]:
            opponentcard = deck.pullRandomCard()

        mf.prettyPrint(f'Your hand is {deck.valueToRank(playercard[0])} of {playercard[1]}')
        mf.enterToContinue()

        mf.prettyPrint(f'Your opponent\'s card is {deck.valueToRank(opponentcard[0])} of {opponentcard[1]}')
        mf.enterToContinue()

        if playercard[0] > opponentcard[0]:
            mf.prettyPrint('You win!')
            results.append(True)

        else:
            mf.prettyPrint('You lose!')
            results.append(False)

        if not mf.yesNoInput('Do you want to continue?'):
            results.append('quit')
        else:
            results.append('continue')
        return results
