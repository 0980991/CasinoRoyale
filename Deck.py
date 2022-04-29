from audioop import reverse
import copy as copy
import random as r
import numpy as np
import helperfunctions as hf
from operator import itemgetter

class Deck:
    def __init__(self, add_jokers=False):
        self.suits = ["Hearts", "Diamonds", "Spades", "Clubs"]           # Hearts, Diamonds, Spades, Clubs
        self.deck = []
        self.add_jokers = add_jokers

    # Fills empty deck with 52 cards and shuffles them accordingly
    def fillDeck(self):
        for suit in range(4):
            for value in range(2, 15):
                self.deck.append([value, self.suits[suit]])

        if self.add_jokers:
            self.deck.extend([[15, 'Joker'], [15, 'Joker']] )

        self.deck = self.shuffle()

    # Shuffles the deck using random.sample()
    def shuffle(self):
        return r.sample(self.deck, 52)

    # Converts values 10 to 14 to Jack - Ace
    def valueToRank(self, value):
        if   value == 11: return 'Jack'
        elif value == 12: return 'Queen'
        elif value == 13: return 'King'
        elif value == 14: return 'Ace'
        return value

    # Prints out the current deck
    def revealDeck(self):
        for card in self.deck:
            self.printCard(card)

    # Sorts the hand in orsder
         # asc  -> Ascending
         # desc -> Descending
    def sortHand(self, hand, order='asc', sort_suits=False):
        if order == 'asc':
            sorted_hand = sorted(hand, key=itemgetter(0))
        elif order == 'desc':
            sorted_hand = sorted(hand, key=itemgetter(0), reverse=True)

        return sorted_hand

    # Prints a card
    def printCards(self, cards, horizontal=True):
        card_strings = self.formatCards(cards)
        print(cards)
        """
        for card in cards:
            card_strings.append(f'{self.valueToRank(card[0])} of {card[1]}')
        if horizontal:
            print(' | '.join(card_strings))
        else:
            for card in card_strings:
                print(card)
         """

    # Format card list to string
    def formatCards(self, cards):
        card_strings = []
        for card in cards:
            card_strings.append(f'{self.valueToRank(card[0])} of {card[1]}')
        return ' | '.join(card_strings)

    # Pulls a number of random cards
    def XpullRandomCards(self, number_of_cards, sort=True):
        hand = []
        if self.getLength() > 0 and number_of_cards < self.getLength():
            for card_nr in range(number_of_cards):
                card = r.choice(self.deck)
                hand.append(card)
                self.removeCard(self.deck.index(card))
            return self.sortHand(hand)
        self.fillDeck()

    # Pulls a random card from the deck
    def pullRandomCard(self):
        if self.getLength() > 0:
            card = r.choice(self.deck)
            self.removeCard(self.deck.index(card))
            return card
        self.fillDeck()

    # Pulls 2 random cards from the deck
    def pull2RandomCards(self):
        return [self.pullRandomCard(), self.pullRandomCard()]

    # Discards a card from the deck
    def removeCard(self, cardindex):
        self.deck.pop(cardindex)
        return

    # Add the value of all cards in a hand
    def sumCards(self, hand):
            sumcards = 0
            for card in hand:
                sumcards += card[0]
            return sumcards

    # Returns the length of the deck
    def getLength(self):
        return len(self.deck)

    # Returns whether the hand[0] is bigger than hand[1]
    def firstHandGreater(self, hands):
        if hands[0] > hands[1]:
            return True
        elif hands[1] > hands[0]:
            return False
        else: return None


class BlackjackDeck(Deck):
    def __init__(self):
        super().__init__()

    def fillDeck(self):
        for suit in range(4):
            for value in range(2, 15):
                # Sets card types in order to access them when printing a card to console
                if   value == 11: card_type = 'Jack'
                elif value == 12: card_type = 'Queen'
                elif value == 13: card_type = 'King'
                elif value == 14: card_type = 'Ace'
                else:             card_type = ''

                if value > 10 and value < 14:
                    self.deck.append([10, self.suits[suit], card_type])
                elif value == 14:
                    self.deck.append([11, self.suits[suit], card_type])
                else:
                    self.deck.append([value, self.suits[suit], card_type])

        self.deck = self.shuffle()

    # Returns a list with multiple sums depending on whether the hand contains an ace
    def sumCards(self, hand):
        all_hands = [hand]


        for hand in all_hands:
            for card in hand:
                if card[2] == 'Ace':
                    new_hand = copy.deepcopy(hand)
                    new_hand.remove(card)
                    new_hand.append([1, card[1], ''])
                    all_hands.append(new_hand)

        sums = []
        for hand in all_hands:
            sum = 0
            for card in hand:
                sum += card[0]
            sums.append(sum)

        return list(dict.fromkeys(sums))  # Removes duplicates