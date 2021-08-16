import random as rd
import json
import tkinter
import InputFunctions as inf
from Player import Player
from Game   import Game

class Lobby:
    def __init__(self):
        self.player = None

    def newPlayer(self):
        username = inf.readUserInput(['Please enter your player name'])
        self.player = Player([username, 10])

########### TABLES #############
class Lounge:
    def __init__(self):
        self.player = Player(['Mr House', 500, []])

    def chooseGame(self):
        choice = input('What game would you like to play today?\n'
                       '1. Highest Card\n'
                       '2. Black Jack\n'
                       '3. Highest dice toss')

        if choice == '1':
            self.joinTable('highestcard')
        elif choice == '2':
            self.joinTable('blackjack')
        elif choice == '3':
            self.joinTable('highestdicetoss')

    def joinTable(self, gamename):
        Game(self.player, gamename).playTurn()

#Lounge().chooseGame()
#Lobby().newPlayer()