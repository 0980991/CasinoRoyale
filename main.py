import random as rd
from sqlite3 import dbapi2
import miscfunctions as mf

import tkinter
import DbAPI as db


from Player import Player
from Game import Game


class Lobby:
    def __init__(self):
        self.player = None

    @classmethod
    def newPlayer(self):
        usercredentials = mf.readUserInput(['Please enter your player name', 'Please enter your password'])
        # Create player object and assign it to the current player
        return Player(''.join(usercredentials[0]), usercredentials[1], 1000)

    @classmethod
    def initializeExistingPlayer(self):
        userexists = False
        while not userexists:
            usercredentials = mf.readUserInput(['What is your username?', 'What is your password?'])
            if db.establishConnection(f'SELECT * FROM playerinfo WHERE username = "{usercredentials[0]}" AND password = "{usercredentials[1]}"', 'read') != []:
                userexists = True

        return Player(''.join(usercredentials[0]), usercredentials[1])

class Lounge:
    def __init__(self):
        self.tablenames = ['highestcard', 'blackjack', 'dicetoss']
        if not mf.yesNoInput('Do you have an existing account?'):
            self.player = Lobby.newPlayer()
        else:
            self.player = Lobby.existingPlayer()

        self.chooseGame()

    def chooseGame(self, choice=2):
        while choice != 0:
            choice = mf.optionsMenu('What game would you like to play today?',
                                     ['Highest Card', 'Black Jack', 'Dice toss', 'View balance', 'View statistics'])

            if choice in [1, 2, 3]:
                self.joinTable(self.tablenames[choice - 1])
            elif choice == 4:
                self.checkBalance()
            elif choice == 5:
                self.checkStats()

    def checkBalance(self):
        mf.prettyPrint(f'Your balance is: {self.player.getCredits()} M-Bucks')
        mf.enterToContinue()

    def checkStats(self):
        statsstring = self.player.getStats(self.tablenames[(mf.optionsMenu('Which game do you want to see stats from? ', ['Highest Card', 'Black Jack', 'Dice toss'])) - 1])
        mf.enterToContinue(statsstring)

    def joinTable(self, gamename):
        game = Game(self.player, gamename).playGame()
        game = None


if __name__ == '__main__':
    lounge = Lounge()