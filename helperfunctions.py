import os
from numpy import append
import side_by_side as sbs
from Deck import Deck

def optionsMenu(header, options):
    # Input: List of options
    # Output: Index + 1 of the option that the user selected
    # Output: -1 if the user wants to go back in the menu
    # Makes sure that invalid input gets cancelled
    optionsMenuHeader(header)
    for i in range(len(options)):
        print(str(i+1)+'.',options[i])
    choice = input()
    if choice == 'b':
        return -1
    try:
        while int(choice) not in range(len(options)+1) or int(choice) == 0:
            print("\nInvalid option. Please try again. (1 - %s)" % len(options))
            choice = input()
    except ValueError:
        int("\nInvalid option. Please try again. (1 - %s)" % len(options))
        choice = input()
    return int(choice)

def yesNoInput(question='', default_yes=True):
    if default_yes:
        question += '(Y/n)\n'
    else:
        question += '(y/N)\n'
    user_input = input(question)

    while user_input not in ['Y', 'N', 'y', 'n', '']:
        user_input = input('Invalid input please enter y or n\n')

    if user_input == 'Y' or user_input == 'y' or (user_input == '' and default_yes):
        return True
    return False

def readUserInput(questionList):
    user_input = []
    for i, question in enumerate(questionList):
        user_input.append(input('(Press b to cancel)\n\n' + question + '\n')) ## The char escape functie zou hier aangeroepen kunnen worden
        while user_input[i] == '':
            print('This field cannot be empty')
            user_input.pop() # Removes the empty space added to list
            user_input.append(input('(Press b to cancel)\n\n' + question + '\n'))
        if user_input[i] == 'b':
            return []
    return user_input

def enterToContinue(message=''):
    input(message + '\nPlease press enter to continue...')

def pageHeader(text):
    print(f'*{(len(text)*"=")}*\n|{text}|\n*{(len(text)*"-")}*\n')

def optionsMenuHeader(text):
    print(f'{text}\n{len(text) * "-"}')

def listToQuery(valuelist):
    outputstring = '"' # double quotes needed for SQL to accept them als values
    for i, detail in enumerate(valuelist):
        if i != len(valuelist)-1:  # Adds  '", "' after every input except for the last
            outputstring += str(detail) + '", "'
        else:
            outputstring += str(detail) + '"'
    return outputstring

def formatDbRow(row, attributes):
        outputstring = (20 * '=') + '\n'
        for i, userattribute in enumerate(row):
            outputstring += attributes[i] + str(userattribute) + '\n'
        return outputstring

# Converts [(a, b, c), (d, e, f)] to [[a, b, c], [d, e, f]]
def dbOutputToList(listoftuples):
    for i, item in enumerate(listoftuples):
        listoftuples[i] = list(item)
    return listoftuples

def prettyString(msg):
    output = f'{6*"*"}{(len(msg)*"*")}\n|  {msg}  |\n{6*"*"}{(len(msg)*"*")}\n'
    return output

# Prints a box of characters around a string of any length
def prettyPrint(msg):
    print(prettyString(msg))

def appendStrings(list_of_strings, divider='|', left_border='|'):
    output = ''
    for string in list_of_strings:
        output += str(string) + divider
    return output

def appendMultiRowStrings(list_of_string_lists, divider='  |  ', divider_margin=2):
    divider = f'{divider_margin * " "}{divider}{divider_margin * " "}'
    inverted_list = [list(row) for row in zip(*list_of_string_lists)]
    output = ''
    for string_list in inverted_list:
        output += f'{appendStrings(string_list, divider)}\n'
    return output

def nestedStringArrToStrTable(list_of_string_lists, row_titles=None, col_titles=None):
    return_string = ''
    if col_titles is None:
        max_nr_of_cols = len(list_of_string_lists)
        col_titles = [str(i) for i in range(max_nr_of_cols+1)]
    if row_titles is None:
        row_titles = [str(i+1) for i in range(len(list_of_string_lists)-1)]
        # row_titles.pop()

    title_col_length = len(max(row_titles))
    title_row_length = len(max(col_titles))

    list_of_string_lists.insert(0, row_titles)
    for i, title in enumerate(col_titles):
        list_of_string_lists[i].insert(0, title)
        return_string += separateRows(list_of_string_lists[i], title_col_length, title_row_length)
    '''
    mls = separateRows(list_of_string_lists)
    mls = appendMultiRowStrings(mls, '')
    return mls
    '''

def separateRows(string_list, title_col_length, title_row_length):
    row = ''
    for string in string_list:
        row += f'+ {(title_col_length*3)*"-"} '
    row += '+\n'
    for i, string in enumerate(string_list):
        if i == 0:
            row += '|  '
        row += string
        row += f'{title_row_length*" "}|  '
        margin = int(((title_row_length + 4) - len(string)) / 2)
        # row += f'{(margin-1)*" "}{string}{margin*" "}|'
    print(row)
    return row

#### Specifically catered to this project ####
def playAgain(): # returns a boolean
    enterToContinue()
    os.system('cls')
    prettyPrint('Continue?')
    if yesNoInput():
        return 'continue'
    return 'quit'

def handleOutcome(outcome):
    prettyPrint(outcome[2])
    return [outcome[0], outcome[1]]

def stringHand(hand):
    str_hand = ''
    for i in range(len(hand)):
        str_hand += prettyString(f'{Deck().valueToRank(hand[i][0])} of {hand[i][1]}')
    return str_hand

def printHand(str_hand): # returns nothing
    for i in range(len(hand)):
        prettyPrint(f'{Deck().valueToRank(hand[i][0])} of {hand[i][1]}')

    enterToContinue()

def printBothHands(hands, sums, player_hand_nr):
    output = ['', '']
    if player_hand_nr == 1:
        output[0] += prettyString(f'Your hand is {sums[0]}:')
    else:
        output[0] += prettyString(f'Your second hand is {sums[0]}:')

    output[1] += prettyString(f'The dealer\'s hand is {sums[1]}:')
    for i, hand in enumerate(hands):
        for card in hand:
            if card[0] >= 10 and card[2] != '':
                output[i] += f'\n{card[2]} of {card[1]}'
            else:
                output[i] += f'\n{card[0]} of {card[1]}'
    sbs.print_side_by_side(output[0] , output[1])
    print('\n')

def printListSideBySide(string_list):
    output = ''
    l = []
    line_list = []
    for item in string_list:
        if '\n' in item:
            line_list = item.split('\n')
        line_list.pop()
        l.append(line_list)
    output = appendMultiRowStrings(l)
    # os.system('cls')
    print(output)
    return