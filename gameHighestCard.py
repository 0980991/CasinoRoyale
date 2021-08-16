
import time
class HighestCard:

    def start(self, deck):
        results = []
        playercard   = deck.pullRandomCard()
        opponentcard = deck.pullRandomCard()
        while playercard[0] is opponentcard[0]:
            opponentcard = deck.pullRandomCard()


        input(f'Your hand is {deck.valueToRank(playercard[0])} of {playercard[1]}\n')
        
        print(f'Your opponent\'s card is {deck.valueToRank(opponentcard[0])} of {opponentcard[1]}\n')

        if playercard[0] > opponentcard[0]:
            input('You win!')
            results.append(True)

        else:
            input('You lose!')
            results.append(False)

        continueYN = input('Do you want to quit?\n')
        if continueYN == 'Y': 
            results.append('quit')
        else:
            results.append('continue')
        return results