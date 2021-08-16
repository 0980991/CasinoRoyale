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
        self.player = Player([''.join(username), 10,[]])

########### TABLES #############
class Lounge:
    def __init__(self):
        if not inf.yesNoInput('Do you have an existing account?'):
            self.player = Lobby().newPlayer()

        self.chooseGame()

    def chooseGame(self):
        choice = 1
        while choice != 0:
            inf.optionsMenuHeader('What game would you like to play today?')
            choice = inf.optionsMenu(['Highest Card', 'Black Jack', 'Highest dice toss'])

            if choice == '1':
                self.joinTable('highestcard')
            elif choice == '2':
                self.joinTable('blackjack')
            elif choice == '3':
                self.joinTable('highestdicetoss')

    def joinTable(self, gamename):
        Game(self.player, gamename).playTurn()

Lounge()
