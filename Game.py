from gameDiceToss import DiceToss
from gameHighestCard import HighestCard
from gameBlackJack   import BlackJack
from Deck import Deck
from Deck import BlackJackDeck as BJD
from Dice import Dice
from Player import Player
import InputFunctions as inf
# interface for all casino games
class Game:
    def __init__(self, player, game):
        self.player = player
        self.currentbet = 0
        self.deck = None
        self.usedeck = False
        self.usedice = False

        if   game == 'highestcard':
            self.currentgame = HighestCard()
            self.deck = Deck()
            self.deck.fillDeck()
            self.usedeck = True

        elif game == 'blackjack':
            self.currentgame = BlackJack()
            self.deck = BJD()
            self.deck.fillDeck()
            self.usedeck = True

        elif game == 'dicetoss':
            self.currentgame = DiceToss()
            self.usedice = True


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
            if self.usedeck:
                if self.deck.getLength() < 40:
                        self.deck = self.deck.fillDeck()
                        results = self.currentgame.start(self.deck)

            if self.usedice:
                sides = inf.readUserInput(["How many sides should your die be?"])
                self.dice = Dice(sides[0])
                results  = self.currentgame.start(self.dice)

            if results[0] is None:  # The game tied...Add 0
                self.currentbet = 0
                addorsubtract = 'add'
            elif results[0] is True:
                addorsubtract = 'add'
            elif results[0] is False:
                addorsubtract = 'subtract'


            self.player.changeCredits(self.currentbet, addorsubtract)
            self.currentbet = 0
        return

#game = Game(Player([''.join("Test"), 1000]), 'blackjack')
