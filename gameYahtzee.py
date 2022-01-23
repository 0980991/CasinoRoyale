from multiprocessing.sharedctypes import Value
import helperfunctions as hf
from asciiDice import AsciiDice
from Dice import Dice

class Yahtzee:
    def __init__(self, dice, opponent_amt):
        self.dice            = Dice(6)
        self.ad              = AsciiDice()
        self.opponent_amt    = opponent_amt
        self.player_scores   = []
        self.nr_yahtzee_cols = 0

    def start(self):
        if not self.setNrYahtzeeCols():
            return

        quitting = False
        round = 0
        while not quitting and round < (13 * self.nr_yahtzee_cols):
            self.playerTurn()
            round += 1

    def playerTurn(self):
        roll_nr = 0
        nr_of_dice = 5
        saved_dice = []
        turn_active = True
        while roll_nr < 3 and turn_active:
            roll_nr += 1
            roll_values = self.rollDice(nr_of_dice)
            next_move = hf.optionsMenu(f'What is your next move?\nCurrent roll:{roll_nr}',
                                       ['Save dice', 'Roll', 'View your current scores', 'End turn', 'Quit'])

            if next_move == 1:
                curr_saved_dice = self.saveDice(roll_values)
                nr_of_dice -= len(curr_saved_dice)
                saved_dice.append(curr_saved_dice)
                if nr_of_dice != 0:
                    break

            if next_move == 2:
                continue


    def rollDice(self, nr_of_dice):
        roll_values = []
        dice_list = []
        for i in range(nr_of_dice):
            roll_values.append(self.dice.roll())
            dice_list.append(self.ad.getDice(roll_values[i]))
        hf.printDiceSideBySide(*dice_list)
        return roll_values

    def saveDice(self, roll_values):
        chosen_dice = input('Which dice would you like to save?:\n')
        while chosen_dice not in [str(val) for val in roll_values]:
            print('Please enter a valid value:\n')
            chosen_dice = input('Which dice would you like to save?:\n')

        r = [roll_values.remove(val) for val in roll_values if val != int(chosen_dice)]
        return r

    def setNrYahtzeeCols(self):
        nr_yahtzee_cols = 0
        while nr_yahtzee_cols <= 0:
            print('How many columns would you like your game to be?\n')
            nr_yahtzee_cols = input('Your must enter a value greater than 0:\n')
            if nr_yahtzee_cols == 'b':
                return False
            try:
                nr_yahtzee_cols = int(nr_yahtzee_cols)
            except ValueError:
                print(f'You must enter an integer value greater than 0:')
        self.nr_yahtzee_cols = nr_yahtzee_cols
        for player_nr in range(self.opponent_amt + 1):
            self.player_scores.append([])
            for col_nr in range (nr_yahtzee_cols):
                self.player_scores[player_nr].append(dict.fromkeys(
                                                        ['1', '2', '3', '4', '5', '5', '6',
                                                        '3_of_a_kind', '4_of_a_kind', 'full_house',
                                                        'small_street', 'large_street', 'yahtzee', 'chance'], 0
                                                        )
                                                    )
        '''
        s = ''
        for i, score in enumerate(self.player_scores):
            for col in score:
                s += str(col)
            print(f'Player {i}:\n{s}')
        '''
        return True
