from gameHighestCard import HighestCard
from gameBlackJack   import BlackJack
from Deck import Deck
from Deck import BlackJackDeck as BJD
from Player import Player
import InputFunctions as inf
# interface for all casino games
class Game:
    def __init__(self, player, game):
        self.player = player
        self.currentbet = 0
        self.deck = None

        if   game == 'highestcard':
            self.currentgame = HighestCard()
            self.deck = Deck()
            self.deck.fillDeck()

        elif game == 'blackjack':
            self.currentgame = BlackJack()
            self.deck = BJD()
            self.deck.fillDeck()

    def placeBet(self):
        self.currentbet = self.player.getCredits() + 1
        while self.currentbet > self.player.getCredits():
            try:
                self.currentbet = int(input('Please enter your bet:\n'
                                       f'Available M-Bucks: {self.player.getCredits()}\n'))
            except ValueError:
                print('Please enter a value')
        inf.enterToContinue('Your bet has been placed')

    def playGame(self):
        results = [None, 'continue']  # [Win/Lose, 'continue/'quit']

        while results[1] == 'continue':
            self.placeBet()
            if self.deck.getLength() < 40:
                self.deck = self.deck.fillDeck()
            results = self.currentgame.start(self.deck)

            if results[0] is True:
                addorsubtract = 'add'
            elif results[0] is False:
                addorsubtract = 'subtract'
            else: # Tied game ~ Add 0
                self.currentbet = 0
                addorsubtract = 'add'

            self.player.changeCredits(self.currentbet, addorsubtract)
            self.currentbet = 0
        return

game = Game(Player([''.join("Test"), 1000]), 'blackjack')
