import side_by_side
import gameHighestCard as game
import Deck as d
import Game as g
import Player as p
import helperfunctions as hf
from side_by_side import print_side_by_side
import os
from main import Lounge
# CHECK IF WINNING AND LOSING WITH D_D PICKS THE CORRECT RESULT AND APPLIES MULTIPLIER 
# lounge = Lounge()

# Highest card Unit test
""" game = game.HighestCard()
deck = d.Deck()
deck.fillDeck()
results = [True, 'continue']
while results[1] == 'continue':
    deck.fillDeck()
    results = game.start(deck, 30)
"""
# Game class new layout test
# g.Game(p.Player('usr', 'pwd', 10000), 'blackjack').playGame()

# bjd = d.BlackjackDeck()
# bjd.fillDeck()
# sum = bjd.sumCards([[11, 'hearts', 'Ace'], [11, 'spades', 'Ace'], [3, 'spades', '']])
# print(sum)
# sum = bjd.sumCards([[11, 'hearts', 'Ace'], [10, 'spades', ''], [3, 'spades', '']])
# print(sum)
# sum = bjd.sumCards([[10, 'hearts', ''], [10, 'spades', ''], [3, 'spades', '']])
# print(sum)