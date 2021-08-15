import random as rd
import json
import tkinter
from Deck   import Deck
from Player import Player
from Game   import Game

class Lobby:
    def __init__(self):
        self.player = None

    def newPlayer(self):
        self.player = Player([input('Please enter your player name'), 10])

########### TABLES #############
class Lounge:
    def __init__(self):
        self.deck = Deck()
        self.player = Player(['Mr House', 500, []])
    def joinTable(self):
        Game(self.player,'highestcard').playTurn()

Lounge().joinTable()
#Lobby().newPlayer()