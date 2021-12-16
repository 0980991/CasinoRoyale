from gameDiceToss import DiceToss
from gameHighestCard import HighestCard
from gameBlackJack   import BlackJack
from Deck import Deck
from Deck import BlackJackDeck as BJD
from Dice import Dice
from Player import Player
import helperfunctions as hf
# interface for all casino games
class Game:
    def __init__(self, player, game):
        self.player = player
        self.current_bet = 0
        self.deck = None
        self.usedeck = False
        self.usedice = False
        self.game_string = game

        if   game == 'highestcard':
            self.current_game = HighestCard()
            self.deck = Deck()
            self.deck.fillDeck()
            self.usedeck = True

        elif game == 'blackjack':
            self.current_game = BlackJack()
            self.deck = BJD()
            self.deck.fillDeck()
            self.usedeck = True

        elif game == 'dicetoss':
            self.current_game = DiceToss()
            self.usedice = True


    def placeBet(self):
        self.current_bet = self.player.getCredits() + 1
        while self.current_bet > self.player.getCredits():
            try:
                self.current_bet = int(input('Please enter your bet:\n'
                                       f'Available M-Bucks: {self.player.getCredits()}\n'))
            except ValueError:
                print('Please enter a value')
        hf.enterToContinue('Your bet has been placed')

    def playGame(self):
        results = [None, 'continue']  # [Win/Lose, 'continue/'quit']

        opponent_amt = 0
        while opponent_amt not in range(1, 20):
            opponent_amt = int(input('How many opponents would you like to play against? '))

        while results[1] == 'continue':
            self.placeBet()
            if self.usedeck:
                if self.deck.getLength() < 40:
                        self.deck = self.deck.fillDeck()
                        results = self.current_game.start(self.deck)

            if self.usedice:
                sides = hf.readUserInput(["How many sides should your die have?"])
                self.dice = Dice(sides[0])
                results  = self.current_game.start(self.dice, opponent_amt)

            if results[0] is None:  # The game tied...Add 0
                self.current_bet = 0
                add_or_subtract = 'add'
            elif results[0] is True:
                add_or_subtract = 'add'
            elif results[0] is False:
                add_or_subtract = 'subtract'

            self.player.changeCredits(self.current_bet, opponent_amt, add_or_subtract)
            self.player.updateStats(self.game_string, results[0])
            self.current_bet = 0
        return

#game = Game(Player([''.join("Test"), 1000]), 'blackjack')
