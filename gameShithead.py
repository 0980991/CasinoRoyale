# from sympy import pretty
from Deck import *
import helperfunctions as hf

class Shithead():
    def __init__(self, deck, opponent_amt):
        self.deck           = deck
        self.opponent_amt   = opponent_amt
        self.player_cards   = []  # 0: Hand | 1: Face-up
        self.opponent_cards = []  # List of all cards the opponent currently has
        self.pot            = []

    def start(self):
        self.initialize_cards()
        self.displayUserCards()
        swapping_cards = hf.yesNoInput('Would you like to swap any cards?')
        while swapping_cards:
            i_face_up_card = hf.optionsMenu('Which face-up card would you like to add to your hand?', self.player_cards[1]) - 1
            i_hand_card = hf.optionsMenu('Which card from your hand would you like to replacec it with?', self.player_cards[0]) - 1
            self.swapCards(i_hand_card, i_face_up_card)
            self.displayUserCards()
            swapping_cards = hf.yesNoInput('Would you like to swap any cards?')

        self.displayOpponentCards()
        in_game = True
        while in_game:
            self.playerTurn()


    def initialize_cards(self):
        self.deck.fillDeck()
        self.player_cards = [self.deck.XpullRandomCards(3),  # Hand cards
                             self.deck.XpullRandomCards(3)]  # Face up cards
        for opponent_nr in range(self.opponent_amt):
            self.opponent_cards.append([self.deck.XpullRandomCards(3), self.deck.XpullRandomCards(3)])

    def swapCards(self, i_hand_card, i_face_up_card):
            temp = self.player_cards[0][i_hand_card]
            self.player_cards[0][i_hand_card] = self.player_cards[1][i_face_up_card]
            self.player_cards[1][i_face_up_card] = temp

    def displayOpponentCards(self):
        for opponent_nr in range(self.opponent_amt):
            hf.prettyPrint(f'Opponent {opponent_nr+1}\'s face up cards are:')
            hf.printHand(self.player_cards[1])
            # self.deck.printCards(self.player_cards[1], True)

    def displayUserCards(self):
        hf.prettyPrint('Your hand is:')
        player_hand_string = hf.stringHand(self.player_cards[0])
        print(player_hand_string)
        # player_hand_string += self.deck.formatCards(self.player_cards[0])
        hf.prettyPrint('Your face up cards are:')
        player_hand_string = hf.stringHand(self.player_cards[1])
        print(player_hand_string)
        # player_hand_string += self.deck.formatCards(self.player_cards[0])

    def listViablePlays(self):
        viable_plays = []
        special_cards = [2, 3, 10]
        previous_value self.pot[-1][0] # Is used to look at the previous card. If a 3 was played, it looks at the card before the 3.
        i_pot = 1
        while previous_value == 3:
            previous value == self.pot[-1 - i_pot]
        for card in self.player_cards[0]:
            is_viable = False
            if previous_value in [2, 10]:
                return self.player_cards[0] # All cards can be player after a 2
            elif previous_value == 7:
                if (card[0] <= 7 or card[0] in special_cards):
                    is_viable = True
            elif previous_value > card[0]:
                is_viable = False

            if is_viable:
                viable_plays.append(card)


        return viable_plays

    def playerTurn(self):
        choice = hf.optionsMenu('What would you like to do?', ['Play', 'Pick-up pot'])
        if choice == 1:
            card_choice = hf.optionsMenu('What card would you like to play', self.listViablePlays)
        else
            self.player_cards[0].extend(self.pot)
            self.pot = []
            # Check pot, cards
    #      in_hand = [card1, card 2, card 3, ... , ... ]
    #      face_up = [card1, card 2, card 3]

