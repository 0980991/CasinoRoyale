from gameDiceToss import DiceToss
from gameHighestCard import HighestCard
from gameBlackJack   import BlackJack
from Deck import Deck
from Deck import BlackJackDeck as BJD
from Dice import Dice
from Player import Player
import helperfunctions as hf

# Interface for all casino games
class Game:
    def __init__(self, player, game):
        self.deck          = None
        self.player        = player
        self.current_bet   = 0
        self.game_string   = game
        self.game_instance = None

    # Handles creating game instances and passing game objects such as decks and dice
    def playGame(self):
        results = [None, 'continue']  # [Win/Lose, 'continue/'quit']
        opponent_amt = self.setOpponentAmount()

        while results[1] == 'continue':
            self.placeBet()

            if self.game_string == 'highestcard':
                self.game_instance = HighestCard()
                self.deck = Deck()
                self.deck.fillDeck()
                # Refill the deck before every game
                if self.deck.getLength() < 40:
                    self.deck = self.deck.fillDeck()
                results = self.game_instance.start(self.deck, opponent_amt)

            elif self.game_string == 'blackjack':
                self.game_instance = BlackJack()
                self.deck = BJD()
                self.deck.fillDeck()

            elif self.game_string == 'dicetoss':
                self.game_instance = DiceToss()
                sides = self.setDiceSides()
                self.dice = Dice(sides)
                results  = self.game_instance.start(self.dice, opponent_amt)

            if results[0] is None:  # The game tied...Add 0 (Should never happen but in case it does, the game doesnt break)
                self.current_bet = 0
                add_or_subtract = 'add'
            elif results[0] is True:
                add_or_subtract = 'add'
            elif results[0] is False:
                add_or_subtract = 'subtract'

            # Update player credits both locally and in the database
            self.player.changeCredits(self.current_bet, opponent_amt, add_or_subtract)
            # Update statistics both locally and in the database
            self.player.updateStats(self.game_string, results[0])
            # Reset bet for next round
            self.current_bet = 0
        return

    # Configures the number of opponents the player faces
    def setOpponentAmount(self):
        opponent_amt = 0 # Used to enter the while loop
        while opponent_amt <= 0:
            print('Please enter the number of opponents you would like to play against')
            try:
                opponent_amt = int(input('Your must enter a value greater than 0:\n'))
            except ValueError:
                print(f'You must enter an integer value greater than 0:')
        return opponent_amt

    # Configures the number of sides on a dice
    def setDiceSides(self):
        sides = 0 # Used to enter the while loop
        while sides <= 1:
            print(f'Please enter the number of sides you dice has')
            try:
                sides = int(input('Your must enter a value greater than 1:\n'))
            except ValueError:
                print(f'You must enter an integer value greater than 1:')
        return sides

    # Places the players bet
    def placeBet(self):
        self.current_bet = self.player.getCredits() + 1 # Enables the while loop to be entered
        while self.current_bet > self.player.getCredits() or self.current_bet <= 0:
            print(f'Please enter a bet between 0 and {self.player.getCredits()} M-Bucks:\n')
            try:
                self.current_bet = int(input('Please enter your bet:\n'
                                        f'Available M-Bucks: {self.player.getCredits()}\n'))
            except ValueError:
                print(f'Please enter an integer value between 0 and {self.player.getCredits()} M-Bucks\n')
        hf.enterToContinue('Your bet has been placed')

