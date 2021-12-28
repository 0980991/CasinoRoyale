import random as r
import numpy as np

class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Spades", "Clubs"]           # Hearts, Diamonds, Spades, Clubs
        self.deck = []

    # Fills empty deck with 52 cards and shuffles them accordingly
    def fillDeck(self):
        for suit in range(4):
            for value in range(2, 15):
                self.deck.append([value, self.suits[suit]])
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

    # Prints a card
    def printCard(self, card):
        print(f'{self.valueToRank(card[0])} of {card[1]}')

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


    def sumCards(self, hand):
        sum = []
        ace_hands = []
        for i, card in enumerate(hand):
            if card[2] == 'Ace':
                ace_hands.append([1, card[1], ''])
                ace_hands.append(hand[(i + 1) % 2])
        sum.append(hand[0][0] + hand[1][0])

        i = 0
        while i < len(ace_hands):
            sum.append(ace_hands[i][0] + ace_hands[i+1][0])
            i += 2
        return sum