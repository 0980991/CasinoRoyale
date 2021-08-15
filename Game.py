from gameHighestCard import HighestCard
from Deck import Deck
# interface for all casino games
class Game:
    def __init__(self, player, game):
        self.deck = Deck()
        self.player1 = player
        self.currentbet = 0
        if game == 'highestcard':
            self.currentgame = HighestCard()

    def placeBet(self):
        self.currentbet = int(input('Please enter your bet:\n'
                                   f'Available MBucks: {self.player1.getCredits()}\n'))

        input('Your bet has been placed')

    def playTurn(self):
        results = [None, 'continue']
        while results[1] == 'continue':
            self.placeBet()
            results = self.currentgame.start(self.deck)
            if results[0] is True:
                addorsubtract = 'add'
            else:
                addorsubtract = 'subtract'

            self.player1.changeCredits(self.currentbet, addorsubtract)
            self.currentbet = 0
        return

