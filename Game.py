from gameHighestCard import HighestCard
from gameBlackJack   import BlackJack
from Deck import Deck

import InputFunctions as inf
# interface for all casino games
class Game:
    def __init__(self, player, game):
        self.deck = Deck()
        self.player = player
        self.currentbet = 0
        if game == 'highestcard':
            self.currentgame = HighestCard()

    def placeBet(self):
        self.currentbet = self.player.getCredits() + 1
        while self.currentbet > self.player.getCredits():
            self.currentbet = int(input('Please enter your bet:\n'
                                       f'Available M-Bucks: {self.player.getCredits()}\n'))

        inf.enterToContinue('Your bet has been placed')

    def playTurn(self):
        results = [None, 'continue']
        while results[1] == 'continue':
            self.placeBet()
            results = self.currentgame.start(self.deck)
            if results[0] is True:
                addorsubtract = 'add'
            else:
                addorsubtract = 'subtract'

            self.player.changeCredits(self.currentbet, addorsubtract, self.currentgame)
            self.currentbet = 0
        return

