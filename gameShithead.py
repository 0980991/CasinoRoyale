from sympy import pretty
from Deck import *
import helperfunctions as hf

class Shithead():
    def __init__(self, deck, opponent_amt):
        self.deck           = deck
        self.opponent_amt   = opponent_amt
        self.player_cards   = []
        self.opponent_cards = []  # List of all cards the opponent currently has

    def start(self):
        self.initialize_cards()
        self.displayUserCards()
        # self.



    def initialize_cards(self):
        self.deck.fillDeck()
        self.player_cards = [self.deck.XpullRandomCards(3),  # Hand cards
                             self.deck.XpullRandomCards(3)]  # Face up cards
        for opponent_nr in range(self.opponent_amt):
            self.opponent_cards.append([self.deck.XpullRandomCards(3), self.deck.XpullRandomCards(3)])

    def swap_cards(self, i_hand_card, i_face_up_card):
            temp = self.player_cards[0][i_hand_card]
            self.player_cards[0][i_hand_card] = self.player_cards[1][i_face_up_card]
            self.player_cards[1][i_face_up_card] = temp

    def displayUserCards(self, ):
        player_hand_string = hf.prettyString('Your hand is:')
        player_hand_string += self.deck.formatCards(self.player_cards[0], True)
        player_hand_string += hf.prettyString('Your face up cards are:')
        player_hand_string += self.deck.formatCards(self.player_cards[0], True)


        for opponent_nr in range(self.opponent_amt):
            hf.prettyPrint(f'Opponent {opponent_nr+1}\'s face up cards are:')
            self.deck.printCards(self.player_cards[1], True)

        

        input()

    #      in_hand = [card1, card 2, card 3, ... , ... ]
    #      face_up = [card1, card 2, card 3]

