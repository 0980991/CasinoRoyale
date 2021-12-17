import random as rd
import helperfunctions as hf

from tkinter import *

from View.LoungeView import *
import DbAPI as db

from PlayerController import *
from Player import Player
from Game import Game


class Lobby:
    def __init__(self):
        self.player = None



class Lounge:
    def __init__(self):
        self.table_names = ['highestcard', 'blackjack', 'dicetoss']             # Used to identify game types
        self.output_table_names = ['Highest Card', 'Blackjack', 'Dice Toss']    # Used to display game names on screen

        self.root = Tk()
        self.root.title('Casino Royale - Lounge')
        self.root.geometry('500x500')

        # Main Frame
        self.menu_frame = Frame(self.root)
        self.menu_frame.grid(row=0, column=0)
        Button(self.menu_frame, text='Start', command=self.login).pack()
        self.root.mainloop()

        self.previousframe
        # Login Frame
        self.login_frame = Frame(self.root)


    def login(self):
        self.clear(self.menu_frame)
        self.login_frame = Frame(self.root)
        self.login_frame.grid(row=0, column=0)
        Label(self.login_frame, text='Do you have an existing account?').grid(row=1, column=250)
        Button(self.login_frame, text='Yes', command=self.clickExistingPlayer).grid(row=1, column=0)
        Button(self.login_frame, text='No',  command=self.clickNewPlayer).grid(row=1, column=1)
        Button(self.login_frame, text='<--', command=self.back).grid(row=0, column=0)


    # clear screen function
    def clear(self, frame):
        slaves = frame.grid_slaves()
        for x in slaves:
            x.destroy()

    def back(self, frame):
        pass

    def clickExistingPlayer(self):
        # Clear screen
        self.clear()
        # Render text fields/labels
        menu_frame = Frame(self.root)
        Entry()
        # VerifyButton
        pass

    def clickNewPlayer(self):
        pass

    def chooseGame(self, choice=2):
        option_list = self.output_table_names
        option_list.extend(['View balance', 'View statistics'])

        while choice != 0:
            choice = hf.optionsMenu('What game would you like to play today?', option_list)

            if choice in [1, 2, 3]:
                self.joinTable(self.table_names[choice - 1])
            elif choice == 4:
                self.checkBalance()
            elif choice == 5:
                self.checkStats()

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




if __name__ == "__main__":
    lounge = Lounge()