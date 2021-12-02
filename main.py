import random as rd
from sqlite3 import dbapi2
import InputFunctions as inf

import tkinter
import DbAPI as db


from Player import Player
from Game import Game


class Lobby:
    def __init__(self):
        self.player = None

    def newPlayer(self):
        username = inf.readUserInput(['Please enter your player name'])
        self.player = Player([''.join(username), 1300])
        return self.player


class Lounge:
    def __init__(self):
        self.tablenames = ['highestcard', 'blackjack', 'dicetoss']
        userinfo = []
        if not inf.yesNoInput('Do you have an existing account?'):
            self.player = Lobby().newPlayer()
        else:
            while userinfo == []:

                username = inf.readUserInput(['What is your username?'])
                userinfo = db.establishConnection(
                    f'SELECT  * FROM playerinfo WHERE username = "{username[0]}"', 'read')
            self.player = Player([''.join(userinfo[0][0]), userinfo[0][1]])
        self.chooseGame()

    def chooseGame(self, choice=2):
        while choice != 0:
            choice = inf.optionsMenu('What game would you like to play today?',
                                     ['Highest Card', 'Black Jack', 'Dice toss', 'View balance', 'View statistics'])

            if choice in [1, 2, 3]:
                self.joinTable(self.tablenames[choice - 1])
            elif choice == 4:
                self.checkBalance()
            elif choice == 5:
                self.checkStats()

    def checkBalance(self):
        inf.prettyPrint(f'Your balance is: {self.player.getCredits()} M-Bucks')
        inf.enterToContinue()

    def checkStats(self):
        statsstring = self.player.getStats(self.tablenames[(inf.optionsMenu('Which game do you want to see stats from? ', ['Highest Card', 'Black Jack', 'Dice toss'])) - 1])
        inf.enterToContinue(statsstring)

    def joinTable(self, gamename):
        game = Game(self.player, gamename).playGame()
        game = None


if __name__ == '__main__':
    lounge = Lounge()