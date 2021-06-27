import random as rd
import json
import tkinter

class Lobby:
    def __init__(self):
        pass

class Tables:
    def__init__(self):
        self.blackJack = BlackJack()

class Cage:
    def __init__(self):
        self.cashier = 1

########### TABLES #############
class BlackJack:
    def __init__(self):
        self.deck = Deck()



class Deck:
    def __init__(self):
        self.suits = ["H", "D", "S", "C"]           # Hearts, Diamonds, Spades, Clubs
        self.deck - []

    def Shuffle(self):
        for suit in self.suits:
