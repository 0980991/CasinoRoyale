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

########### TABLES #############


class Lounge:
    def __init__(self):
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
                                     ['Highest Card', 'Black Jack', 'Highest dice toss', 'View balance'])

            if choice == 1:
                self.joinTable('highestcard')
            elif choice == 2:
                self.joinTable('blackjack')
            elif choice == 3:
                self.joinTable('dicetoss')
            elif choice == choice == 4:
                self.checkBalance()

    def checkBalance(self):
        inf.prettyPrint(f'Your balance is: {self.player.getCredits()} M-Bucks')
        inf.enterToContinue()

    def joinTable(self, gamename):
        game = Game(self.player, gamename).playGame()
        game = None
if __name__ == '__main__':
    lounge = Lounge()
    #lounge.chooseGame(self.player, gamename).playGame`()
#Lounge()
