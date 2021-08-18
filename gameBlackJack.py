import InputFunctions as inf
from Deck import Deck
class BlackJack:
    def start(self, deck):
        results = []
        roundcount = 1
        gamenotover = True

        playerhand = deck.pull2RandomCards()
        dealerhand = deck.pull2RandomCards()
        while gamenotover:
            inf.prettyPrint('Your hand is:')
            for i in range(len(playerhand)):
                    inf.prettyPrint(f'{deck.valueToRank(playerhand[i][0])} of {playerhand[i][1]}')

            inf.enterToContinue()

            inf.prettyPrint(f'The dealer\'s hand is:')
            for i in range(len(dealerhand)):
                inf.prettyPrint(f'{deck.valueToRank(dealerhand[i][0])} of {dealerhand[i][1]}')
            inf.enterToContinue()

            if playerhand[0][0] == playerhand[1][0] and roundcount == 1:
                playeroptions = ['Hit', 'Hold', 'Double down', 'Split']

            else:
                playeroptions = ['Hit', 'Hold', 'Double down']

            choice = inf.optionsMenu('What is your next move?', playeroptions)
            if choice == 1:
                self.hit(playerhand, deck.pullRandomCard())
            elif choice == 2:
                self.hold()
            elif choice == 3:
                self.joinTable('highestdicetoss')

    def hit(self, hand, card):
        hand.append(card)

    def hold(self):
        pass

    def split(self, hand):
        pass

    def doubleDown(self):
        pass


BlackJack().start(Deck())
