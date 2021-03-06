import random as rd
import helperfunctions as hf
import os
import time

import tkinter
import DbAPI as db

from Player import Player
from Game import Game


class Lobby:
    def __init__(self):
        self.player = None

    @classmethod
    def initializeNewPlayer(self):
        available = False
        while not available:
            username = input('Please enter your new player name\n').casefold()
            # Restart program when the user has entered 'b'
            if username == 'b':
                os.system('python main.py')
                time.sleep(2)
            available = self.verifyUsernameAvailability(username)

        password = input('Please enter your password\n')
        if password == 'b':
            os.system('python main.py')
            time.sleep(2)
        # Create player object and assign it to the current player
        return Player(''.join(username), password, 1000)

    @classmethod
    def initializeExistingPlayer(self):
        user_exists = False
        while not user_exists:
            user_credentials = hf.readUserInput(['Please enter the username of your existing account',
                                                 'What is your password?'])
            # Restart program when the user has entered 'b'
            if user_credentials == []:
                os.system('python main.py')
                time.sleep(2)
            user_credentials[0].casefold()
            if db.establishConnection(f'SELECT * FROM playerinfo WHERE username = "{user_credentials[0]}" AND password = "{user_credentials[1]}"', 'read') != []:
                user_exists = True

        return Player(''.join(user_credentials[0]), user_credentials[1])

    @classmethod
    def verifyUsernameAvailability(self, username):
        if db.establishConnection(f'SELECT * FROM playerinfo WHERE username = "{username[0]}"', 'read') != []:
            print('This username is already in use, please try another')
            return False
        return True


class Lounge:
    def __init__(self):
        self.table_names = ['highestcard', 'blackjack', 'dicetoss', 'yahtzee']             # Used to identify game types
        self.output_table_names = ['Highest Card', 'Blackjack', 'Dice Toss', 'Yahtzee']    # Used to display game names on screen

        if not hf.yesNoInput('Do you have an existing account?'):
            self.player = Lobby.initializeNewPlayer()
        else:
            self.player = Lobby.initializeExistingPlayer()

        self.chooseGame()

    def chooseGame(self, choice=2):
        option_list = self.output_table_names
        option_list.extend(['View balance', 'View statistics', 'Add funds'])

        while choice != 0:
            choice = hf.optionsMenu('What game would you like to play today?', option_list)
            if choice == -1:
                self.player = Lobby.initializeExistingPlayer()

            if choice in [1, 2, 3]:
                self.joinTable(self.table_names[choice - 1])
            elif choice == 4:
                self.checkBalance()
            elif choice == 5:
                self.checkStats()
            elif choice == 6:
                self.addFunds()

    def checkBalance(self):
        hf.prettyPrint(f'Your balance is: {self.player.getCredits()} M-Bucks')
        hf.enterToContinue()

    def checkStats(self):
        for i, table_name in enumerate(self.table_names):
            hf.prettyPrint(self.output_table_names[i])
            stats_string = self.player.getStats(table_name)
            hf.enterToContinue(stats_string)

    def joinTable(self, game_name):
        # Initialize game
        game = Game(self.player, game_name).playGame()
        # Reset game variable
        game = None

    # Super user function // Debug
    def addFunds(self):
        self.player.changeCredits(10000, 2, 'add')

if __name__ == "__main__":
    lounge = Lounge()