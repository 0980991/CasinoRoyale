import random as r
import numpy as np

class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Spades", "Clubs"]           # Hearts, Diamonds, Spades, Clubs
        self.deck = []
        for suit in range(4):
            for value in range(2, 15):
                self.deck.append([value, self.suits[suit]])
        self.deck = self.shuffleDeck(self.deck)
        self.revealDeck(self.deck)

    def shuffleDeck(self, deck):
        newdeck = []
        for i in range(53):
            newdeck[i] = deck[int(r.sample(range(53), 1))]
        return newdeck

    def valueToRank(self, value):
        if   value == 11: return 'Jack'
        elif value == 12: return 'Queen'
        elif value == 13: return 'King'
        elif value == 14: return 'Ace'
        return value

    def revealDeck(self, deck): # Prints out the current deck
        for card in deck:
            print(f'{card[0]} of {card[1]}')
'''
    def generateShuffledDeck():
        deckindex = 0
        while deckindex < 52:
            exists = False
            nextcard =  [self.valueToRank(r.randint(2, 14)), self.suits[r.randint(0, 3)]]
            for j, card in enumerate(self.deck):
                if nextcard == card:
                    exists = True
                    break
            if exists is False:
                self.deck.append(nextcard)
                print(self.deck[deckindex])
                deckindex += 1
        print(len(self.deck))
'''

Deck()