from gameDiceToss import DiceToss
from gameHighestCard import HighestCard
from gameBlackjack   import Blackjack
from Deck import Deck
from Deck import BlackjackDeck as BJD
from Dice import Dice
from Player import Player
import helperfunctions as hf

# Interface for all casino games
class Game:
    def __init__(self, player, game):
        self.deck          = None
        self.player        = player
        self.exit_flag     = False
        self.current_bet   = 0
        self.game_string   = game
        self.opponent_amt  = 0
        self.game_instance = None

    # Handles creating game instances and passing game objects such as decks and dice
    def playGame(self):
        if self.player.getCredits() == 0:
            hf.enterToContinue('You are bankrupt!!!')
            return

        while not self.exit_flag:
            results = [None, 'continue']  # [Win/Lose, 'continue/'quit']
            if self.game_string != 'blackjack':
                opponents_set = self.setOpponentAmount()
                if not opponents_set:
                    return

            while results[1] == 'continue':
                if self.player.getCredits() == 0:
                    hf.enterToContinue('You are bankrupt!!!')
                    return

                multiplier = 1
                bet_placed = self.placeBet()
                if not bet_placed:
                    break
                if self.game_string == 'highestcard':
                    self.game_instance = HighestCard()
                    # Refill the deck before every game
                    self.deck = Deck()
                    self.deck.fillDeck()
                    results = self.game_instance.start(self.deck, self.opponent_amt)

                elif self.game_string == 'blackjack':
                    self.opponent_amt = 1
                    self.deck = BJD()
                    self.deck.fillDeck()
                    self.game_instance = Blackjack(self.deck, [self.player.getCredits(), self.current_bet])
                    results = self.game_instance.start()
                    multiplier = results[2]

                elif self.game_string == 'dicetoss':
                    self.game_instance = DiceToss()
                    sides = self.setDiceSides()
                    self.dice = Dice(sides)
                    results  = self.game_instance.start(self.dice, self.opponent_amt)

                if results[0] is None:  # The game tied...Add 0 (Should never happen but in case it does, the game doesnt break)
                    self.current_bet = 0
                    add_or_subtract = 'add'
                elif results[0] is True:
                    add_or_subtract = 'add'
                elif results[0] is False:
                    add_or_subtract = 'subtract'

                # Update player credits both locally and in the database
                self.player.changeCredits(self.current_bet * multiplier, self.opponent_amt, add_or_subtract)
                # Update statistics both locally and in the database
                self.player.updateStats(self.game_string, results[0])
                # Reset bet for next round
                self.current_bet = 0


            if results[1] != 'continue':
                self.exit_flag = True
        return

    # Configures the number of opponents the player faces
    def setOpponentAmount(self):
        self.opponent_amt = 0 # Used to enter the while loop
        while self.opponent_amt <= 0:
            print('Please enter the number of opponents you would like to play against')
            opponent_amt = input('Your must enter a value greater than 0:\n')
            if opponent_amt == 'b':
                return False
            try:
                self.opponent_amt = int(opponent_amt)
            except ValueError:
                print(f'You must enter an integer value greater than 0:')
        return True

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
            bet = input('Please enter your bet:\n'
                       f'Available M-Bucks: {self.player.getCredits()}\n')

            if bet == 'b':
                return False

            try:
                self.current_bet = int(bet)

            except ValueError:
                print(f'Please enter an integer value between 0 and {self.player.getCredits()} M-Bucks\n')
        hf.enterToContinue('Your bet has been placed')
        return True

